from tkinter import *
from tkinter import colorchooser
from random import shuffle
from sqlite3 import *
from tkinter import font,messagebox



class Setings:
    def __init__(self):
        self.SETTINGS = Tk()
        width = 1200
        height = 900

        self.SETTINGS.geometry(
            '{}x{}+{}+{}'.format(width, height, (self.SETTINGS.winfo_screenwidth() - width) // 2,
                                 (self.SETTINGS.winfo_screenheight() - height) // 2))
        self.SETTINGS.minsize(width=900, height=600)
        self.SETTINGS.iconbitmap('icon.ico')