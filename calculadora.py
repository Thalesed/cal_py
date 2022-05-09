from tkinter import *

#screen.geometry('600x600')
equal = ''


screen = Tk()
screen.title('My programm')
screen.iconbitmap('cal.ico')

box = Entry(screen, width=50, borderwidth=5)
box.grid(row=0, column=0, columnspan=4)

try:
    aleatorio = x +1
except:
    x = 0


def button_click(number):
    if box.get() == 'error':
        box.delete(0, END)
    num = box.get()
    box.delete(0, END)
    box.insert(0, str(num) + str(number))

def button_oper(oper):
    global num1
    global equal
    num1 = box.get()
    box.delete(0, END)
    equal = oper

def finish():
    global x
    global num2
    x = 1
    num2 = box.get()
    box.delete(0, END)
    answ = 'error'

    if equal == '+':
        try:
            answ = float(num1) + float(num2)
        except:
            answ = 'error'
    elif equal == '-':
        try:
            answ = float(num1) - float(num2)
        except:
            answ = 'error'
    elif equal == '*':
        try:
            answ = float(num1) * float(num2)
        except:
            answ = 'error'
    elif equal == '/':
        try:
            answ = float(num1) / float(num2)
        except:
            answ = 'error'
    elif equal == '**':
        try:
            answ = float(num1) ** float(num2)
        except:
            answ = 'error'
    elif equal == '√':
        try:
            answ = float(num2) ** (1 / float( num1))
        except:
            answ = 'error'


    box.insert(0, str(answ))


def clear():
    box.delete(0, END)
    num1 = ''
def mine():
    value = box.get()
    box.delete(0, END)
    newvalue = -1 * float(value)
    box.insert(0, str(newvalue))


button_9 = Button(screen, text='9',borderwidth=5,padx=30, pady=20, command=lambda: button_click(9))
button_8 = Button(screen, text='8',borderwidth=5,padx=30, pady=20, command=lambda:button_click(8))
button_7 = Button(screen, text='7',borderwidth=5,padx=30, pady=20, command=lambda:button_click(7))
button_6 = Button(screen, text='6',borderwidth=5,padx=30, pady=20, command=lambda:button_click(6))
button_5 = Button(screen, text='5',borderwidth=5,padx=30, pady=20, command=lambda:button_click(5))
button_4 = Button(screen, text='4',borderwidth=5,padx=30, pady=20, command=lambda:button_click(4))
button_3 = Button(screen, text='3',borderwidth=5,padx=30, pady=20, command=lambda:button_click(3))
button_2 = Button(screen, text='2',borderwidth=5,padx=30, pady=20, command=lambda:button_click(2))
button_1 = Button(screen, text='1',borderwidth=5,padx=30, pady=20, command=lambda:button_click(1))
button_0 = Button(screen, text='0',borderwidth=5, padx=30, pady=20, command=lambda:button_click(0))

button_add = Button(screen, text='+', borderwidth=5, padx=30, pady=20, command=lambda:button_oper('+'))
button_sub = Button(screen, text='-', borderwidth=5, padx=30, pady=20, command=lambda:button_oper('-'))
button_mut = Button(screen, text='x', borderwidth=5, padx=30, pady=20, command=lambda:button_oper('*'))
button_div = Button(screen, text='/', borderwidth=5, padx=30, pady=20, command=lambda:button_oper('/'))
button_equal = Button(screen, text='=', borderwidth=5, padx=30, pady=20, command=finish)
button_clear = Button(screen, text='clear', borderwidth=5, padx=20, pady=55, command=clear)
button_pow = Button(screen, text='^', borderwidth=5, padx=30, pady=20, command=lambda:button_oper('**'))
button_sqrt = Button(screen, text='√', borderwidth=5, padx=30, pady=20, command=lambda:button_oper('√'))
button_change = Button(screen, text='+/-', borderwidth=5, padx=25, pady=20, command=mine)

button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_mut.grid(row=5, column=1)
button_div.grid(row=5, column=2)
button_equal.grid(row=5, column=0)
button_0.grid(row=4, column=0)
button_clear.grid(row=1, column=3, rowspan=2)
button_pow.grid(row=4, column=3)
button_sqrt.grid(row=5, column=3)
button_change.grid(row=3, column=3)

button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)
button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)
button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

screen.mainloop()
