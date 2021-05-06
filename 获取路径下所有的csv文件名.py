# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  获取路径下所有的csv文件名.py
# 日期时间：2021/4/16，13:17
import os

def get_all_csv_filenames_under_the_path(root_path):
    """
    获取路径下所有的csv文件名
    :param root_path: 传入文件夹路径信息
    :return: 返回包含所有csv文件的名称的列表和包含文件路径信息的列表
    """
    csv_filename_list = []
    csv_filepath_list = []
    for j in os.listdir(root_path):
        if os.path.splitext(j)[1] == '.csv':
            csv_filename_list.append(j)
            csv_filepath_list.append(os.path.join(root_path, j))
    return csv_filename_list, csv_filepath_list

root_path = '其他'
csv_filename_list, csv_filepath_list = get_all_csv_filenames_under_the_path(root_path)
print("csv_filename_list----------", csv_filename_list)
print("csv_filepath_list----------", csv_filepath_list)
