# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/29
from tkinter import *
import tkinter.messagebox


def showName():
    my_name = Entry.get(Entry1)
    tkinter.messagebox.showinfo("My name", my_name)


def changeName():
    Entry1.insert(0, "Sam")


root = Tk()
topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack()
myLabel = Label(topFrame, text="Enter your name:")
Entry1 = Entry(topFrame)

Listbox1 = Listbox(topFrame)
Button1 = Button(bottomFrame, text="Show name", fg="red", command=showName)
Button2 = Button(bottomFrame, text="Change name", fg="green", command=changeName)
myLabel.pack()
Entry1.pack()
Listbox1.pack()
Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Listbox1.insert(0, "Male")
Listbox1.insert(1, "Female")

root.mainloop()
