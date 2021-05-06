# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  合并文件.py
# 日期时间：2021/4/15，17:38
import os
import pandas as pd


def merge_simple_sample_file(root_path):
    """
    合并多个单个文件里面的内容, 共用相同列名
    :param root_path: 多个单个文件的存放路径
    :return: 返回 merge_result.csv 存放位置为当前程序所在路径
    """
    header = pd.read_csv(os.path.join(root_path, os.listdir(root_path)[0]), header=None).values[0, :]
    res = None
    for file in os.listdir(root_path):
        file_path = os.path.join(root_path, file)
        df = pd.read_csv(file_path)
        res = pd.concat([res, df], axis=0)

    res.to_csv('merge_result.csv', index=False, header=header)
    print("merge success! ")


def merge_simple_sample_file_no_header(root_path):
    """
    合并多个单个文件里面的内容, 文件无列名
    :param root_path: 多个单个文件的存放路径
    :return: 返回 merge_result_no_header.csv 存放位置为当前程序所在路径
    """
    res = None
    for file in os.listdir(root_path):
        file_path = os.path.join(root_path, file)
        df = pd.read_csv(file_path, header=None)
        res = pd.concat([res, df], axis=0)
    res.to_csv('merge_result_no_header.csv', index=False, header=False)
    print("merge success! ")


if __name__ == '__main__':
    root_path = "simple_sample"
    merge_simple_sample_file(root_path)
    # root_path = "simple_sample_no_header"
    # merge_simple_sample_file_no_header(root_path)