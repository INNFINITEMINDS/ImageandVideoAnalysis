import cv2
import numpy as np

img = cv2.imread('img/cut.png', cv2.IMREAD_COLOR)

cv2.line(img, (1, 1), (50, 50), (2, 255, 255), 2)
cv2.rectangle(img, (60, 70), (150, 150), (0, 255, 0), 2)
cv2.circle(img, (120, 300), 55, (0, 0, 255), 12)

pts = np.array([[12, 32], [10, 50], [70, 80], [200, 90]], np.int32)
cv2.polylines(img, [pts], True, (255, 0, 0), 5)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "opencv tuts!", (0, 400), font, 2, (2, 2, 2)
            , 5)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
