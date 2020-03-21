from tkinter import *

root = Tk()
root.geometry("600x500+300+200")
listbox1 = Listbox(root, height=10, width=15, selectmode=EXTENDED,  bg = '#222222',highlightcolor = 'red',fg = "#EEEEEE")
listbox2 = Listbox(root, height=5, width=15, selectmode=SINGLE)
list1 = [u"Москва", u"Санкт-Петербург", u"Саратов", u"Омск"]
list2 = [u"Канберра", u"Сидней", u"Мельбурн", u"Аделаида"]
root.bind("Enter")
for i in list1:
    listbox1.insert(END, i)
for i in list2:
    listbox2.insert(END, i)
listbox1.pack()
listbox2.pack()
root.mainloop()
