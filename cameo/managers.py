# -*-coding:utf-8-*-
import cv2
import numpy as np
import time

# 从获取流中分配图像, 再将图像分到一个或多个输出中（如图像文件、视频文件或窗口）
class CaptureManager(object):
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):

        # 若设置该特性, 则在窗口显示帧
        self.previewWindowManager = previewWindowManager
        # 让帧在窗口中镜像（水平翻转）
        self.shouldMirrorPreview = shouldMirrorPreview

        # VideoCapture类：从视频流中获取帧（图像）或帧信息
        self._capture = capture
        self._channel = 0
        # 判断是否能成功获取到帧
        self._enteredFrame = False
        # 帧（图像）
        self._frame = None
        # 输出的图像文件名
        self._imageFilename = None
        # 输出的视频文件名
        self._videoFilename = None
        # 视频编码
        self._videoEncoding = None
        # VideoWriter类（需fps, 但OpenCV不能提供准确的fps, 通过帧计数器和time.time()来估计）
        self._videoWriter = None

        # 估算fps
        self._startTime = None
        self._framesElapsed = 0
        self._fpsEstimate = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
        return self._frame

    @frame.setter
    def frame(self, value):
        if value is not None:
            self._frame = value

    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None

    def enterFrame(self):
        """获取下一个帧, 如果还有"""

        # 先检查上一个获取到的帧是否已经释放
        assert not self._enteredFrame, 'previous enteredFrame() had no matching exitFrame()'

        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):
       """在窗口中显示, 写出文件, 释放帧"""

        # 判断是否已执行过enterFrame(), 但没执行过exitFrame(), 且上一帧不是最后一帧
       if self.frame is None:
           self._enteredFrame = False
           return

       # 估算帧速率（fps）
       if self._framesElapsed == 0:
           self._startTime = time.time()
       else:
           timeElapsed = time.time() - self._startTime
           self._fpsEstimate = self._framesElapsed / timeElapsed
       self._framesElapsed += 1

       # 在窗口中显示帧, 如果真有的话
       if self.previewWindowManager is not None:
           if self.shouldMirrorPreview:
               mirroredFrame = np.fliplr(self._frame).copy()
               self.previewWindowManager.show(mirroredFrame)
           else:
               self.previewWindowManager.show(self._frame)

       # 输出为图像文件, 如果真有的话
       if self.isWritingImage:
           if self.shouldMirrorPreview:
               mirroredFrame = np.fliplr(self._frame).copy()
               cv2.imwrite(self._imageFilename, mirroredFrame)
           else:
               cv2.imwrite(self._imageFilename, self._frame)
           self._imageFilename = None

       # 输出为视频文件, 如果真有的话
       self._writeVideoFrame();

       # 释放帧
       self._frame = None
       self._enteredFrame = False

    def writeImage(self, filename):
        """"""
        self._imageFilename = filename

    def startWritingVideo(self, filename, encoding = cv2.VideoWriter_fourcc('I', '4', '2', '0')):
        """"""
        self._videoFilename = filename
        self._videoEncoding = encoding

    def stopWritingVideo(self):
        """"""
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

    def _writeVideoFrame(self):
        if not self.isWritingVideo:
            return

        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                #
                if self._framesElapsed < 20:
                    #
                    return
                else:
                    fps = self._fpsEstimate
            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps, size)

        if self.shouldMirrorPreview:
            mirroredFrame = np.fliplr(self._frame).copy()
            self._videoWriter.write(mirroredFrame)
        else:
            self._videoWriter.write(self._frame)
            


class WindowManager(object):
    def __init__(self, windowName, keypressCallback = None, mouseCallback = None):
        self.keypressCallback = keypressCallback
        self.mouseCallback = mouseCallback

        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):
        if self.mouseCallback is not None:
            cv2.setMouseCallback(self._windowName, self.mouseCallback)

        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # 在GTK编码中过滤掉所有非ASCII的部分
            keycode &= 0xFF
            self.keypressCallback(keycode)
