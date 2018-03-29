import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

""" 均值滤波：与 blur 函数相关的 boxFilter 函数

boxFilter(src, ddepth, ksize, dst=None, anchor=None, normalize=None, borderType=None)

src：原始图像
ddepth： 输出图像的深度(-1表示使用原始图像的深度)
dst：滤波后的图像
ksize：核（领域）大小, 以下例子邻域大小为 5 * 5
anchor：邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
normalize：等于 false 时相当于邻域内各像素的数值求和
           等于 true 时，计算结果等效于 blur 函数
borderType：是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT

"""
img = cv2.imread('img/1.png')

dst = cv2.boxFilter(img, -1, (5, 5), dst = None, anchor = (-1, -1), normalize = True, borderType = cv2.BORDER_DEFAULT)

plt.subplot(121), \
plt.imshow(img), \
plt.title('Original')

plt.xticks([]), \
plt.yticks([])

plt.subplot(122), \
plt.imshow(dst), \
plt.title('BoxFilter')

plt.xticks([]), \
plt.yticks([])
plt.show()