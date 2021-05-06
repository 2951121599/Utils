# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  生成日历.py
# 日期时间：2020/9/30，17:43
import calendar

year = int(input("输入年份:"))
month = int(input("输入月份:"))

# 显示日历
print(calendar.month(year, month))
