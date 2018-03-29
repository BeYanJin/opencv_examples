import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

""" 可分离滤波器 sepFilter2D
一个 2 维滤波器, 若可分离为 x 和 y 方向两个独立的 1 维滤波器, 那么该 2 维滤波器就称为 可分离滤波器

高斯滤波器就是一个典型的可分离滤波器, 具有这种性质的滤波器有快速算法, 可比不具有这个性质的普通滤波器更高效地计算
sepFilter2D(src, ddepth, kernelX, kernelY, dst=None, anchor=None, delta=None, borderType=None)

src：原始图像
ddepth： 输出图像的深度(-1表示使用原始图像的深度)
kernelX：x方向的核（领域）大小
kernelY：y方向的核（领域）大小
dst：滤波后的图像
anchor：邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
delta：在将 过滤后的像素 存储在dst之前 添加可选值
borderType：是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT

"""
img = cv2.imread('img/1.png')

# ksize越大模糊程度越大, 但会趋于平稳
# sigma越大模糊程度越大, 但会趋于平稳
kernel_1 = cv2.getGaussianKernel(1, 1.5, cv2.CV_32F)
kernel_2 = cv2.getGaussianKernel(7, 1.5, cv2.CV_32F)

# (y)纵向模糊
dst_y = cv2.sepFilter2D(img, -1, kernel_1, kernel_2)
# (x)横向模糊
dst_x = cv2.sepFilter2D(img, -1, kernel_2, kernel_1)

plt.subplot(131),\
plt.imshow(img),\
plt.title('Original')

plt.xticks([]),\
plt.yticks([])

plt.subplot(132),\
plt.imshow(dst_y),\
plt.title('Separate_Filter_Y')

plt.subplot(133),\
plt.imshow(dst_x),\
plt.title('Separate_Filter_X')

plt.xticks([]),\
plt.yticks([])
plt.show()