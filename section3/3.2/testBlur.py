import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

""" 均值滤波, 这种滤波方法就是取一个像素的邻域内各像素的平均值作为滤波结果

blur(src, ksize, dst=None, anchor=None, borderType=None)

src：原始图像
ksize：核（领域）大小, 以下例子邻域大小为 5 * 5
dst：滤波后的图像
anchor：邻域的中心, 以下例子为 (-1, -1), 表明邻域的零位, 这个是默认值，如果不改变的话可以不填
borderType：是对边界的处理办法, 这个一般也不需要改变的, 默认为 cv2.BORDER_DEFAULT

"""
img = cv2.imread('img/1.png')

dst = cv2.blur(img, (5, 5), dst = None, anchor = (-1, -1), borderType = cv2.BORDER_DEFAULT)

plt.subplot(121),\
plt.imshow(img),\
plt.title('Original')

plt.xticks([]),\
plt.yticks([])

plt.subplot(122),\
plt.imshow(dst),\
plt.title('Averaging')

plt.xticks([]),\
plt.yticks([])
plt.show()