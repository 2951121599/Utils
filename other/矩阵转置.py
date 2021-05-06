# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  矩阵转置.py
# 当前系统日期时间：2020/7/24，22:48 
import numpy as np

samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
for i in range(samples.shape[1]):  # 列数
    col = samples[:, i]  # 所有行的第i列
    print(col)
