# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  list分块.py
# 日期时间：2021/3/10，17:32
from math import ceil
from itertools import chain


def chunk(li, size):
    """
    给定具体的大小，定义一个函数以按照这个大小切割列表。
    :param li: 要切割列表
    :param size: 切割大小
    :return: 切割好的列表
    """
    return list(map(lambda x: li[x * size:x * size + size], list(range(0, ceil(len(li) / size)))))


print(chunk([1, 2, 3, 4, 5], 2))  # [[1,2],[3,4],5]


def compact(li):
    """
    将布尔型的值去掉
    :param li: 传入一个列表
    :return: 返回去掉布尔型的值的列表
    """
    return list(filter(bool, li))


print(compact([0, 1, False, 2, '', 3, 'a', 's', 34]))  # [ 1, 2, 3, 'a', 's', 34 ]


def unpack(li):
    """
    解包:可以将打包好的成对列表解开成两组不同的元组
    :param li:打包好的成对列表
    :return:解开成两组不同的元组
    """
    return zip(*li)


print(unpack([['a', 'b'], ['c', 'd'], ['e', 'f']]))  # [('a', 'c', 'e'), ('b', 'd', 'f')]


def connection_list_string(li):
    """
    将列表连接成单个字符串，且每一个元素间的分隔方式设置为了逗号。
    :param li: 传入的列表
    :return: 返回逗号分隔的一个字符串
    """
    return ', '.join(li)


print(connection_list_string(["basketball", "football", "swimming"]))  # basketball, football, swimming


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    """
    通过递归的方式将列表的嵌套展开为单个列表
    :param lst: 嵌套的列表
    :return: 展开为单个列表
    """
    result = []
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


print(deep_flatten([1, [2], [[3], 4], 5]))  # [1, 2, 3, 4, 5]


def spread2(li):
    """
    将列表内的所有元素，包括子列表，都展开成一个列表。
    :param li:传入一个列表(包含子列表)
    :return:返回展开后的列表
    """
    ret = []
    for i in li:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


print(spread2([1, 2, 3, [4, 5, 6], [7], 8, 9]))


def difference(a, b):
    """
    返回第一个列表的元素，其不在第二个列表内。
    :param a:第一个列表
    :param b:第二个列表
    :return:返回列表1-列表2的元素
    """
    set_a = set(a)
    set_b = set(b)
    comparison_a_b = set_a.difference(set_b)
    # comparison_b_a = set_b.difference(set_a)
    return list(comparison_a_b)


print(difference([1, 2, 3], [1, 2, 4]))  # [3]


def has_duplicates(li):
    """
    检查两个列表是不是有重复项
    :param li:
    :return: 返回True或False
    """
    return len(li) != len(set(li))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
print(has_duplicates(x))  # True
print(has_duplicates(y))  # False


def merge_dictionaries(a, b):
    """
    合并两个字典
    :param a:
    :param b:
    :return: 合并后的字典
    """
    return {**a, **b}


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))  # {'x': 1, 'y': 3, 'z': 4}


def to_dictionary(keys, values):
    """
    将两个列表转化为单个字典
    :param keys:第一个列表作为键
    :param values:第二个列表作为值
    :return:返回合并之后的字典
    """
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))  # {'a': 2, 'b': 3, 'c': 4}


def most_frequent(li):
    """
    根据元素频率取列表中最常见的元素
    :param li:要传入的列表
    :return:返回出现次数最多的元素
    """
    return max(set(li), key=li.count)


print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))  # 2


def lower_list(li):
    """
    列表元素都变为小写
    :param li: 传入的列表
    :return: 返回变为小写的元素列表
    """
    return [i.lower() for i in li]


print(lower_list(['Hello', 'World']))


def list_merge_deduplication(li1, li2):
    """
    列表合并之后去重
    :param li1: 列表1
    :param li2:列表2
    :return: 返回合并去重之后的列表
    """
    return list(set(li1 + li2))


print(list_merge_deduplication([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]))  # [1, 2, 3, 4, 5, 6, 8, 10]


def matrix_to_list(matrix):
    """
    将多维矩阵转换为一维列表
    :param matrix: 多维矩阵
    :return: 转换后的一维列表
    """
    return list(chain.from_iterable(matrix))


print(matrix_to_list(
    [[1, 2],
     [3, 4, 9],
     [4, 5, 6]]
))  # [1, 2, 3, 4, 9, 4, 5, 6]


def merge_dict(dict1, dict2):
    """
    合并两个字典, 若键相同, 则覆盖之前的
    :param dict1: 字典1
    :param dict2: 字典2
    :return: 返回合并后的字典
    """
    return {**dict1, **dict2}


dict1 = {
    'a': 1,
    'b': 2
}

dict2 = {
    'c': 3,
    'd': 4
}

print(merge_dict(dict1, dict2))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def get_some_item(num_list, n):
    """
    for循环每次取n个数据
    :param num_list: 传入的列表
    :param n: 每次取出 n个元素
    :return: 返回每n个元素为一组的列表
    """
    return [num_list[i:i + n] for i in range(0, len(num_list), n)]


for item in get_some_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5):
    print(item)  # [1, 2, 3, 4, 5] [6, 7, 8, 9, 0]


def take_second(item):
    """
    取第二个元素
    :param item:
    :return:
    """
    return item[1]


# 返回按照第二个元素排序的列表
li = [(2, 2), (3, 4), (4, 1), (1, 5)]
li.sort(key=take_second)
print(li)  # [(4, 1), (2, 2), (3, 4), (1, 5)]


def print_list_item(li):
    """
    打印列表元素
    :param li:
    :return:
    """
    res = []
    for i in range(li):
        res.append(i)
        yield res


for item in print_list_item(10):
    print(item)
