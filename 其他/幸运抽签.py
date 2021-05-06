import random
import time
from tkinter import *
import threading
from tkinter import messagebox as msgbox

root = Tk()

list_candidate = ["1-1", "1-2", "1-3", "1-4", "1-5", "1-6", "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "3-1", "3-2",
                  "3-3", "3-4", "3-5", "3-6", "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "5-1", "5-2", "5-3", "5-4",
                  "5-5", "5-6", "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "7-1", "7-2", "7-3", "7-4", "7-5", "7-6",
                  "8-1", "8-2", "8-3", "8-4", "8-5", "8-6", "9-1", "9-2", "9-3", "9-4", "9-5", "9-6", ]


class lottery():
    def __init__(self):
        self.root = root
        self.msgbox = msgbox
        self.root.geometry("800x600+480+220")
        self.root.title("抽签小程序")
        self.button_start = Button(self.root, text="开始抽签", width=12, command=self.start)
        self.button_stop = Button(self.root, text="结束抽签", width=12, command=self.stop)
        self.label_str = StringVar()
        self.label_str.set("抽签马上开始了")
        self.label_winner = Label(self.root, font=("华文行楷", 20), width=20, height=30, fg="red",
                                  textvariable=self.label_str)
        self.label_winner.pack()

        self.button_start.place(relx=0.2, rely=0.7)
        self.button_stop.place(relx=0.7, rely=0.7)

        self.ready = 0

        self.root.mainloop()

    def draw(self):
        global list_candidate
        self.label_str.set(list_candidate)
        while self.ready:
            index_num = random.randint(1, 1000) % len(list_candidate)
            # print(index_num)
            winner = list_candidate[index_num]
            self.label_str.set(winner)
        self.label_str.set('4-2')
        self.msgbox.showinfo("中奖信息", "恭喜" + '4-2' + "，您中奖啦！")

    def start(self):
        self.ready = 1
        # 此处必须启用新的线程，否则会卡死在开始按钮，且标签的中奖人信息不会刷新
        self.thread = threading.Thread(target=self.draw, args=())
        self.thread.setDaemon(True)
        self.thread.start()

    def stop(self):
        global winner
        self.ready = 0


if __name__ == '__main__':
    Lottery = lottery()
