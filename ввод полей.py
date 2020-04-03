from pymysql import *
from tkinter import font
from tkinter.ttk import *
import pyAesCrypt as  crypt
from ttkthemes import ThemedTk


# Режим отображение таблиц
def polya(event):
    print(event.widget.get())
def cr(event):
    # print(event.widget.get())

    cursor.execute("SHOW COLUMNS FROM " + event.widget.get())
    # print(*cursor.fetchall()[0].keys())
    listpolya = []
    all = cursor.fetchall()
    if len(all):
        for i in all:
                print(i)
                listpolya.append(i[0])
        ComboPolya['values'] = listpolya
        ComboPolya['state'] = 'readonly'
    else:
        ComboPolya['values'] = []
        ComboPolya['state'] = 'disabled'
    print(listpolya)



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = connect('localhost','root','root','project_trpo')  # подлкючение к БД

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
cursor.execute("SHOW TABLES")
for i in cursor.fetchall():
        listtables.append(i[0])
frame2 = Frame(root)
frame2.pack(side='right')
ComboPolya = Combobox(frame2, values=[], height=10,state="disabled")
ComboPolya.set(value="Поля")
ComboPolya.bind('<<ComboboxSelected>>', polya)
ComboPolya.pack(side="right")


ComboTables = Combobox(frame, values=listtables, height=10,state="readonly")
ComboTables.set(value = "Таблицы")
ComboTables.bind('<<ComboboxSelected>>',cr)
ComboTables.pack(side="left")
root.mainloop()
# for kof in range(1, 10):
#     for x in range(10, 100):
#         for y in range(10, 100):
#             if (kof * x * y == 100 * x + y):
#                 print(kof, x, y)
