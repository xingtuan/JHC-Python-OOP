# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/29
from tkinter import *


def calcC():
    user_input = float(Entry.get(Entry1))
    new_temp = (user_input - 32) / 1.8
    myLabel.config(text=str(new_temp))


def calcF():
    user_input = float(Entry.get(Entry1))
    new_temp = user_input * 1.8 + 32
    myLabel.config(text=str(new_temp))


root = Tk()
root.geometry("200x80")
topFrame = Frame(root)
topFrame.pack()
Entry1 = Entry(topFrame)
myLabel = Label(topFrame, text="")
Button1 = Button(root, text="Celsius", fg="red", command=calcC)
Button2 = Button(root, text="Fahrenheit", fg="green", command=calcF)
Entry1.pack()
myLabel.pack()
Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
root.mainloop()
