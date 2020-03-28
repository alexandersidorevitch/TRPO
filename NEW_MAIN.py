from tkinter import *
from tkinter import font

from ttkthemes import ThemedTk


def callback(event):
    print(event)
    print("Тарас конч")


def but(number: int):
    global buttons
    buttons[number]["bg"] = '#333333'


def butleave(number: int):
    global buttons
    buttons[number]["bg"] = '#222222'


def pow(number, n):
    otvet = 1
    for i in range(n):
        otvet *= number
    return otvet
def gandon(but):
    but += 2

def press(number: int):
    global buttons
    buttons[number]['text'] = 'Privet'


root = ThemedTk()
root.set_theme('breeze')
root.geometry("600x500+300+200")
buttons = []
q = root.grid()
fon = list(font.families())
fon = [fon[50], fon[88], fon[110]]
for i in range(9):
    f = font.Font(family=fon[1], size=14)
    buttons.append(
        Button(text=str('Стелла'), width=10, height=1, bg='#222222', fg='#EEEEEE', bd=0, activebackground='#333333',
               activeforeground='#EEEEEE', highlightcolor="black", relief=SUNKEN, wraplength=200,
               font=f, command=lambda number=i: press(number)))
    buttons[i].grid(row=i, column=1, columnspan=1, ipadx=103, ipady=3)
    buttons[i].bind("<Enter>", lambda event, number=i: but(number))
    buttons[i].bind("<Leave>", lambda event, number=i: butleave(number))
    # buttons[i].pack()
i = 0
a = 5
a = gandon(a)
print(a)
root.mainloop()
