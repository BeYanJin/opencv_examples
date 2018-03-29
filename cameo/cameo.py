import cv2
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress, self.onMouseClick)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """ 运行main循环 """
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # TODO: 过滤处理帧（图像）

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """ 处理键盘事件

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
        if event == cv2.EVENT_LBUTTONUP:
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()