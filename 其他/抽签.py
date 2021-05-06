# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  抽签.py
# 日期时间：2020/10/27，16:24
import tkinter
import time
import threading  # 用于提供线程相关的操作，线程是应用程序中工作的最小单元。

# from PIL import Image


root = tkinter.Tk()
root.title('下一个谁讲')
root.minsize(450, 350)

btn1 = tkinter.Button(text='姚志立', bg='red')
btn1.place(x=20, y=20, width=50, height=50)

btn2 = tkinter.Button(text='于涛', bg='white')
btn2.place(x=90, y=20, width=50, height=50)

btn3 = tkinter.Button(text='李世楠', bg='white')
btn3.place(x=160, y=20, width=50, height=50)

btn4 = tkinter.Button(text='罗豆豆', bg='white')
btn4.place(x=230, y=20, width=50, height=50)

btn5 = tkinter.Button(text='刘宇', bg='white')

btn5.place(x=230, y=90, width=50, height=50)
btn6 = tkinter.Button(text='于涛', bg='white')
btn6.place(x=230, y=160, width=50, height=50)

btn7 = tkinter.Button(text='李思楠', bg='white')
btn7.place(x=230, y=230, width=50, height=50)

btn8 = tkinter.Button(text='罗豆豆', bg='white')
btn8.place(x=160, y=230, width=50, height=50)

btn9 = tkinter.Button(text='刘宇', bg='white')
btn9.place(x=90, y=230, width=50, height=50)

btn10 = tkinter.Button(text='于涛', bg='white')
btn10.place(x=20, y=230, width=50, height=50)

btn11 = tkinter.Button(text='李世楠', bg='white')
btn11.place(x=20, y=160, width=50, height=50)

btn12 = tkinter.Button(text='刘宇', bg='white')
btn12.place(x=20, y=90, width=50, height=50)
'''button_img_gif = Tkinter.PhotoImage(file = 'button_gif.gif')
button_img = Tkinter.Button(root, image = button_img_gif, text = '带图按钮')
button_img.pack()   #没能实现，不知道为什么，是个坑
'''

new = tkinter.Label(text="来看看在我后面哪个讲", bg='white')
new.place(x=300, y=20, width=150, height=50)

# 将所有选项组成列表
carlist = [btn1, btn2, btn3, btn4, btn5, btn6, btn6, btn7, btn8, btn9, btn10, btn11, btn12]
# 是否开始循环的标志
isloop = False


def round():
    # 判断是否开始循环
    if isloop == True:
        return  # 结束函数的执行，从函数返回
    # 初始化计数   变量
    i = 0
    # 死循环
    while True:
        time.sleep(0.001)
        # 将所有的组件背景变为白色
        for x in carlist:
            x['bg'] = 'white'
            # 将当前数值对应的组件变色
            carlist[i]['bg'] = 'red'
        # 变量+1
        i += 1
        # 如果i大于最大索引直接归零

        if i >= len(carlist):
            i = 0
        if functions == True:
            neww = tkinter.Label(text="  ", bg='white')
            neww.place(x=300, y=100, width=150, height=50)
            continue
        else:
            neww = tkinter.Label(text="4-2", bg='white')
            neww.place(x=300, y=100, width=150, height=50)
            break


# 建立一个新线程的函数。
def newtask():
    global isloop  # 全局函数定义
    global functions
    # 建立新线程
    t = threading.Thread(target=round)  # 给函数传递回调对象
    # 开启线程运行
    t.start()
    # 设置程序开始标志
    isloop = True
    # 是否运行的标志
    functions = True


# 定义停止循环的函数
def stop():
    global isloop
    global functions
    functions = False
    isloop = False


# 开始按钮
btn_start = tkinter.Button(root, text='start', command=newtask, bg='pink')
btn_start.place(x=90, y=120, width=50, height=50)

btn_stop = tkinter.Button(root, text='stop', command=stop, bg='green')
btn_stop.place(x=160, y=120, width=50, height=50)

root.mainloop()