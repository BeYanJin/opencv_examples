# -*-coding:utf-8-*-
import cv2
import numpy as np
import os

# 创建一个由120000个元素（1字节, 8位, 0-255）组成的数组
# os.urandom(120000)随机生成原始字节, 随后会把该字节转换为NumPy数组
# randomByteArray = bytearray(np.random.randint(0, 256, 120000))
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)
print('flatNumpyArray:', flatNumpyArray, '\tsize:', flatNumpyArray.size)

# 把数组转化为400×300, 单通道的灰度图 和 200×200, 三通道的BRG图
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('img/RandomGray.png', grayImage)
bgrImage = flatNumpyArray.reshape(200, 200, 3)
cv2.imwrite('img/RandomBgr.png', bgrImage)