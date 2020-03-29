from tkinter import *
from ttkthemes import ThemedTk
from sortirovka import *

root = ThemedTk()
root.set_theme('equilux')
#                           0,     1,          2,          3,      4
#                            bg, normal_color, choise1, chois2, ok_color
colors_scheme = {"dracula": ("white", "#A9B7C6", "#A94826", "#8888C6", "#8DB897"),
                 "normal": ("white", "#C61B0C", "#1FA2C6", "#C67000", "#25A90D")}
diveders = [int(i) for i in range(2, root.winfo_screenwidth() - 36) if (root.winfo_screenwidth() - 36) % i == 0]
height = int(root.winfo_screenheight() - 100)
width = int(root.winfo_screenwidth() - 36)
kol = diveders[randint(0,len(diveders))]
root.geometry(
    '{}x{}+{}+{}'.format(width, height, (root.winfo_screenwidth() - width - 100) // 2,
                         (root.winfo_screenheight() - height - 100) // 2))
root.resizable(False, False)
#
#

inc = QuickSort(width, height, kol, name=root, color_scheme="dracula")
inc.sort()
root.mainloop()
