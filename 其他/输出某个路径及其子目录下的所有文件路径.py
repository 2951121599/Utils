# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  输出某个路径及其子目录下的所有文件路径.py
# 日期时间：2020/9/30，18:01
import os


def show_dir(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath, i)
        print(path)
        if os.path.isdir(path):  # 判断是否是目录
            show_dir(path)


filepath = "C:\\Users\\cuite\\PycharmProjects\\ML\\Utils"
show_dir(filepath)
