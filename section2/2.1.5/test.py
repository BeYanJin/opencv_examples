# -*-coding:utf-8-*-
import cv2

# 捕获摄像头的帧
cameraCapture = cv2.VideoCapture(0)
if cv2.VideoCapture.isOpened(cameraCapture):    # 是否正确构造了VideoCapture类
    # cameraCapture.get(cv2.CAP_PROP_FPS)总是返回0, VideoCapture类所使用的终端不支持所查询的这个属性, 这里先假设为30（通常的USB摄像头帧速）
    fps = 30;
    size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    videoWriter = cv2.VideoWriter('video/MyOutputVid.avi',
                                  cv2.VideoWriter_fourcc('I', '4', '2', '0'),
                                  fps, size)

    success, frame = cameraCapture.read()
    numFramesRemaining = 10 * fps - 1
    while success and numFramesRemaining > 0:
        videoWriter.write(frame)
        success, frame = cameraCapture.read()
        numFramesRemaining -= 1
    cameraCapture.release()