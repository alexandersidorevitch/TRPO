from sqlite3 import *
from tkinter import font
from tkinter.ttk import *

from ttkthemes import ThemedTk


# Режим отображение таблиц
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
frame.grid()

listtables = []
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for i in cursor.fetchall():
    if i['name'] != "sqlite_sequence":
        listtables.append(i['name'])
ComboTables = Combobox(frame, values=listtables, height=10)
Combobox.set(root,)
ComboTables.pack(side="left")
root.mainloop()
