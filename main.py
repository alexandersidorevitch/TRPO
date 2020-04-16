from tkinter import *
from ttkthemes import ThemedTk
from sortirovka import *

def start():
    root_main = ThemedTk()
    root_main.set_theme('equilux')
    #                           0,     1,          2,          3,      4
    #                            bg, normal_color, choise1, chois2, ok_color
    colors_scheme = {"dracula": ("white", "#A9B7C6", "#A94826", "#8888C6", "#8DB897"),
                     "normal": ("white", "#C61B0C", "#1FA2C6", "#C67000", "#25A90D")}
    diveders = [int(i) for i in range(2, root_main.winfo_screenwidth() - 36) if (root_main.winfo_screenwidth() - 36) % i == 0]
    height = int(root_main.winfo_screenheight() - 100)
    width = int(root_main.winfo_screenwidth() - 36)
    values = list(map(lambda x:int(x/100*height),[10,20,30,40,50,60,70,80]))
    kol = len(values)
    print(values)
    root_main.geometry(
        '{}x{}+{}+{}'.format(width, height, (root_main.winfo_screenwidth() - width - 100) // 2,
                             (root_main.winfo_screenheight() - height - 100) // 2))
    root_main.resizable(False, False)
    inc = InsertionSort(width, height, kol, name=root_main, color_scheme="dracula",values = values)
    inc.sort()
    root_main.mainloop()

if __name__ == '__main__':
    start()

