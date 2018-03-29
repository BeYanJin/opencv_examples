import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

""" 高斯滤波, 意义：
1. 均值滤波对邻域内各个像素采用统一的权值, 这种方式对大多数应用来说不是最佳的
2. 高斯滤波采取邻域内越靠近的值提供越大的权重的方式计算平均值, 权重的选取采用高斯函数的形式
3. 高斯函数有个非常好的特点, 就是无论在时域还是频域都是钟形的
4. 通过控制 borderType 可以控制低通滤波的截止频率

GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)

src：原始图像
ksize：核（领域）大小, 以下例子邻域大小为 5 * 5, 值越大模糊程度越大
sigmaX：一般取 0
dst：滤波后的图像
sigmaY：通常情况下 sigmaY 取与 sigmaX 相同的值, 这时可以不写出来, 也就是用它的默认值 0
borderType：高斯滤波的参数, 可用来控制低通滤波的截止滤波

"""
img = cv2.imread('img/1.png')

dst = cv2.GaussianBlur(img, (5, 5), 0, borderType = cv2.BORDER_DEFAULT)
# 计算高斯滤波器的系数, 但是它计算的是 1 维滤波器的系数
# print(cv2.getGaussianKernel(5, 4, cv2.CV_32F))


plt.subplot(121),\
plt.imshow(img),\
plt.title('Original')

plt.xticks([]),\
plt.yticks([])

plt.subplot(122),\
plt.imshow(dst),\
plt.title('Gaussian')

plt.xticks([]),\
plt.yticks([])
plt.show()