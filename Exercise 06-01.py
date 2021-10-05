# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/29
from tkinter import *

root = Tk()
root.geometry('300x80')
topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack()
myLabel = Label(topFrame, text="Do not click the OK button!", fg="red")
Label1 = Label(topFrame, text=" ")
Button1 = Button(bottomFrame, text="OK", fg="green")
Button2 = Button(bottomFrame, text="Cancel", fg="blue")
myLabel.pack()
Label1.pack(side=LEFT)
Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
root.mainloop()
