# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  均值滤波2.py
# 当前系统日期时间：2020/7/21，15:58
"""
实现降噪

均值滤波是指任意一点的像素值，都是周围 N \times M 个像素值的均值。

中值滤波在使用邻域平均法去噪的同时也使得边界变得模糊。
而中值滤波是非线性的图像处理方法，在去噪的同时可以兼顾到边界信息的保留。
选一个含有奇数点的窗口W，将这个窗口在图像上扫描，把窗口中所含的像素点按
灰度级的升或降序排列，取位于中间的灰度值来代替该点的灰度值。

高斯滤波
     为了克服简单局部平均法的弊端(图像模糊)，目前已提出许多保持边缘、细节的局部平滑算法。
     它们的出发点都集中在如何选择邻域的大小、形状和方向、参数加平均及邻域各店的权重系数等。
     图像高斯平滑也是邻域平均的思想对图像进行平滑的一种方法，在图像高斯平滑中，对图像进行平均时，
     不同位置的像素被赋予了不同的权重。高斯平滑与简单平滑不同，它在对邻域内像素进行平均时，
     给予不同位置的像素不同的权值，下图的所示的 3\times3 和 5\times5 邻域的高斯模板。
"""
import cv2
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('./ml_data/test3.jpg')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 均值滤波
result = cv2.blur(source, (3, 3))  # 可以更改核的大小

# 显示图形
titles = ['Source Image', 'Blur Image (10, 10)']
images = [source, result]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
