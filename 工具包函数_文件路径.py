# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  工具包函数_文件路径.py
# 日期时间：2021/3/11，17:50
# python中sys, getopt模块处理命令行参数
# import sys
# print("脚本名：", sys.argv[0])
# for i in range(1, len(sys.argv)):
#     print("参数", i, sys.argv[i])


# 文件名:  列出路径下的文件.py
import os
import pandas as pd
import fnmatch


def file_under_the_path(path):
    for curDir, dirs, files in os.walk(path):
        print("现在的目录：", curDir)
        print("该目录下包含的子目录：", str(dirs))
        print("该目录下包含的文件：", str(files))
        print('\n')


# file_under_the_path('../Utils')

# 文件名:  .py

# TODO
def list_of_files_in_the_upper_folder():
    """
    列出上层目录下的所有文件和文件夹名称列表
    :return: 返回一个保存好的csv文件
    """
    print(os.path.abspath('.'))
    filename = [item for item in os.listdir('.')]
    data = pd.DataFrame({'filename': filename})
    print(data)
    # data.to_csv('./demo.csv', index=False, header=False)


# print(list_of_files_in_the_upper_folder())


# import os
# import fnmatch
def iter_files(walk_path, file_type="*.*"):
    """
    获取遍历路径下所有某一类型的文件的完整路径
    :param walk_path: 要遍历的路径
    :param file_type: 文件的类型
    :return: 返回所有此路径下所有的这一文件类型文件的完整路径
    """
    for path, dirs, files in os.walk(walk_path):
        for filename in fnmatch.filter(files, file_type):
            yield os.path.join(path, filename)


file_type = "*.py"
walk_path = ".\\20210324_fresh_0h_run1\\XIC"

with open("file_list.log", 'wt') as f:
    for full_name in iter_files(walk_path, file_type):
        f.write(full_name + '\n')
        print('success')
