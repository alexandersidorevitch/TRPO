from ttkthemes import ThemedTk

from sortirovka import *

root_main = None
def start(func, kol, speed, values=None, color_scheme="dracula"):
    root_main = ThemedTk()
    root_main.iconbitmap('icon.ico')
    root_main.title("Vizulization")
    root_main.set_theme('equilux')
    height = root_main.winfo_screenheight() - 300
    width = root_main.winfo_screenwidth() - 300
    root_main.geometry(
        '{}x{}+{}+{}'.format(width, height, (root_main.winfo_screenwidth() - width) // 2,
                             (root_main.winfo_screenheight() - height) // 2))
    root_main.resizable(False, False)
    if values:
        kol = len(values)
    func(width, height, kol, name=root_main, color_scheme=color_scheme, speed=speed, values=values).sort()
    root_main.mainloop()


def destroy():
    QuickSort.stop = True
    root_main.destroy()


if __name__ == '__main__':
    start(BubbleSort, 8, 5)
