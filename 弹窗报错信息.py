# -*-coding:utf-8-*- 
# ���ߣ�   29511
# �ļ���:  ����.py
# ����ʱ�䣺2021/3/5��10:17
from tkinter import Tk
from tkinter import messagebox

try:
    with open("abnormal.txt") as f:
        print("over")

except Exception as e:
    print(e)
    root = Tk()
    root.withdraw()  # ʵ������������
    messagebox.showerror("Error", "Error Message:\n%s" % e)  # ��ʾ����


    # messagebox.showinfo("Alert", e)
    # messagebox.askyesnocancel("askyesnocancel", "Error Message:\n%s" % e)
    # messagebox.showinfo("showinfo", "Error Message:\n%s" % e)
    # messagebox.showwarning("showwarning", "Error Message:\n%s" % e)
    # messagebox.showerror("Error", "Error Message:\n%s" % e)
    # messagebox.askquestion("askquestion", "Error Message:\n%s" % e)
    # messagebox.askokcancel("askokcancel", "Error Message:\n%s" % e)

