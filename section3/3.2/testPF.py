import cv2
import numpy as np
from scipy import ndimage

""" 高/低通滤波器（High/Low Pass Filter）

高通滤波器（HPF）用于检测图像的边缘
低通滤波器（LPF）用于去噪（平滑图像）, 模糊化

"""

# 用自定义卷积核来实现两个高通滤波器
kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

img = cv2.imread("img/3.png", 0)
cv2.imshow("origin", img)

# 经过 kernel_3x3 滤波处理（卷积和）后得到的图像
k3 = ndimage.convolve(img, kernel_3x3)
cv2.imshow("3x3", k3)
# 经过 kernel_5x5 滤波处理（卷积和）后得到的图像
k5 = ndimage.convolve(img, kernel_5x5)
cv2.imshow("5x5", k5)

""" 以不同的方式实现高通滤波器

1. 对图像应用低通滤波器
2. 与原始图像计算差值

"""
blurred = cv2.GaussianBlur(img, (11, 11), 0)
g_hpf = img - blurred
cv2.imshow("g_hpf(The best)", g_hpf)

cv2.waitKey()
cv2.destroyAllWindows()