# -*-coding:utf-8-*-
# 作者：   29511
# 文件名:  取列表元素.py
# 日期时间：2021/4/16，11:33
def get_from_start_to_end_item(li, start, end):
    """
    获取开始到结束之间的元素
    :param li: 列表元素
    :param start: 开始位置
    :param end: 结束位置
    :return: 返回开始位置到结束位置之间的元素
    """
    return li[start:end + 1]


def get_in_addition_from_start_to_end_item(li, start, end):
    """
    获取除开始到结束之外的元素
    :param li: 列表元素
    :param start: 开始位置
    :param end: 结束位置
    :return: 返回开始位置到结束位置之间的元素
    """
    return li[start:end + 1]


def get_elements_other_than_start_to_end(li, start, end):
    """
    获取除开始到结束之外的元素
    :param li: 列表元素
    :param start: 开始位置
    :param end: 结束位置
    :return:返回除开始到结束之外的元素
    """
    return li[:start] + li[end + 1:]


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7]
    start = 2
    end = 4
    print(get_from_start_to_end_item(li, start, end))
    print(get_elements_other_than_start_to_end(li, start, end))
