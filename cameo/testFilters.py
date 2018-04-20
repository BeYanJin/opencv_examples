from filters import SharpenFilter, FindEdgesFilter, BlurFilter, EmbossFilter, sepFilter
import cv2
import numpy as np

"""锐化滤波器 """
img = cv2.imread('img/screenshot.png')
SharpenFilter().apply(img, img)
cv2.imwrite('img/SharpenFilter.png', img)


"""边缘检测滤波器 """
# 通过自定义核检测边缘
img = cv2.imread('img/screenshot.png')
FindEdgesFilter().apply(img, img)
cv2.imwrite('img/FindEdgesFilter.png', img)

# 在源图像基础上描绘出黑色的边缘
img = cv2.imread('img/screenshot.png')
FindEdgesFilter().strokeEdgesOriginBg(img, img)
cv2.imwrite('img/FindEdgesFilter_Laplacian_BGR.png', img)

# 将源图像背景变为黑色, 并描绘出白色的边缘
img = cv2.imread('img/screenshot.png')
img = FindEdgesFilter().strokeEdgesBlackBg(img)
cv2.imwrite('img/FindEdgesFilter_Laplacian_Black.png', img)

# 将源图像背景变为白色, 并描绘出黑色的边缘
img = cv2.imread('img/screenshot.png')
img = FindEdgesFilter().strokeEdgesWhiteBg(img)
cv2.imwrite('img/FindEdgesFilter_Laplacian_White.png', img)

# Canny函数边缘检测
img = cv2.imread('img/screenshot.png')
img = FindEdgesFilter().canny(img, 50, 150)
cv2.imwrite('img/FindEdgesFilter_canny.png', img)


""" 模糊滤波器 """
# 通过自定义核模糊化
img = cv2.imread('img/screenshot.png')
BlurFilter().apply(img, img)
cv2.imwrite('img/BlurFilter.png', img)

# blur()方法 均值滤波
img = cv2.imread('img/screenshot.png')
BlurFilter().blur(img, (5, 5), img, (-1, -1), cv2.BORDER_DEFAULT)
cv2.imwrite('img/BlurFilter_blur.png', img)

# boxFilter()方法 均值滤波
img = cv2.imread('img/screenshot.png')
BlurFilter().boxFilter(img, -1, (5, 5), img, (-1, -1), True, cv2.BORDER_DEFAULT)
cv2.imwrite('img/BlurFilter_boxFilter.png', img)

# GaussianBlur()方法 高斯滤波
img = cv2.imread('img/screenshot.png')
BlurFilter().GaussianBlur(img, (5, 5), 0, img, 0, cv2.BORDER_DEFAULT)
cv2.imwrite('img/BlurFilter_GaussianBlur.png', img)

# medianBlur()方法 高斯滤波
img = cv2.imread('img/screenshot.png')
BlurFilter().medianBlur(img, 7, img)
cv2.imwrite('img/BlurFilter_medianBlur.png', img)


""" 浮雕滤波器 """
# 通过自定义核模糊化
img = cv2.imread('img/screenshot.png')
EmbossFilter().apply(img, img)
cv2.imwrite('img/EmbossFilter.png', img)


""" 可分离滤波器 """
# ksize越大模糊程度越大, 但会趋于平稳
# sigma越大模糊程度越大, 但会趋于平稳
kernel_1 = cv2.getGaussianKernel(1, 1.5, cv2.CV_32F)
kernel_2 = cv2.getGaussianKernel(7, 1.5, cv2.CV_32F)

img = cv2.imread('img/screenshot.png')
imgHeight = img.shape[0]
imgWidth = img.shape[1]
dst_x = np.zeros((imgHeight, imgWidth), dtype = img.dtype)
dst_y = np.zeros((imgHeight, imgWidth), dtype = img.dtype)
dst_x = cv2.cvtColor(dst_x, cv2.COLOR_GRAY2BGR)
dst_y = cv2.cvtColor(dst_y, cv2.COLOR_GRAY2BGR)

# (x)横向模糊
sepFilter().sepFilter2D(img, -1, kernel_2, kernel_1, dst_x, (-1, -1), 0, cv2.BORDER_DEFAULT)
# (y)纵向模糊
sepFilter().sepFilter2D(img, -1, kernel_1, kernel_2, dst_y, (-1, -1), 0, cv2.BORDER_DEFAULT)

cv2.imwrite('img/sepFilter_x.png', dst_x)
cv2.imwrite('img/sepFilter_y.png', dst_y)
