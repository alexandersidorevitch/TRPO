from sqlite3 import *
from tkinter import font
from tkinter.ttk import *

from ttkthemes import ThemedTk


# Режим отображение таблиц
def polya(event):
    print(event.widget.get())
def cr(event):
    # print(event.widget.get())

    cursor.execute("SELECT * FROM " + event.widget.get())
    # print(*cursor.fetchall()[0].keys())
    listpolya = []
    for i in cursor.fetchall()[0].keys():
            print(i)
            listpolya.append(i)
    print(listpolya)



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = connect("TRPO.db")  # подлкючение к БД

conn.row_factory = dict_factory

cursor = conn.cursor()

root = ThemedTk()
root.set_theme('equilux')
print(font.families())
# s = Style()
# print(s.theme_names())
# s.theme_use('clam')
root.geometry("600x500+300+200")

frame = Frame(root)
frame.pack(side='left')

listtables = []
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in cursor.fetchall():
    if i['name'] != "sqlite_sequence":
        listtables.append(i['name'])
frame2 = Frame(root)
frame2.pack(side='right')
ComboTables = Combobox(frame2, values=[], height=10,state="disabled")
ComboTables.set(value="Поля")
ComboTables.bind('<<ComboboxSelected>>', polya)
ComboTables.pack(side="right")


ComboTables = Combobox(frame, values=listtables, height=10,state="readonly")
ComboTables.set(value = "Таблицы")
ComboTables.bind('<<ComboboxSelected>>',cr)
ComboTables.pack(side="left")
root.mainloop()
