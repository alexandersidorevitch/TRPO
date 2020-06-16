from sqlite3 import *
from tkinter import *
from tkinter import font, messagebox

import rsa

import LogIN


class Registration:
    def __init__(self):
        self.conn = connect('project_trpo')  # подлкючение к БД
        x = 500 // 2 - 30
        height = 70
        interval = 60
        self.REGISTRATION = Tk()
        self.REGISTRATION['bg'] = "#444444"
        self.REGISTRATION.resizable(False, False)
        self.REGISTRATION.geometry("600x500")
        self.REGISTRATION.iconbitmap('icon.ico')
        self.conn.row_factory = self.dict_factory
        self.label = Label(self.REGISTRATION, text="", fg="#FF002F", bg="#444444",
                           font=font.Font(slant=font.ROMAN, size=10))
        self.label.place(x=x - 130, y=height + interval * 2 + 22)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT USERNAME FROM users")
        self.logins = {i["USERNAME"] for i in self.cursor.fetchall()}

        Label(self.REGISTRATION, text="Логин", fg="#FFFFFF", bg="#444444").place(x=x, y=height + interval * 2)
        self.login = StringVar()
        self.ButLog = Entry(self.REGISTRATION, textvariable=self.login, bg="#222222", fg="#FFFFFF",
                            selectbackground="#444444", selectforeground="#19C710",width=13,font=("@Microsoft YaHei UI Light", 16))
        self.ButLog.place(x=x, y=height + interval * 2 + 22)
        self.ButLog.focus_set()
        self.ButLog.bind("<Any-KeyRelease>", lambda event: (self.check_login(), self.check_texts()))

        Label(self.REGISTRATION, text="Пароль", fg="#FFFFFF", bg="#444444").place(x=x, y=height + interval * 3)
        self.password = StringVar()
        self.pas = Entry(self.REGISTRATION, textvariable=self.password, show='*', bg="#222222", fg="#FFFFFF",
                         selectbackground="#444444", selectforeground="#19C710",width=13,font=("@Microsoft YaHei UI Light", 16))
        self.pas.place(x=x, y=height + interval * 3 + 22)
        self.pas.bind("<Any-KeyRelease>", lambda event: (self.check_password(), self.check_texts()))

        Label(self.REGISTRATION, text="Повторите пароль", fg="#FFFFFF", bg="#444444").place(x=x,
                                                                                            y=height + interval * 4)
        self.second_password = StringVar()
        self.sec_pas = Entry(self.REGISTRATION, textvariable=self.second_password, show='*', bg="#222222", fg="#FFFFFF",
                             selectbackground="#444444", selectforeground="#19C710",width=13,font=("@Microsoft YaHei UI Light", 16))
        self.sec_pas.place(x=x, y=height + interval * 4 + 22)
        self.sec_pas.bind("<Any-KeyRelease>", lambda event: (self.check_second_password(), self.check_texts()))

        Label(self.REGISTRATION, text="Ваше имя", fg="#FFFFFF", bg="#444444").place(x=x, y=height + interval * 0)
        self.name = StringVar()
        self.name_Entry = Entry(self.REGISTRATION, textvariable=self.name, bg="#222222", fg="#FFFFFF",
                                selectbackground="#444444", selectforeground="#19C710",width=13,font=("@Microsoft YaHei UI Light", 16))
        self.name_Entry.place(x=x, y=height + interval * 0 + 22)
        self.name_Entry.bind("<Any-KeyRelease>", lambda event: (self.check_name(), self.check_texts()))

        Label(self.REGISTRATION, text="Группа", fg="#FFFFFF", bg="#444444").place(x=x, y=height + interval * 1)
        self.gruop = StringVar()
        self.gruop_Entry = Entry(self.REGISTRATION, textvariable=self.gruop, bg="#222222", fg="#FFFFFF",
                                 selectbackground="#444444", selectforeground="#19C710",width=13,font=("Bahnschrift Light SemiCondensed", 18))
        self.gruop_Entry.place(x=x, y=height + interval * 1 + 22)
        self.gruop_Entry.bind("<Any-KeyRelease>", lambda event: (self.check_group(), self.check_texts()))

        fon = list(font.families())
        f = font.Font(family=fon[88], size=14)
        self.b = Button(self.REGISTRATION, text="Регистрация", width=13, height=1, bg='#222222', fg='#EEEEEE', bd=0,
                        activebackground='#333333',
                        activeforeground='#EEEEEE', highlightcolor="black", relief=SUNKEN,
                        font=f, command=self.press)
        self.b.place(x=220, y=380)
        self.b['state'] = 'disabled'
        self.REGISTRATION.bind("<Return>", lambda _: self.press())
        self.REGISTRATION.grid()
        self.REGISTRATION.mainloop()

    def proverka(self, all_data, el, name):
        for i in all_data:
            if el == i[name]:
                return True
        return False

    def press(self):
        if not (self.login.get() and self.password.get() and self.name.get() and self.gruop.get()):
            messagebox.askretrycancel('Пустое поле', 'Введите данные')
        else:
            # Регистрация
            with open('publickey', 'r') as public:
                pub_key = tuple(int(i) for i in public.readline().split(','))
            introduced_passwords = rsa.encrypt(self.password.get().encode('utf8'), rsa.PublicKey(*pub_key))
            self.cursor.execute("SELECT USERNAME FROM users")
            all_data = self.cursor.fetchall()
            if not self.proverka(all_data, self.login.get(), 'USERNAME'):
                # Регистрация
                self.cursor.execute(
                    "INSERT INTO `users` (`id`, `USERNAME`, `password`, `name`, `grup`) VALUES (NULL, ?, ? ,?, ?)",
                    (
                        self.login.get(), introduced_passwords, self.name.get(), self.gruop.get()))
                self.conn.commit()
                messagebox.showinfo('Готово', 'Пользователь создан')
                self.REGISTRATION.destroy()
                LogIN.Login()
            else:
                messagebox.showerror('Ошибка', 'Пользователь уже существует')

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def check_login(self):
        pattern = r"[^-_\s][\w_-]{3,18}\b"
        if self.login.get() in self.logins:
            self.label['text'] = 'Логин существует'
        else:
            self.label['text'] = ''
        if re.fullmatch(pattern, self.login.get()) and self.login.get() not in self.logins:
            self.ButLog['fg'] = '#19C710'
        elif not self.login.get():
            self.ButLog['fg'] = '#222222'
        else:
            self.ButLog['fg'] = '#FF002F'

    def check_password(self):
        pattern = r"(?=.*[A-ZА-Я])(?=.*[0-9].*[0-9])(?=.*[a-zа-я].*[a-zа-я].*[a-zа-я]).{8,}\b"
        self.check_second_password()
        if re.fullmatch(pattern, self.password.get()):
            self.pas['fg'] = '#19C710'
        elif not self.password.get():
            self.pas['fg'] = '#222222'
        else:
            self.pas['fg'] = '#FF002F'

    def check_second_password(self):
        if self.password.get() == self.second_password.get() != "":
            self.sec_pas['fg'] = '#19C710'
        elif not self.second_password.get():
            self.sec_pas['fg'] = '#222222'
        else:
            self.sec_pas['fg'] = '#FF002F'

    def check_texts(self):
        if self.name_Entry['fg'] == self.gruop_Entry['fg'] == self.ButLog['fg'] == self.pas['fg'] == \
                self.sec_pas['fg'] == "#19C710":
            self.b['state'] = 'normal'
        else:
            self.b['state'] = 'disabled'

    def check_group(self):
        pattern = r"[А-Я]{1}-\d{4}\b"

        if re.fullmatch(pattern, self.gruop.get()):
            self.gruop_Entry['fg'] = '#19C710'
        elif not self.gruop_Entry.get():
            self.gruop_Entry['fg'] = '#222222'
        else:
            self.gruop_Entry['fg'] = '#FF002F'

    def check_name(self):
        pattern = r"[А-ЯA-ZЁ][а-яa-zё]{2,}\s?[А-ЯA-ZЁ]?[а-яa-zё]{0,}"

        if re.fullmatch(pattern, self.name.get()):
            self.name_Entry['fg'] = '#19C710'
        elif not self.name.get():
            self.name_Entry['fg'] = '#222222'
        else:
            self.name_Entry['fg'] = '#FF002F'


if __name__ == "__main__":
    Registration()
