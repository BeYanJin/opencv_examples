# -*-coding:utf-8-*-
import cv2

# 视频文件的读/写
videoCapture = cv2.VideoCapture('video/MyInputVid.mp4')
# 读取帧速率和帧大小
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 采用YUV颜色编码（模拟彩色电视制式采用的颜色空间, YUV与BGR之间有明确的换算公式）将其写入另一个帧中
videoWriter = cv2.VideoWriter('video/MyOutputVid.avi',
                              cv2.VideoWriter_fourcc('I', '4', '2', '0'),
                              fps, size)

# success表示是否还有帧, frame表示一帧
success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()