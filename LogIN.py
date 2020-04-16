from sqlite3 import *
from tkinter import font, messagebox

import rsa

from ttkthemes import ThemedTk

from main import *


def proverka(all_data, el, name):
    for i in all_data:
        if el == i[name]:
            return True
    return False


def press():
    if not (login.get() or password.get()):
        messagebox.askretrycancel('Пустое поле', 'Не введен логин и пароль')
    elif not login.get():
        messagebox.askretrycancel('Пустое поле', 'Не введен логин')
    elif not password.get():
        messagebox.askretrycancel('Пустое поле', 'Не введен пароль')
    else:
        with open('privatekey', 'r') as private:
            priv_key = tuple(int(i) for i in private.readline().split(','))
        # Регистрация
        # with open('publickey', 'r') as public:
        #     pub_key = tuple(int(i) for i in public.readline().split(','))
        # introduced_password = rsa.encrypt(password.get().encode('utf8'), rsa.PublicKey(*pub_key))
        cursor.execute("SELECT USERNAME FROM users")
        all_data = cursor.fetchall()
        if not proverka(all_data, login.get(), 'USERNAME'):
            messagebox.showerror('Ошибка', 'Неправильно введен логин или пароль')
            # Регистрация
            # cursor.execute(
            #     "INSERT INTO `users` (`id`, `USERNAME`, `password`, `name`, `grup`) VALUES (NULL, %s, %s ,'sasha', 'p-1807')",
            #     (
            #         login.get(), introduced_password))
            # conn.commit()
        else:
            cursor.execute("SELECT password FROM users WHERE ? = USERNAME", (login.get(),))
            all_data = cursor.fetchall()[0]
            if password.get() == rsa.decrypt(all_data['password'], rsa.PrivateKey(*priv_key)).decode('utf-8'):
                root.withdraw()
                start()
                messagebox.showinfo('', 'Пароль верный')
            else:
                messagebox.showerror('Ошибка', 'Неправильно введен логин или пароль')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = connect('project_trpo')  # подлкючение к БД

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

fon = list(font.families())
fon = [fon[50], fon[88], fon[110]]
f = font.Font(family=fon[1], size=14)
registarion = Button(root, text="Не нажимать!", width=10, height=1, bg='#222222', fg='#EEEEEE', bd=0,
                     activebackground='#333333',
                     activeforeground='#EEEEEE', highlightcolor="black", relief=SUNKEN,
                     font=f, command=press).place(x=100, y=300)
root.bind("<Return>", lambda _: press())
root.grid()
root.mainloop()
