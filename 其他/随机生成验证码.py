# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  随机生成验证码.py
# 日期时间：2020/9/30，17:54
import random
import string

str1 = '0123456789'
str2 = string.ascii_letters  # 所有英文字母大小写
str3 = str1 + str2

print(''.join(random.sample(str3, 4)))
