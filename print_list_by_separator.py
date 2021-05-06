# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  print_list_by_separator.py
# 日期时间：2021/4/19，15:37
def print_list_by_separator(li, separator):
    """
    按照分隔符打印列表
    :param li: 列表
    :param separator: 分隔符
    :return: 返回按照分割符打印的所有列表元素
    """
    print(separator.join(str(i) for i in li))
    # if separator == ',':
    #     print(",".join(str(i) for i in li))
    # elif separator == ' ':
    #     print(" ".join(str(i) for i in li))
    # elif separator == '\n':
    #     print("\n".join(str(i) for i in li))
    # else:
    #     print("输入有误!")


li = [1, 2, 3, 4]
separator = ','
print_list_by_separator(li, separator)
