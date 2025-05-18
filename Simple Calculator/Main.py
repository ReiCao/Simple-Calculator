from tkinter import *
from tkinter import ttk

#Creates and Formats the Window
root = Tk()
root.title('Calculator')
root.resizable(False, False)


#Simp Calc Commands
comm = 0     #Tells what the operation is (1=mult, 2=divided, 3=minus, 4=plus)
first_n = 0  

def PutNum(number):
    num1 = Display.get()
    Display.delete(0, END)
    Display.insert(0, str(num1) + str(number))
    return

def addition():
    num1 = Display.get()
    global first_n
    first_n = float(num1)
    global comm
    comm = 4
    Display.delete(0, END)
    return

def subtraction():
    num1 = Display.get()
    global first_n
    first_n = float(num1)
    global comm
    comm = 3
    Display.delete(0, END)
    return

def division():
    num1 = Display.get()
    global first_n
    first_n = float(num1)
    global comm
    comm = 2
    Display.delete(0, END)
    return

def multiplication():
    num1 = Display.get()
    global first_n
    first_n = float(num1)
    global comm
    comm = 1
    Display.delete(0, END)
    return

def SimpCalcExec():
    num2 = Display.get()
    Display.delete(0, END)
    if comm == 1:
        Display.insert(0, float(first_n) * float(num2))
    elif comm == 2:
        Display.insert(0, float(first_n) / float(num2))
    elif comm == 3:
        Display.insert(0, float(first_n) - float(num2))
    elif comm == 4:
        Display.insert(0, float(first_n) + float(num2))
    return

def SimpCalcClear():
    Display.delete(0, END)
    return


#Simple Calculator Hud

Display = Entry(root, width=21, font=(24))
Display.grid(row=0, column=0 ,columnspan=4, sticky='nsew')
clear = Button(root, text="clear", command=SimpCalcClear).grid(row=1, column=0,columnspan=4, sticky='nsew')
B1 = Button(root, text="1", command=lambda: PutNum(1)).grid(row=4, column=0, sticky='nsew')
B2 = Button(root, text="2", command=lambda: PutNum(2)).grid(row=4, column=1, sticky='nsew')
B3 = Button(root, text="3", command=lambda: PutNum(3)).grid(row=4, column=2, sticky='nsew')
B4 = Button(root, text="4", command=lambda: PutNum(4)).grid(row=3, column=0, sticky='nsew')
B5 = Button(root, text="5", command=lambda: PutNum(5)).grid(row=3, column=1, sticky='nsew')
B6 = Button(root, text="6", command=lambda: PutNum(6)).grid(row=3, column=2, sticky='nsew')
B7 = Button(root, text="7", command=lambda: PutNum(7)).grid(row=2, column=0, sticky='nsew')
B8 = Button(root, text="8", command=lambda: PutNum(8)).grid(row=2, column=1, sticky='nsew')
B9 = Button(root, text="9", command=lambda: PutNum(9)).grid(row=2, column=2, sticky='nsew')
B0 = Button(root, text="0", command=lambda: PutNum(0)).grid(row=5, column=0, sticky='nsew')
Bplus = Button(root, text="+", command=addition).grid(row=5, column=3, sticky='nsew')
Bminus = Button(root, text="-", command=subtraction).grid(row=4, column=3, sticky='nsew')
Bdivide = Button(root, text="/", command=division).grid(row=3, column=3, sticky='nsew')
Bmult = Button(root, text="*", command=multiplication).grid(row=2, column=3, sticky='nsew')
Bequal = Button(root, text="=", command=SimpCalcExec).grid(row=5, column=1, columnspan=2, sticky='nsew')

mainloop()