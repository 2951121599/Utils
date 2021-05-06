# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  替换列表中的数据.py
# 日期时间：2020/9/30，17:57
num = [3, 34, 45, 56, 76, 87, 78, 45, 3, 3, 3, 76]
# print(num.count(3))
for i in range(num.count(3)):  # 获取3出现的次数
    ele_index = num.index(3)  # 获取3首次出现的坐标
    num[ele_index] = 6
print(num)
