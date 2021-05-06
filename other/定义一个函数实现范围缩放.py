# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  定义一个函数实现范围缩放.py
# 当前系统日期时间：2020/7/24，13:21
def MinMaxScaler(raw_samples):
    # 传统方法实现
    mms_samples = raw_samples.copy()
    for col in mms_samples.T:
        col_min = col.min()
        col_max = col.max()
        a = np.array([
            [col_min, 1],
            [col_max, 1]])
        b = np.array([0, 1])
        x = np.linalg.solve(a, b)
        col *= x[0]
        col += x[1]
    return mms_samples


if __name__ == '__main__':
    import numpy as np
    raw_samples = np.array([
        [17., 100., 4000],
        [20., 80., 5000],
        [23., 75., 5500]])
    print(MinMaxScaler(raw_samples))
