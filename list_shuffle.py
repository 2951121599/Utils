# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  list_shuffle.py
# 日期时间：2021/4/19，15:47

def list_shuffle(li):
    """
    打乱列表元素
    :param li: 原列表
    """
    import random
    random.shuffle(li)


li = [1, 2, 3, 4, 5]
list_shuffle(li)  # 调用之后li反生了改变
print(li)
