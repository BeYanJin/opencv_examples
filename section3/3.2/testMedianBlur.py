import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

""" 中值滤波器, 是一种最常用的非线性滤波器, 它是取邻域内各点的统计中值作为输出的
1. 这种滤波器可以有效的去除椒盐噪声, 还能保持图像中各物体的边界不被模糊掉 
2. 这种滤波器只能使用正方形的邻域。

medianBlur(src, ksize, dst=None)

src：原始图像
ksize：核（领域）大小, 以下例子邻域大小为 5 * 5
dst：滤波后的图像

"""
img = cv2.imread('img/2.png')

# 中值滤波对于去除图中的细线更有效（同样大小滤波核高斯滤波会让细线模糊, 但是难以去除）
dst = cv2.medianBlur(img, 7, dst = None)

plt.subplot(121),\
plt.imshow(img),\
plt.title('Original')

plt.xticks([]),\
plt.yticks([])

plt.subplot(122),\
plt.imshow(dst),\
plt.title('Median')

plt.xticks([]),\
plt.yticks([])
plt.show()