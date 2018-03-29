# -*-coding:utf-8-*-
import cv2
import numpy as np

# imshow() 显示一幅图像
img = cv2.imread('img/input_1.png')
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()
