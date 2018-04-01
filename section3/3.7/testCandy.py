import cv2
import numpy as np

""" Canny边缘检测 """

# img = cv2.imread("img/CV_8U.png", 0)
img = cv2.imread("img/input.png", 0)
cv2.imwrite("img/output.png", cv2.Canny(img, 200, 300))

cv2.imshow("origin-input", cv2.imread("img/input.png"))
cv2.imshow("canny-output", cv2.imread("img/output.png"))

cv2.waitKey()
cv2.destroyAllWindows()