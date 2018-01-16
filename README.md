# python3 + opencv3 + numpy + matplotlib

* 安装用的anaconda,有什么安装问题可以加微信：qly6353508
* 1、OpenCV与Python介绍和加载图像教程——introduction.py
* 2、加载视频源OpenCV Python教程——vedioLoading.py
```
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

* 3、在OpenCV Python绘图和书写——drawing.py
* 4、图像操作OpenCV Python教程——imgOperation.py
* 5、图像算术和逻辑OpenCV Python教程（阈值预备）——Image arithmetics and Logic.py
* 6、阈值opencv python教程——thresholding.py
```
    cv2.adaptiveThreshold(gray_scale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
```
* 7、颜色过滤OpenCV Python教程——Color Filtering.py
```
    mask = cv2.inRange(hsv_frame, lower_rad, upper_rad)
    res = cv2.bitwise_and(frame, frame, mask=mask)
```