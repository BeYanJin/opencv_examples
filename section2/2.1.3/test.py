# -*-coding:utf-8-*-
import cv2
import numpy as np

img = cv2.imread('img/MyPic.png')
# 获取像素坐标(150, 120)的B值
print '像素坐标(150, 120)的B值:', img.item(150, 120, 0)
# 设置像素坐标(150, 120)的B值0
img.itemset((150, 120, 0), 255)
print '像素坐标(150, 120)的新B值:', img.item(150, 120, 0)

# 用索引解决高代价的低效像素操作问题
newImgB0 = np.array(img)
newImgG0 = np.array(img)
newImgR0 = np.array(img)
# 将图像所有的B（蓝色）值设为0
newImgB0[:, :, 0] = 0;
cv2.imwrite('img/MyPic-B0.png', newImgB0)
# 将图像所有的G（绿色）值设为0
newImgG0[:, :, 1] = 0;
cv2.imwrite('img/MyPic-G0.png', newImgG0)
# 将图像所有的R（红色）值设为0
newImgR0[:, :, 2] = 0;
cv2.imwrite('img/MyPic-R0.png', newImgR0)

# ROI(Region Of Interest), 将图像的一部分拷贝到该图像的另一个位置
img = cv2.imread('img/input_1.png')
my_roi = img[0:115, 0:115]
my_roi2 = img[0:115, 115:230]
img[115:230, 0:115] = my_roi
img[115:230, 115:230] = my_roi2
cv2.imwrite('img/new_input_1.png', img)

# 获取图像三个属性
print 'img.shape:', img.shape
print 'img.size:', img.size
print 'img.dtype:', img.dtype