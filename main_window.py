#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from random import shuffle
from sqlite3 import *
from tkinter import font

import Visualition


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
        self.edit = tk.Entry(master, textvariable=self.varible, bg="#222222", fg="#FFFFFF",
                             selectbackground="#60CA85", font=("@Microsoft YaHei UI Light", 32, "bold"))
        kwargs = dict(text="Вход", width=12, height=1, bg='#222222', fg='#EEEEEE', bd=0,
                      activebackground='#333333',
                      activeforeground='#EEEEEE', highlightcolor="black", relief=tk.SUNKEN, state='disabled',
                      font=("@Microsoft YaHei UI Light", 32, "bold"))
        self.vizual_button = tk.Button(master, **kwargs,
                                       command=lambda: self.press_vizual())
        self.main_text = tk.Label(self.outer, text="", font=("Bahnschrift Light SemiCondensed", 32, "bold"))

        self.vizual_lebel = tk.Label(master, text="Введите количество элементов или массив значений",
                                     font=font.Font(family="@Microsoft YaHei UI Light", size=14))
        self.edit.bind("<Any-KeyRelease>", self.check)
        # ttk.Notebook()
        self.usual_text = tk.Text(width=82, height=10, wrap=tk.WORD, font=("@Microsoft YaHei UI Light", 16),
                                  relief=tk.FLAT,
                                  bg='#FFFFFF',fg='#000000')

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
        self.main_text.place(x=191, rely=0.1)
        self.usual_text.place(x=191, y=200)

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

    def update_texts(self, **kwargs):
        main_text = kwargs.pop("main_text", None)
        usual_text = kwargs.pop("usual_text", None)
        self.main_text["text"] = main_text
        self.usual_text.configure(state='normal')
        print('\n\n\n\n\n\n'+self.usual_text.get(1.0,tk.END))
        self.usual_text.delete(1.0, tk.END)
        self.usual_text.insert(1.0, str(usual_text))
        self.usual_text.configure(state='disabled')

    def press_vizual(self):
        if self.varible.get().count(','):
            if len(self.varible.get().split(',')) < 180:
                speed = 30
            else:
                speed = 3
            Visualition.start(self.func, len(self.varible.get().split(',')), speed,
                              list(map(lambda x: 980 - int(x), self.varible.get().split(','))))
        else:
            if int(self.varible.get()) < 180:
                speed = 1
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
    def __init__(self):
        self.MAIN_WINDOW = tk.Tk()
        self.MAIN_WINDOW.title("Scrollbar Test")
        self.MAIN_WINDOW.resizable(False,True)
        self.variable = []
        self.test_buttons = []
        self.text = tk.StringVar()
        width = 1200
        height = 600
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
                                           bg="black")

        self.frame.pack(fill=tk.BOTH, expand=True)  # fill window
        cursor = self.conn.cursor()
        cursor.execute("SELECT topic, Theory FROM Topics")
        data = cursor.fetchall()
        self.frame.update_texts(usual_text=data[0]['Theory'],main_text=data[0]['topic'])
        # self.frame.pack_propagate(0)
        self.MAIN_WINDOW.update()
        # self.frame.edit.place(x=225, y=20)
        self.MAIN_WINDOW.update()
        self.frame.create_text()
        texts_for_buttons = ('Теория', 'Визуализация', 'Тест')
        kol = 0
        # all_data = ['Сортировка "пузырьком".', 'Сортировка "Вставками"', '"Быстрая" сортировка.',
        #             '"Быстрая" сортировка с асинхронностью.', 'Сортировка подсчётом.']
        for i, text in enumerate(all_data):
            self.buttons.append(
                tk.Button(self.frame, text=text['topic'], width=24, height=3, bg='#7CD5CB', fg='#111111', bd=0,
                          activebackground='#333333',
                          disabledforeground='#111111', highlightcolor="black", relief=tk.SUNKEN, wraplength=100,
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
                              bg='#222222', fg='#EEEEEE', bd=0,
                              activebackground='#333333',
                              activeforeground='#EEEEEE', highlightcolor="black", relief=tk.SUNKEN, justify=tk.LEFT,
                              wraplength=170,
                              command=lambda key=i + kol: self.press(key)))
                self.buttons[i + kol].bind("<Enter>", lambda event, number=i + kol: self.but(number))
                self.buttons[i + kol].bind("<Leave>", lambda event, number=i + kol: self.butleave(number))
                self.buttons[i + kol].grid(column=2, row=i + kol)


        mas = ['ghgf', 'gfdg', 'fdswedfsd', '32e3df', '1wewer34frdsf']
        # self.activate_RadioButton(mas)
        # self.vizual()
        self.MAIN_WINDOW.mainloop()

    def but(self, number: int):
        if number % 4 == 0:
            pass
        else:
            self.buttons[number]["bg"] = '#333333'

    def butleave(self, number: int):
        if number % 4 == 0:
            pass
        else:
            self.buttons[number]["bg"] = '#222222'

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
        self.test_buttons.clear()
        self.variable.clear()

    def activate_CheckButton(self, texts):
        self.delete_buttons()
        shuffle(texts)
        for i, text in enumerate(texts):
            self.variable.append(tk.IntVar())
            self.test_buttons.append(
                tk.Checkbutton(self.MAIN_WINDOW, text=text, variable=self.variable[i], onvalue=1, offvalue=0))
            self.test_buttons[i].place(x=225, y=375 + 30 * i)

    def activate_RadioButton(self, texts):
        self.delete_buttons()
        self.variable.append(tk.IntVar())
        shuffle(texts)
        for i, text in enumerate(texts):
            self.test_buttons.append(
                tk.Radiobutton(self.MAIN_WINDOW, text=text, variable=self.variable[0], value=i))
            self.test_buttons[i].place(x=225, y=375 + 30 * i)

    def press(self, key):
        self.vizual_delete()
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

    def vizual_delete(self):
        self.frame.vizual_lebel.place_forget()
        self.frame.edit.place_forget()
        self.frame.vizual_button.place_forget()

    def vizual(self):
        self.frame.delete_text()
        self.frame.vizual_lebel.place(x=500, y=340)
        self.frame.edit.place(x=500, y=375)
        self.frame.vizual_button.place(x=500, y=150)


if __name__ == "__main__":
    main_window()
