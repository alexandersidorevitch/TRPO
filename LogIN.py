from sqlite3 import *
from tkinter import font, messagebox

import rsa

import Registration
import main_window
from Visualition import *


class Login:
    def __init__(self):
        conn = connect('project_trpo')  # подлкючение к БД
        conn.row_factory = self.dict_factory
        self.cursor = conn.cursor()
        self.cursor.execute("SELECT USERNAME FROM users")
        self.logins = [i["USERNAME"] for i in self.cursor.fetchall()]
        LOGIN = Tk()
        LOGIN['bg'] = "#444444"
        LOGIN.resizable(False, False)
        LOGIN.geometry("600x500")
        LOGIN.iconbitmap('icon.ico')

        self.login = StringVar()
        self.log = Entry(LOGIN, textvariable=self.login, bg="#222222", fg="#FFFFFF", selectbackground="#444444",
                         selectforeground="#19C710", width=10, font=("@Microsoft YaHei UI Light", 16, "bold"))
        self.log.place(x=200, y=160)
        self.log.bind("<Any-KeyRelease>", self.check_login)
        fon = list(font.families())
        Label(LOGIN, text="Логин", fg="#FFFFFF", bg="#444444").place(x=200, y=134)
        Label(LOGIN, text="Пароль", fg="#FFFFFF", bg="#444444").place(x=200, y=198)
        self.password = StringVar()
        self.pas = Entry(LOGIN, textvariable=self.password, bg="#222222", fg="#FFFFFF", show="*",
                         selectbackground="#444444", selectforeground="#19C710", width=10,
                         font=("@Microsoft YaHei UI Light", 16, "bold"))
        self.pas.place(x=200, y=220)
        self.pas.bind("<Any-KeyRelease>", self.check_password)
        self.pas.bind("<Enter>", self.Enter)
        self.pas.bind("<Leave>", self.Leave)

        self.LOGIN = LOGIN

        f = font.Font(family="@Microsoft YaHei UI Light", size=14)
        kwargs = dict(text="Вход", width=12, height=1, bg='#222222', fg='#EEEEEE', bd=0,
                      activebackground='#333333',
                      activeforeground='#EEEEEE', highlightcolor="black", relief=SUNKEN,
                      font=f, command=self.press)
        w = Button(LOGIN, **kwargs)
        w.place(x=200, y=270)
        kwargs["text"] = "Регистрация"
        kwargs['bg'] = '#7CD5CB'
        kwargs['fg'] = '#000000'
        kwargs["command"] = self.press_registration
        Button(LOGIN, **kwargs).place(x=200, y=320)

        LOGIN.bind("<Return>", lambda _: self.press())
        # LOGIN.grid()
        LOGIN.mainloop()

    def proverka(self, all_data, el, name):
        for i in all_data:
            if el == i[name]:
                return True
        return False

    def Enter(self, event):
        self.pas['show'] = ""

    def Leave(self, event):
        self.pas['show'] = "*"

    def press_registration(self):
        self.LOGIN.destroy()
        Registration.Registration()

    def press(self):
        if not (self.login.get() or self.password.get()):
            messagebox.askretrycancel('Пустое поле', 'Не введен логин и пароль')
        elif not self.login.get():
            messagebox.askretrycancel('Пустое поле', 'Не введен логин')
        elif not self.password.get():
            messagebox.askretrycancel('Пустое поле', 'Не введен пароль')
        else:
            with open('privatekey', 'r') as private:
                priv_key = tuple(int(i) for i in private.readline().split(','))
            self.cursor.execute("SELECT USERNAME FROM users")
            all_data = self.cursor.fetchall()
            if not self.proverka(all_data, self.login.get(), 'USERNAME'):
                messagebox.showerror('Ошибка', 'Неправильно введен логин или пароль')
            else:
                self.cursor.execute("SELECT password FROM users WHERE ? = USERNAME", (self.login.get(),))
                all_data = self.cursor.fetchone()
                if self.password.get() == rsa.decrypt(all_data['password'], rsa.PrivateKey(*priv_key)).decode('utf-8'):
                    self.LOGIN.destroy()
                    self.cursor.execute("SELECT theme FROM Users WHERE ? = USERNAME", (self.login.get(),))
                    main_window.main_window(self.cursor.fetchone()['theme'], self.login.get())

                else:
                    messagebox.showerror('Ошибка', 'Неправильно введен логин или пароль')

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def check_login(self, event):
        pattern = r"[^-_\s][\w_-]{3,18}\b"

        if re.fullmatch(pattern, self.login.get(), re.I):
            self.log['fg'] = '#19C710'
        elif not self.login.get():
            self.log['fg'] = '#222222'
        else:
            self.log['fg'] = '#FF002F'

    def check_password(self, event):
        pattern = r"(?=.*[A-ZА-Я])(?=.*[0-9].*[0-9])(?=.*[a-zа-я].*[a-zа-я].*[a-zа-я]).{8,}"

        if re.fullmatch(pattern, self.password.get()):
            self.pas['fg'] = '#19C710'
        elif not self.password.get():
            self.pas['fg'] = '#222222'
        else:
            self.pas['fg'] = '#FF002F'


if __name__ == "__main__":
    l = Login()
