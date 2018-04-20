import cv2
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

""" 
threshold(src, thresh, maxval, type[, dst]) -> retval, dst
    @brief 函数 cvThreshold 对单通道数组应用固定阈值操作, 该函数的典型应用是对灰度图像进行阈值操作得到二值图像
 
    :param src 源图像
    :param thresh 进行分类的阈值
    :param maxval 高于（低于）阈值时赋予的新值
    :param type 一个方法选择参数, 常用的有： 
            • cv2.THRESH_BINARY（黑白二值） 
            • cv2.THRESH_BINARY_INV（黑白二值反转） 
            • cv2.THRESH_TRUNC （得到的图像为多像素值） 
            • cv2.THRESH_TOZERO 
            • cv2.THRESH_TOZERO_INV 
    :param dst （可选）输出图像数组, 其尺寸要和src相同
    
    该函数有两个返回值
    :return retVal 得到的阈值, 一般和thresh相同
    :return dst 阈值化后的图像
"""

img = cv2.imread('img/screenshot.png', 0) # 直接读为灰度图像

# 二值化处理，低于阈值的像素点灰度值置为0, 高于阈值的值置为参数3
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 大于阈值的像素点灰度值置为0, 小于阈值置为参数3
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 小于阈值的像素点灰度值不变, 大于阈值的像素点置为该阈值
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# 小于阈值的像素点灰度值不变, 大于阈值的像素点置为0, 其中参数3任取
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# 大于阈值的像素点灰度值不变, 小于阈值的像素点置为0, 其中参数3任取
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
figure(1)
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

ret, thresh1 = cv2.threshold(img, 45, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 45, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 45, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 45, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 45, 255, cv2.THRESH_TOZERO_INV)
titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
figure(2)
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()