# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  工具包函数_时间日期.py
# 日期时间：2021/3/11，17:39
import datetime


def get_everyday(begin_date, end_date):
    """
    获取两日期之间的每一天
    :param begin_date:开始的日期
    :param end_date:结束的日期
    :return: 两日期之间的每一天
    """
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


print(get_everyday('2021-01-01', '2021-02-11'))
