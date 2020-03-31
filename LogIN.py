from tkinter import *
from tkinter import font, messagebox

import rsa
from pymysql import *
from ttkthemes import ThemedTk


def proverka(all_data, el, name):
    for i in all_data:
        if el == i[name]:
            return True
    return False


def press():
    if not (log.get() or pas.get()):
        messagebox.askretrycancel('Пустое поле', 'Не введен логин и пароль')
    elif not log.get():
        messagebox.askretrycancel('Пустое поле', 'Не введен логин')
    elif not pas.get():
        messagebox.askretrycancel('Пустое поле', 'Не введен пароль')
    else:
        with open('privatekey', 'r') as private:
            priv_key = tuple(int(i) for i in private.readline().split(','))
        # Регистрация
        # with open('publickey', 'r') as public:
        #     pub_key = tuple(int(i) for i in public.readline().split(','))
        # introduced_password = rsa.encrypt(pas.get().encode('utf8'), rsa.PublicKey(*pub_key))
        cursor.execute("SELECT USERNAME FROM users")
        all_data = cursor.fetchall()
        if not proverka(all_data, log.get(), 'USERNAME'):
            messagebox.showerror('Ошибка', 'Неправильно введен логин или пароль')
            # Регистрация
            # cursor.execute(
            #     "INSERT INTO `users` (`id`, `USERNAME`, `password`, `name`, `grup`) VALUES (NULL, %s, %s ,'sasha', 'p-1807')",
            #     (
            #         log.get(), introduced_password))
            # conn.commit()
        else:
            cursor.execute("SELECT password FROM users WHERE '" + str(log.get()) + "' = USERNAME")
            all_data = cursor.fetchall()[0]
            if pas.get() == rsa.decrypt(all_data['password'], rsa.PrivateKey(*priv_key)).decode('utf-8'):
                messagebox.showinfo('','Пароль верный')
            else:
                messagebox.showerror('Ошибка', 'Неправильно введен логин или пароль')


conn = connect('localhost', 'root', 'root', 'project_trpo', cursorclass=cursors.DictCursor)  # подлкючение к БД
cursor = conn.cursor()
root = ThemedTk()
root.set_theme('breeze')
root.resizable(False, False)
root.geometry("600x500")
log = StringVar()
login = Entry(root, textvariable=log).place(x=100, y=100)
pas = StringVar()
password = Entry(root, textvariable=pas).place(x=300, y=100)
fon = list(font.families())
fon = [fon[50], fon[88], fon[110]]
f = font.Font(family=fon[1], size=14)
registarion = Button(root, text="Не нажимать!", width=10, height=1, bg='#222222', fg='#EEEEEE', bd=0,
                     activebackground='#333333',
                     activeforeground='#EEEEEE', highlightcolor="black", relief=SUNKEN, wraplength=200,
                     font=f, command=press).place(x=100, y=200)
root.grid()
root.mainloop()
