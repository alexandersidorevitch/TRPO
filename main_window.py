#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from random import shuffle
from sqlite3 import *
from tkinter import font, messagebox

import Visualition
import Info
import records

invert = int("bbbbbb", 16)


def invert_color(color):
    rezult = str(hex(abs(invert - int(color[1:], 16))))[2:]
    return '#' + (6 - len(rezult)) * '0' + rezult


class VerticalScrolledFrame:
    """
 A vertically scrolled Frame that can be treated like any other Frame
 ie it needs a master and layout and it can be a master.
 :width:, :height:, :bg: are passed to the underlying Canvas
 :bg: and all other keyword arguments are passed to the inner Frame
 note that a widget layed out in this frame will have a self.master 3 layers deep,
 (outer Frame, Canvas, inner Frame) so
 if you subclass this there is no built in way for the children to access it.
 You need to provide the controller separately.
    """

    def __init__(self, master, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        bg = kwargs.pop('bg', kwargs.pop('background', None))
        self.varible = tk.StringVar()
        self.master = master
        self.func = None
        self.outer = tk.Frame(master, **kwargs)
        self.edit = tk.Entry(master, textvariable=self.varible, bg=invert_color("#222222"), fg=invert_color("#FFFFFF"),
                             selectbackground=invert_color("#60CA85"), font=("@Microsoft YaHei UI Light", 32, "bold"))
        kwargs = dict(text="начать".capitalize(), width=12, height=1, bg=invert_color('#222222'),
                      fg=invert_color('#EEEEEE'), bd=0,
                      activebackground=invert_color('#333333'),
                      activeforeground=invert_color('#EEEEEE'), relief=tk.SUNKEN, state='disabled',
                      font=("@Microsoft YaHei UI Light", 32, "bold"))
        self.vizual_button = tk.Button(master, **kwargs,
                                       command=lambda: self.press_vizual())
        self.main_text = tk.Label(self.outer, text="", font=("Bahnschrift Light SemiCondensed", 32, "bold"),
                                  bg=invert_color('#F0F0F0'), fg=invert_color('#111111'))

        self.vizual_lebel = tk.Label(master, text="Введите количество элементов или массив значений",
                                     font=font.Font(family="@Microsoft YaHei UI Light", size=14), bg=bg,
                                     fg=invert_color('#000000'))
        self.edit.bind("<Any-KeyRelease>", self.check)
        # ttk.Notebook()relief=tk.FLAT,
        self.usual_text = tk.Text(width=82, height=10, wrap=tk.WORD, font=("@Microsoft YaHei UI Light", 16),
                                  relief=tk.FLAT,
                                  bg=invert_color('#F0F0F0'), fg=invert_color('#111111'))

        scroll = tk.Scrollbar(command=self.usual_text.yview)
        self.usual_text.config(yscrollcommand=scroll.set)
        self.create_text()
        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        # self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        self.canvas = tk.Canvas(self.outer, highlightthickness=0, bd=0, width=width, height=height, bg=bg)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        self.canvas['yscrollcommand'] = self.vsb.set
        # mouse scroll does not seem to work with just "bind"; You have
        # to use "bind_all". Therefore to use multiple windows you have
        # to bind_all in the current widget
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame(self.canvas, bg=bg)
        self.outer['bg'] = bg
        self.inner['bg'] = bg
        # pack the inner Frame into the Canvas with the topleft corner 4 pixels offset
        self.canvas.create_window(0, 0, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            # geometry attributes etc (eg pack, destroy, tkraise) are passed on to self.outer
            return getattr(self.outer, item)
        else:
            # all other attributes (_w, children, etc) are passed to self.inner
            return getattr(self.inner, item)

    def create_text(self):

        self.main_text.place(x=191, rely=0.05)
        self.usual_text.place(x=191, y=300)

    def delete_text(self):
        self.main_text.place_forget()
        self.usual_text.place_forget()

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion=(0, 0, x2, max(y2, height)))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def invert_color(self, color):
        return '#' + str(hex(abs(self.color - int(color, 16))))[2:]

    def update_texts(self, **kwargs):
        main_text = kwargs.pop("main_text", '')
        usual_text = kwargs.pop("usual_text", '')
        self.main_text["text"] = main_text
        self.usual_text.configure(state='normal')
        self.usual_text.delete(1.0, tk.END)
        self.usual_text.insert(1.0, str(usual_text))
        self.usual_text.configure(state='disabled')

    def press_vizual(self):
        if self.varible.get().count(','):
            if len(self.varible.get().split(',')) < 180:
                speed = 1
            else:
                speed = 3
            Visualition.start(self.func, len(self.varible.get().split(',')), speed,
                              list(map(lambda x: 980 - int(x), self.varible.get().split(','))))
        else:
            if int(self.varible.get()) < 180:
                speed = 30
            else:
                speed = 3
            Visualition.start(self.func, int(self.varible.get()), int(self.varible.get()) // 3)

    def check_mas(self, mas):
        for i in mas:
            if not i.isdigit() or i == "" or not 0 <= int(i) <= 1000:
                return False
        return True

    def check(self, event):
        if self.varible.get() != "" and self.varible.get()[-1] == ",":
            self.vizual_button["state"] = 'disabled'
            return
        if (self.varible.get().count(",") and self.check_mas(self.varible.get().split(","))) or (
                self.varible.get().isdigit() and 0 < int(self.varible.get()) <= 270):
            self.vizual_button["state"] = 'normal'
        else:
            self.vizual_button["state"] = 'disabled'


#  **** SCROLL BAR TEST *****

class main_window:
    def __init__(self, varib=1, login=''):
        self.MAIN_WINDOW = tk.Tk()
        self.MAIN_WINDOW.title("Scrollbar Test")
        self.MAIN_WINDOW.resizable(False, True)
        self.login = login
        self.color = 0
        if varib:
            global invert
            invert = 0
        print('#' + str(hex(abs(self.color - int('7CD5CB', 16))))[2:])
        self.variable = []
        self.test_buttons = []
        self.questions = tuple()
        self.answers = []
        self.types = tuple()
        self.id = tuple()
        self.number = 0
        self.correct = 0
        self.text = tk.StringVar()
        self.menu_varible = tk.IntVar()
        menu = tk.Menu()
        settings = tk.Menu(tearoff=0)
        self.menu_varible.set(varib)
        settings.add_radiobutton(label='Темная тема', value=0, variable=self.menu_varible, command=self.invett_colors)
        settings.add_radiobutton(label='Светлая тема', value=1, variable=self.menu_varible, command=self.invett_colors)
        menu.add_cascade(label='Настройки темы', menu=settings)
        menu.add_cascade(label='Рекорды', command=lambda: records.records())
        menu.add_cascade(label='Справка', command=lambda: Info.Info(self.MAIN_WINDOW))
        self.MAIN_WINDOW.config(menu=menu)
        self.topic = -1
        width = 1200
        height = 900
        self.MAIN_WINDOW.geometry(
            '{}x{}+{}+{}'.format(width, height, (self.MAIN_WINDOW.winfo_screenwidth() - width) // 2,
                                 (self.MAIN_WINDOW.winfo_screenheight() - height) // 2))
        self.MAIN_WINDOW.minsize(width=900, height=600)
        self.MAIN_WINDOW.protocol('WM_DELETE_WINDOW', self.window_deleted)
        self.MAIN_WINDOW.iconbitmap('icon.ico')
        self.buttons = []
        self.conn = connect('project_trpo')  # подлкючение к БД
        self.conn.row_factory = self.dict_factory
        cursor = self.conn.cursor()

        cursor.execute("SELECT topic FROM Topics")
        all_data = cursor.fetchall()

        self.frame = VerticalScrolledFrame(self.MAIN_WINDOW,
                                           width=168,
                                           borderwidth=2,
                                           relief=tk.SUNKEN,
                                           bg=invert_color("#F0F0F0"))
        self.next = tk.Button(self.MAIN_WINDOW, text='Следующий', width=10, height=2, bg=invert_color('#7CD5CB'),
                              fg='#111111', bd=0,
                              activebackground='#333333',
                              disabledforeground='#FFFFFF', highlightcolor="black", relief=tk.SUNKEN,
                              font=font.Font(family="@Microsoft YaHei UI Light", size=10), command=self.next_press)
        self.prev = tk.Button(self.MAIN_WINDOW, text='Предыдущий', width=10, height=2, bg=invert_color('#7CD5CB'),
                              fg='#111111', bd=0,
                              activebackground='#333333',
                              disabledforeground='#FFFFFF', highlightcolor="black", relief=tk.SUNKEN,
                              font=font.Font(family="@Microsoft YaHei UI Light", size=10), command=self.prev_press)
        self.end = tk.Button(self.MAIN_WINDOW, text='Завершить', width=10, height=2, bg=invert_color('#7CD5CB'),
                             fg='#111111', bd=0,
                             activebackground='#333333',
                             disabledforeground='#FFFFFF', highlightcolor="black", relief=tk.SUNKEN,
                             font=font.Font(family="@Microsoft YaHei UI Light", size=10), command=self.end_press)
        self.frame.pack(fill=tk.BOTH, expand=True)  # fill window
        cursor = self.conn.cursor()
        cursor.execute("SELECT topic, Theory FROM Topics")
        data = cursor.fetchall()
        self.frame.update_texts(usual_text=data[0]['Theory'], main_text=data[0]['topic'])
        # self.frame.pack_propagate(0)
        self.MAIN_WINDOW.update()
        # self.frame.edit.place(x=225, y=20)

        self.MAIN_WINDOW['bg'] = invert_color('#F0F0F0')
        self.MAIN_WINDOW.update()
        self.frame.create_text()
        texts_for_buttons = ('Теория', 'Визуализация', 'Тест')
        kol = 0
        # all_data = ['Сортировка "пузырьком".', 'Сортировка "Вставками"', '"Быстрая" сортировка.',
        #             '"Быстрая" сортировка с асинхронностью.', 'Сортировка подсчётом.']
        for i, text in enumerate(all_data):
            self.buttons.append(
                tk.Button(self.frame, text=text['topic'], width=24, height=3,
                          bg=invert_color('#7CD5CB'), fg='#111111', bd=0,
                          activebackground=invert_color('#333333'),
                          disabledforeground='#111111', highlightcolor="black", relief=tk.SUNKEN,
                          wraplength=100,
                          state='disabled',
                          command=lambda key=i + kol: self.press(key)))
            self.buttons[i + kol].bind("<Enter>", lambda event, number=i + kol: self.but(number))
            self.buttons[i + kol].bind("<Leave>", lambda event, number=i + kol: self.butleave(number))
            self.buttons[i + kol].grid(column=2, row=i + kol)
            for j, t in enumerate(texts_for_buttons):
                kol += 1
                self.buttons.append(
                    tk.Button(self.frame,
                              text=(t + ' по "' + text['topic'] + '"')[:21] + "\n" + (t + ' по "' + text['topic']
                                                                                      + '"')[
                                                                                     21:], width=24, height=3,
                              bg=invert_color('#222222'), fg=invert_color('#EEEEEE'), bd=0,
                              activebackground=invert_color('#333333'),
                              activeforeground=invert_color('#EEEEEE'), highlightcolor="black", relief=tk.SUNKEN,
                              justify=tk.LEFT,
                              wraplength=170,
                              command=lambda key=i + kol: self.press(key)))
                self.buttons[i + kol].bind("<Enter>", lambda event, number=i + kol: self.but(number))
                self.buttons[i + kol].bind("<Leave>", lambda event, number=i + kol: self.butleave(number))
                self.buttons[i + kol].grid(column=2, row=i + kol)

        mas = ['ghgf', 'gfdg', 'fdswedfsd', '32e3df', '1wewer34frdsf']
        # self.activate_RadioButton(mas)
        # self.vizual()
        self.MAIN_WINDOW.mainloop()



    def invett_colors(self):
        global invert
        cursor = self.conn.cursor()

        if invert == int('bbbbbb', 16):
            if self.menu_varible.get() == 0:
                return
            invert = 0
        else:
            if self.menu_varible.get() == 1:
                return
            invert = int('bbbbbb', 16)
        cursor.execute("UPDATE Users SET theme = ? WHERE USERNAME = ?", (self.menu_varible.get(), self.login))
        self.conn.commit()
        self.MAIN_WINDOW.destroy()
        main_window(self.menu_varible.get(), self.login)

    def but(self, number: int):
        if not number % 4 == 0 and self.buttons[number]["bg"] != invert_color("#CCCCCC"):
            self.buttons[number]["bg"] = invert_color('#333333')

    def butleave(self, number: int):
        if not number % 4 == 0 and self.buttons[number]["bg"] != invert_color("#CCCCCC"):
            self.buttons[number]["bg"] = invert_color('#222222')
            self.buttons[number]["fg"] = invert_color('#EEEEEE')

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def window_deleted(self):
        # s = "НЕ УХОДИ ВСЕ РАВНО НЕ ПОЛУЧИТЬСЯ".split()
        # for st in s:
        #     messagebox.askretrycancel(title=s[0], message=st)
        self.MAIN_WINDOW.destroy()

    def delete_buttons(self):
        for button in self.test_buttons:
            button.place_forget()

        self.next.place_forget()
        self.end.place_forget()
        self.prev.place_forget()
        self.test_buttons.clear()
        self.variable.clear()

    def activate_CheckButton(self, texts):
        self.delete_buttons()
        self.variable = []
        for i, text in enumerate(texts):
            self.variable.append(tk.IntVar())
            self.test_buttons.append(
                tk.Checkbutton(self.MAIN_WINDOW, text=text[0], variable=self.variable[i], onvalue=1, offvalue=0,
                               wraplength=1000, bg=invert_color('#F0F0F0'), fg=invert_color('#000000'),
                               selectcolor=invert_color('#EEEEEE'),
                               font=font.Font(family="@Microsoft YaHei UI Light", size=20)))
            self.test_buttons[i]['activebackground'] = 'red'
            self.test_buttons[i]['activeforeground'] = 'black'
            self.test_buttons[i].place(x=225, y=150 + 100 * i)

    def activate_RadioButton(self, texts):
        self.delete_buttons()
        self.variable.clear()
        self.variable.append(tk.IntVar())
        for i, text in enumerate(texts):
            self.test_buttons.append(
                tk.Radiobutton(self.MAIN_WINDOW, text=text[0], variable=self.variable[0], value=i, wraplength=900,
                               relief=tk.FLAT, overrelief=tk.FLAT,
                               bg=invert_color('#F0F0F0'), fg=invert_color('#000000'),
                               selectcolor=invert_color('#EEEEEE'),
                               font=font.Font(family="@Microsoft YaHei UI Light", size=20)))
            self.test_buttons[i].place(x=225, y=150 + 140 * i)

    def press(self, key):
        # print(colorchooser.askcolor('#ff9dee'))
        for button in self.buttons:
            if button['bg'] == invert_color('#CCCCCC'):
                button['bg'] = invert_color('#222222')
                button['fg'] = invert_color('#EEEEEE')
        self.buttons[key]['bg'] = invert_color('#CCCCCC')
        self.buttons[key]['fg'] = invert_color('#222222')
        self.vizual_delete()
        self.frame.delete_text()
        self.delete_buttons()
        item = key % 4
        block = key // 4
        self.frame.func = \
            (Visualition.BubbleSort, Visualition.InsertionSort, Visualition.QuickSort, Visualition.AsyncQuickSort,
             Visualition.ContingSort
             )[block]
        if item == 2:
            self.vizual()
        elif item == 1:
            cursor = self.conn.cursor()
            cursor.execute("SELECT topic, Theory FROM Topics")
            all_data = cursor.fetchall()
            self.frame.update_texts(usual_text=all_data[block].get('Theory'), main_text=all_data[block]['topic'])
            self.frame.create_text()
        elif item == 3:
            self.topic = block
            self.end['bg'] = invert_color('#7CD5CB')
            self.end['state'] = 'normal'
            cursor = self.conn.cursor()
            self.correct = 0
            self.number = 0
            cursor.execute("SELECT id, question, type FROM Questions WHERE topic = ?", (block,))
            all_data = cursor.fetchall()
            self.questions = tuple(i['question'] for i in all_data)
            self.types = tuple(i['type'] for i in all_data)
            self.id = tuple(i['id'] for i in all_data)
            self.frame.update_texts(main_text=all_data[0]['question'])
            self.frame.create_text()
            cursor.execute("SELECT LABEL, correct FROM All_Answers WHERE question_id = ?", (self.id[0],))
            all_data = cursor.fetchall()
            self.answers = [(i['LABEL'], i['correct']) for i in all_data]
            shuffle(self.answers)
            if self.types[0] == '1':
                self.activate_CheckButton(self.answers)
            else:
                self.activate_RadioButton(self.answers)

            self.variable[0].set(-1)

            self.prev['state'] = 'disabled'
            self.prev['bg'] = '#333333'
            if len(self.questions) == 1:
                self.next['state'] = 'disabled'
                self.next['bg'] = '#333333'
                self.end['state'] = 'normal'
                self.end['bg'] = invert_color('#7CD5CB')
                self.end.place(x=800, y=800)
            else:
                self.next['state'] = 'normal'
                self.next['bg'] = invert_color('#7CD5CB')
            self.next.place(x=1000, y=800)
            self.prev.place(x=900, y=800)

    def check(self):
        if self.types[self.number] == '1':
            # проверка CheckButton
            for i, answer in enumerate(self.answers):
                if not answer[1] == self.variable[i].get():
                    return False
            else:
                return True
        else:
            # проверка RadioButton
            for i, answer in enumerate(self.answers):
                if answer[1] == 1:
                    if self.variable[0].get() == i:
                        return True
                    break
            return False

    def end_press(self):
        if self.check():
            self.correct += 1
        self.end['state'] = 'disabled'
        self.end['bg'] = '#333333'
        self.prev['state'] = 'disabled'
        self.prev['bg'] = '#333333'
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM Records WHERE USERNAME = ? AND topic = ? AND result <= ?',
                       (self.login, self.topic, round(self.correct / len(self.questions) * 100, 1)))
        self.conn.commit()
        cursor.execute(
            '''INSERT INTO Records(USERNAME,topic, result) SELECT ?, ?, ? WHERE NOT EXISTS(SELECT 1 FROM Records 
            WHERE USERNAME = ? AND topic = ?);''',
            (self.login, self.topic, round(self.correct / len(self.questions) * 100, 1), self.login, self.topic,))
        self.conn.commit()
        messagebox.askquestion('Конец', 'Ваш резульльтат прохождени теста ' + str(
            round(self.correct / len(self.questions) * 100, 1)) + ' %.')

    def next_press(self):
        if self.check():
            self.correct += 1

        self.number += 1
        cursor = self.conn.cursor()
        cursor.execute("SELECT LABEL, correct FROM All_Answers WHERE question_id = ?", (self.id[self.number],))
        all_data = cursor.fetchall()
        self.answers = [(i['LABEL'], i['correct']) for i in all_data]
        shuffle(self.answers)
        if self.types[self.number] == '1':
            self.activate_CheckButton(self.answers)
        else:
            self.activate_RadioButton(self.answers)

        if self.number != 0:
            self.prev['state'] = 'normal'
            self.prev['bg'] = invert_color('#7CD5CB')

        if len(self.questions) == self.number + 1:
            self.end.place(x=800, y=800)
            self.next['state'] = 'disabled'
            self.next['bg'] = '#333333'
        else:
            self.next['state'] = 'normal'
            self.next['bg'] = invert_color('#7CD5CB')

        self.frame.update_texts(main_text=self.questions[self.number])
        self.frame.create_text()
        self.next.place(x=1000, y=800)
        self.prev.place(x=900, y=800)

    def prev_press(self):

        self.number -= 1
        cursor = self.conn.cursor()
        cursor.execute("SELECT LABEL, correct FROM All_Answers WHERE question_id = ?", (self.id[self.number],))
        all_data = cursor.fetchall()
        self.answers = [(i['LABEL'], i['correct']) for i in all_data]
        shuffle(self.answers)

        if self.check():
            self.correct -= 1
        if self.number == 0:
            self.prev['state'] = 'disabled'
            self.prev['bg'] = '#333333'
        if self.types[self.number] == '1':
            self.activate_CheckButton(self.answers)
        else:
            self.activate_RadioButton(self.answers)

        if self.number != len(self.questions) - 1:
            self.next['state'] = 'normal'
            self.next['bg'] = invert_color('#7CD5CB')

        if len(self.questions) != self.number + 1:
            self.next['state'] = 'normal'
            self.next['bg'] = invert_color('#7CD5CB')

        self.frame.update_texts(main_text=self.questions[self.number])
        self.frame.create_text()
        self.next.place(x=1000, y=800)
        self.prev.place(x=900, y=800)

    def vizual_delete(self):
        self.frame.vizual_lebel.place_forget()
        self.frame.edit.place_forget()
        self.frame.vizual_button.place_forget()

    def vizual(self):
        self.delete_buttons()
        self.frame.varible.set("")
        self.frame.vizual_lebel.place(x=500, y=340)
        self.frame.edit.place(x=500, y=375)
        self.frame.vizual_button.place(x=500, y=150)


if __name__ == "__main__":
    main_window(1, 'A_Valer')
