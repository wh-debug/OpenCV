# 现在我们知道了如何将BGR图像转换为HSV，我们可以使用它来提取彩色对象。在HSV中，表示颜色比在BGR颜色空间中更容易。
# 在我们的应用程序中，我们将尝试提取蓝色对象。因此，方法如下：
# 拍摄视频的每一帧
# 从BGR转换到HSV颜色空间
# 我们对HSV图像设置红色范围的阈值
# 现在单独提取红色物体，我们可以在图像上做任何我们想做的事情。

# 下面是详细注释的代码：

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    frame = cap.read()[1]

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_blue = np.array([156, 43, 46])
    upper_blue = np.array([180, 255, 255])

    # Threshold the HSV image to get only red colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()


# 图像中有一些噪音。我们将在后面的章节中看到如何删除它。
# 这是目标跟踪中最简单的方法。一旦你学会了轮廓的功能，
# 你就可以做很多事情，比如找到物体的质心并用它来跟踪物体，
# 在相机前移动你的手来绘制图表，以及其他有趣的事情。