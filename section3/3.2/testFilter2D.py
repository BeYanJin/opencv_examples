import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

""" 通用滤波器 filter2D, 以下例子相当于一个 3 * 3 的均值滤波器
1. 当然，如果只是搞个均值滤波器，不需要这么麻烦，直接用 blur 函数就可以了
2. 但是如果我们要设计个很特殊的滤波器时，filter2D 就派上用场了。

filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)

src：原始图像
ddepth： 输出图像的深度(-1表示使用原始图像的深度)
ksize：核（领域）大小
dst：滤波后的图像
anchor：邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
delta：在将 过滤后的像素 存储在dst之前 添加可选值
borderType：是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT

"""
img = cv2.imread('img/1.png')

kernel = np.ones((3, 3),np.float32) / 9
dst = cv2.filter2D(img, -1, kernel, dst = None, anchor = (-1, -1), delta = 0, borderType = cv2.BORDER_DEFAULT)

plt.subplot(121),\
plt.imshow(img),\
plt.title('Original')

plt.xticks([]),\
plt.yticks([])

plt.subplot(122),\
plt.imshow(dst),\
plt.title('Filter2D')

plt.xticks([]),\
plt.yticks([])
plt.show()