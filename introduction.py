import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('img/pin.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img/pin.png', cv2.IMREAD_COLOR)
img3 = cv2.imread('img/pin.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('img/pin_gray.png', img1)

# plt.imshow(img1, cmap='gray', interpolation='bicubic')
# plt.plot([50, 50], [80, 100], 'c', linewidth=5)  # plot() 函数是绘制二维图形的最基本函数
# plt.show()
