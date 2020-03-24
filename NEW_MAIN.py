from tkinter import *


def callback(event):
    print(event)
    print("Тарас конч")


def but(number: int):
    global buttons
    buttons[number]["bg"] = 'black'

def butleave(number: int):
    global buttons
    buttons[number]["bg"] = 'white'


root = Tk()
root.geometry("600x500+300+200")
listbox1 = Listbox(root, height=10, width=15, selectmode=EXTENDED, bg='#222222', highlightcolor='red', fg="#EEEEEE")
listbox2 = Listbox(root, height=5, width=15, selectmode=SINGLE)
button1 = Button(root, text='ok', width=25, height=5, bg='white', fg='red', font='arial 14')
buttons = []
for i in range(5):
    buttons.append(Button(text=str(i), width=10, height=4,bg='white',))
    buttons[i].bind("<Enter>", lambda event, number=i: but(number))
    buttons[i].bind("<Leave>", lambda event, number=i: butleave(number))
    buttons[i].pack()

list1 = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]
list2 = ["Канберра", "Сидней", "Мельбурн", "Аделаида"]
for i in list1:
    listbox1.insert(END, i)
for i in list2:
    listbox2.insert(END, i)
listbox1.bind("<Enter>", callback)
listbox1.pack()
listbox2.pack()
root.mainloop()
