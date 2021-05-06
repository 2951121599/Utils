# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  图像处理-绘制灰度直方图.py
# 当前系统日期时间：2020/7/21，15:41 
import matplotlib.pyplot as plt
import numpy as np

random_state = np.random.RandomState(19680801)
X = random_state.randn(10000)

fig, ax = plt.subplots()
ax.hist(X, bins=25, normed=True, color='yellow')
x = np.linspace(-5, 5, 1000)
ax.plot(x, 1 / np.sqrt(2 * np.pi) * np.exp(-(x ** 2) / 2), linewidth=4)
plt.show()