import cv2
import numpy as np

""" 
cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])   
    @brief Canny边缘检测
    
    :param image 需要处理的原图像, 该图像必须为单通道的灰度图
    :param threshold1 阈值1
    :param threshold2 阈值2
                     其中较大的阈值2用于检测图像中明显的边缘, 但一般情况下检测的效果不会那么完美, 边缘检测出来是断断续续的
                     所以这时候用较小的第一个阈值用于将这些间断的边缘连接起来
    :param apertureSize Sobel算子的大小, 默认为 3
    :param L2gradient 布尔值, 如果为True, 则使用更精确的L2范数进行计算（即两个方向的倒数的平方和再开放）
                              否则, 使用L1范数（直接将两个方向导数的绝对值相加）
"""

# img = cv2.imread("img/CV_8U.png", 0)
img = cv2.imread("img/input.png", 0)
cv2.imwrite("img/output.png", cv2.Canny(img, 110, 200))

cv2.imshow("origin-input", cv2.imread("img/input.png"))
cv2.imshow("canny-output", cv2.imread("img/output.png"))

cv2.waitKey()
cv2.destroyAllWindows()