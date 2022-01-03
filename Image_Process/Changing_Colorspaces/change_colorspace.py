# 在OpenCv中有150多种颜色空间的方法，但是经常见到有两种，一种是BGR->Gray,另一种是BGR->HSV
# 颜色空间的转换一般使用函数cv.cvtColor(input_image, flag) 
# 对于BGR->Gray的转换一般使用的flag是cv.COLOR_BGR2GRAY
# 对于BGR->HSV 的转换一般使用的flag是 cv.COLOR_BGR2HSV
# 通过运行下面的代码来看看opencv中的颜色空间的种类
# 对于HSV，色调范围为[0179]，饱和度范围为[0255]，值的范围为[0255]。不同的软件使用不同的尺度。因此，如果要将opencv值与它们进行比较，则需要规范化这些范围。

import numpy as np
import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')] # dir 函数查看当前模块的属性列表 如果是COLOR_开头的 打印出来
print(flags)
print(len(flags))