# -*-coding:utf-8-*-
import cv2
import numpy as np
from managers import WindowManager, CaptureManager
import filters

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress, self.onMouseClick)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._filter = filters.FindEdgesFilter()

    def run(self):
        """ 运行main循环, 调用电脑摄像头 """
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            # 获取帧副本
            frame = self._captureManager.frame

            # TODO: 过滤处理帧
            # 处理帧的副本请使用 frame 变量; 若欲处理摄像头源帧, 请处理 self._captureManager.frame
            self._captureManager.frame = self._filter.strokeEdgesWhiteBg(frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """
        处理键盘事件：
             space --> 获取截图信息
             tab   --> 可启动/停止截屏（一个视频记录）
             esc   --> 退出应用程序
        """
        if keycode == 32: # space
            self._captureManager.writeImage('img/screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                print("start writing video!")
                self._captureManager.startWritingVideo('video/screencast.avi')
            else:
                print("stop writing video!")
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # esc
            self._windowManager.destroyWindow()

    def onMouseClick(self, event, x, y, flags, param):
        """ 处理鼠标事件`"""
        if event == cv2.EVENT_LBUTTONUP:
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()