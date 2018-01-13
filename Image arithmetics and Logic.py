import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('img/3D-Matplotlib.png')
# img2 = cv2.imread('img/mainsvmimage.png')

# add = img1+img2
# (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255).
# add = cv2.add(img1, img2)
# cv2.imshow('add', add)

# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('weighted', weighted)

img2 = cv2.imread('img/mainlogo.png')

# 我想把标志放在左上角，所以我创建了一个ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2_gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_ivk = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_ivk)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask)  # mask代表蒙版区域，即全白区域为要操作区域

dst = cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst

cv2.imshow('mask', mask)
cv2.imshow('mask_ivk', mask_ivk)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)
cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
