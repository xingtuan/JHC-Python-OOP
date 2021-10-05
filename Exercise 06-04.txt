# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/29
from tkinter import *

root = Tk()
root.geometry("200x170")
root.title("calculator")
# Global variables
# <Make a variable called num1 and make it equal to 0>
num1 = 0
# <Make a variable called num1 and make it equal to 0>
num2 = 0
# <Make a variable called operator and make it equal to ''>
operator = ''
reset = False


# Put the number of the button into the text box
def insertText(num):
    global reset
    if reset:
        myEntry.delete(0, END)
    else:
        reset = False
    # <Make a variable called typedNum and make it equal to the value in myEntry plus num>
    typedNum = Entry.get(myEntry) + num
    myEntry.delete(0, END)  # Delete the value in the text box
    myEntry.insert(0, typedNum)  # Put the new value in the text box


# Set the operator and clear the text box
def makeOperator(op):
    global num1  # We need to use the global variables
    global operator
    #     <Make num1 equal to the value in the text box cast to an int>
    num1 = int(Entry.get(myEntry))
    # <Make operator equal to op>
    operator = op
    # <Delete the value inside the text box>
    myEntry.delete(0, END)


# Calculate the answer and put it in the text box
def calculateAnswer():
    global reset, num2  # We need to use the global variable
    # <Make num2 equal to the value in the text box cast to an int>
    num2 = int(Entry.get(myEntry))
    answer = 0
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        if num1 == 0 or num2 == 0:
            answer = "ERROR!"
        else:
            answer = num1 / num2
    # <finish this if statement for -, * and /   >
    myEntry.delete(0, END)  # <Delete the value inside the text box>
    myEntry.insert(0, answer)  # <Put the answer into the text box>
    reset = True


def factorial():
    global reset, num2
    num2 = round(float(Entry.get(myEntry)))
    answer = num2
    while num2 > 1:
        answer = answer * (num2 - 1)
        num2 -= 1
    myEntry.delete(0, END)  # <Delete the value inside the text box>
    myEntry.insert(0, answer)  # <Put the answer into the text box>
    reset = True


def resetAll():
    global num1, num2, myEntry, operator, reset
    num1 = 0
    num2 = 0
    reset = False
    operator = ''
    myEntry.delete(0, END)


# Make the frames
topFrame = Frame(root)
topFrame.pack()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack()
frame5 = Frame(root)
frame5.pack()
frame6 = Frame(root)
frame6.pack(side=BOTTOM)

# Make the text box
myEntry = Entry(frame1, justify=RIGHT)
myEntry.pack()

# Make the buttons
button1 = Button(frame2, text="1", command=lambda: insertText('1'))
button2 = Button(frame2, text="2", command=lambda: insertText('2'))
button3 = Button(frame2, text="3", command=lambda: insertText('3'))
buttonPlus = Button(frame2, text="+", command=lambda: makeOperator('+'))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
buttonPlus.pack(side=LEFT)

# <Make button 4,5,6 and – and put them into frame3>
button4 = Button(frame3, text="4", command=lambda: insertText('4'))
button5 = Button(frame3, text="5", command=lambda: insertText('5'))
button6 = Button(frame3, text="6", command=lambda: insertText('6'))
buttonMinus = Button(frame3, text="-", command=lambda: makeOperator('-'))

button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
buttonMinus.pack(side=LEFT)

# <Make button 7,8,9 and * and put them into frame4>
button7 = Button(frame4, text="7", command=lambda: insertText('7'))
button8 = Button(frame4, text="8", command=lambda: insertText('8'))
button9 = Button(frame4, text="9", command=lambda: insertText('9'))
buttonMultiply = Button(frame4, text="*", command=lambda: makeOperator('*'))

button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)
buttonMultiply.pack(side=LEFT)

button0 = Button(frame5, text="0", command=lambda: insertText('0'))
buttonEquals = Button(frame5, text="=", width=4, command=lambda: calculateAnswer())
buttonDivide = Button(frame5, text="/", command=lambda: makeOperator('/'))

button0.pack(side=LEFT)
buttonEquals.pack(side=LEFT)
buttonDivide.pack(side=LEFT)

buttonFactorial = Button(frame6, text="x!", command=lambda: factorial())
buttonRestAll = Button(frame6, text="Rest All", command=lambda: resetAll())
buttonFactorial.pack(side=RIGHT)
buttonRestAll.pack(side=LEFT)
root.mainloop()
