# -*-coding:utf-8-*-

__author__ = 'TanYuJin'

import numpy as np
import cv2

# 2.1.1 读/写图像文件

# 3x3 像素的图像，每个像素由一个8位整数来表示
img = np.zeros((3, 3), dtype = np.uint8)
# Blue-green-red(BGR)格式
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# HSV色彩空间
# img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
# 天蓝色
img[0][0] = [0xFE, 0xE3, 0x71];
print('图像序列（BGR格式, 三维数组）：', img, '\n')
print('(高, 宽, 每个像素的通道数)：', img.shape)

# 写出图像文件
cv2.imwrite('img/MyPic.png', img)
# 读取图像文件，将文件格式更改为jpg
newImg = cv2.imread('img/MyPic.png')
cv2.imwrite('img/MyPic.jpg', newImg)
# 读取图像文件，将加载的PNG文件作为灰度图像
grayImage = cv2.imread('img/MyPic.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('img/MyPicGray.png', grayImage)

