from tkinter import *
from tkinter import font, messagebox

import rsa
from sqlite3 import *
from ttkthemes import ThemedTk


def proverka(all_data, el, name):
    for i in all_data:
        if el == i[name]:
            return True
    return False


def press():
    if not (login.get() and password.get() and name.get() and gruop.get()):
        messagebox.askretrycancel('Пустое поле', 'Введите данные')
    else:
        # Регистрация
        with open('publickey', 'r') as public:
            pub_key = tuple(int(i) for i in public.readline().split(','))
        introduced_passwords = rsa.encrypt(password.get().encode('utf8'), rsa.PublicKey(*pub_key))
        cursor.execute("SELECT USERNAME FROM users")
        all_data = cursor.fetchall()
        if not proverka(all_data, login.get(), 'USERNAME'):
            # Регистрация
            cursor.execute(
                "INSERT INTO `users` (`id`, `USERNAME`, `password`, `name`, `grup`) VALUES (NULL, ?, ? ,?, ?)",
                (
                    login.get(), introduced_passwords, name.get(), gruop.get()))
            conn.commit()
            messagebox.showinfo('Готово', 'Пользователь создан')
        else:
            messagebox.showerror('Ошибка', 'Пользователь уже существует')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = connect('C://MAMP//db//sqllite//project_trpo')  # подлкючение к БД

conn.row_factory = dict_factory
cursor = conn.cursor()

root = ThemedTk()
root.set_theme('breeze')
root.resizable(False, False)
root.geometry("600x500")

login = StringVar()
Entry(root, textvariable=login).place(x=100, y=100)

password = StringVar()
Entry(root, textvariable=password).place(x=100, y=130)

name = StringVar()
Entry(root, textvariable=name).place(x=100, y=160)

gruop = StringVar()
Entry(root, textvariable=gruop).place(x=100, y=190)

fon = list(font.families())
fon = [fon[50], fon[88], fon[110]]
f = font.Font(family=fon[1], size=14)
Button(root, text="Не нажимать!", width=10, height=1, bg='#222222', fg='#EEEEEE', bd=0,
       activebackground='#333333',
       activeforeground='#EEEEEE', highlightcolor="black", relief=SUNKEN,
       font=f, command=press).place(x=100, y=250)
root.bind("<Return>", lambda _: press())
root.grid()
root.mainloop()
