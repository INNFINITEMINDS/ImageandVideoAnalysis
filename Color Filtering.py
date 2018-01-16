import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_rad = np.array([40, 85, 70])
    upper_rad = np.array([150, 255, 255])

    # lower_rad = np.array([25, 150, 50])
    # upper_rad = np.array([255, 255, 180])

    # lower_blue = np.array([110, 50, 50])
    # upper_blue = np.array([130, 255, 255])

    # 在范围内的是白色，不在范围内的是白色
    mask = cv2.inRange(hsv_frame, lower_rad, upper_rad)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("gray_frame", hsv_frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
