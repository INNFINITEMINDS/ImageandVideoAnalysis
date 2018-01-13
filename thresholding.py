import numpy as np
import cv2

img = cv2.imread("img/pin.png")
ret, threshold = cv2.threshold(img, 95, 255, cv2.THRESH_BINARY)

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret_gray, threshold_gray = cv2.threshold(gray_scale, 95, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(gray_scale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, threshold2 = cv2.threshold(gray_scale, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("img", img)
cv2.imshow("threshold", threshold)
cv2.imshow("threshold_gray", threshold_gray)
cv2.imshow("gaus", gaus)
cv2.imshow("threshold2", threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()
