from sortirovka import *
from tkinter import *
print(hex(int("a9b7d0",16)+50))
root = Tk()
#0,     1,          2,          3,      4
# bg, normal_color, choise1, chois2, ok_color
colors_scheme = {"dracula": ("white", "#A9B7C6", "#A94826", "#8888C6", "#8DB897"),
                 "normal": ("white", "#C61B0C", "#1FA2C6", "#C67000", "#25A90D")}
diveders = [int(i) for i in range(2,root.winfo_screenwidth()-36) if (root.winfo_screenwidth()-36) % i == 0]
height = int(root.winfo_screenheight() - 100)
width = int(root.winfo_screenwidth() - 36)
# kol = 40
kol = 498
qui = QuickSort(width, height, kol, name=root, color_scheme="dracula")
root.geometry(
    '{}x{}+{}+{}'.format(width, height, (root.winfo_screenwidth() - width - 100) // 2,
                         (root.winfo_screenheight() - height - 100) // 2))
root.resizable(False, False)
#
#
qui.sort()
sleep(5)
qui.c.destroy()
qui2 = QuickSort(width, height, kol, name=root, color_scheme="dracula")
qui2.sort_no_async()
qui2.c.destroy()
# qui.ranbow()
# qui.show()
# qui.c.destroy()
sleep(3)
cs = ContingSort(width, height, kol, name=root, color_scheme="dracula")
cs.sort()
sleep(5)
cs.c.destroy()
bubble = BubbleSort(width, height, kol, name=root, color_scheme="dracula")
bubble.sort()
bubble.c.destroy()
inc = InsertionSort(width, height, kol, name=root, color_scheme="dracula")
inc.sort()
root.mainloop()
