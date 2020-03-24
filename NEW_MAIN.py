from tkinter import *


def callback(event):
    print(event)
    print("Тарас конч")


def but(number: int):
    global buttons
    buttons[number]["bg"] = '#333333'

def butleave(number: int):
    global buttons
    buttons[number]["bg"] = '#222222'

def press(number: int):
    global buttons
    print(number)
    buttons[number]['text'] = str(number + 1)
root = Tk()
root.geometry("600x500+300+200")
listbox1 = Listbox(root, height=10, width=15, selectmode=EXTENDED, bg='#222222', highlightcolor='red', fg="#EEEEEE")
listbox2 = Listbox(root, height=5, width=15, selectmode=SINGLE)
button1 = Button(root, text='ok', width=25, height=5, bg='white', fg='red', font='arial 14')
buttons = []
q = root.grid()
for i in range(10):
    buttons.append(Button(text=str(i), width=10, height=2,bg='#222222',fg = '#EEEEEE',bd=0,activebackground='#333333',activeforeground='#EEEEEE',highlightcolor="black",relief=SUNKEN, command=lambda number = i: press(number)))
    buttons[i].grid(row = i,column = 1,columnspan=1,ipadx=103,ipady=3)
    buttons[i].bind("<Enter>", lambda event, number=i: but(number))
    buttons[i].bind("<Leave>", lambda event, number=i: butleave(number))
    # buttons[i].pack()
i =0

root.mainloop()
