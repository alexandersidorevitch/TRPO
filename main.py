from tkinter import *

from sortirovka import *

root = Tk()
#                           0,     1,          2,          3,      4
#                            bg, normal_color, choise1, chois2, ok_color
colors_scheme = {"dracula": ("white", "#A9B7C6", "#A94826", "#8888C6", "#8DB897"),
                 "normal": ("white", "#C61B0C", "#1FA2C6", "#C67000", "#25A90D")}
diveders = [int(i) for i in range(2, root.winfo_screenwidth() - 36) if (root.winfo_screenwidth() - 36) % i == 0]
height = int(root.winfo_screenheight() - 100)
width = int(root.winfo_screenwidth() - 36)
kol = 41
root.geometry(
    '{}x{}+{}+{}'.format(width, height, (root.winfo_screenwidth() - width - 100) // 2,
                         (root.winfo_screenheight() - height - 100) // 2))
root.resizable(False, False)
#
#

inc = InsertionSort(width, height, kol, name=root, color_scheme="dracula")
inc.sort()
root.mainloop()
