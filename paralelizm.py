from create import *
from decimal import Decimal as Des
from random import choice
import multiprocessing

class QuickSort(Create):
    def __init__(self, width: int, height: int, kol: int, **args):
        super().__init__(width, height, kol, args["name"], args["color_scheme"])
        self.sleep = 1
        self.iter = 0
        self.rand_colors = ('#D0FF00', '#00FFA9', "#E99105", "#E90084", "#09E2E9")

    def show1(self, first_place, second_place):
        c = Des(1 / Des((90 // self.speed)))
        if first_place > second_place:
            a = -1
            b = 1
        else:
            a = 1
            b = -1
        precolor1 = self.c.itemcget(self.tags[first_place], 'fill')
        precolor2 = self.c.itemcget(self.tags[second_place], 'fill')
        self.c.itemconfig(self.tags[first_place], fill=self.colors_scheme[self.all_color][2])
        self.c.itemconfig(self.tags[second_place], fill=self.colors_scheme[self.all_color][3])
        for i in range(90 // self.speed):
            sleep((1 / (((self.speed) * 10) ** 2)))
            self.c.move(self.tags[first_place], self.width_prym * a * abs(first_place - second_place) * c, 0)
            self.c.move(self.tags[second_place], self.width_prym * b * abs(first_place - second_place) * c, 0)
            self.c.update()
        self.c.itemconfig(self.tags[first_place], fill=precolor1)
        self.c.itemconfig(self.tags[second_place], fill=precolor2)
        self.c.update()
    def sort_no_async(self):
        def partition(nums, start, end):
            tmp_color = choice(self.rand_colors)
            for i in range(start, end + 1):
                self.c.itemconfig(self.tags[i], fill=tmp_color)
            pivotIndex = start
            pivotValue = nums[end]
            for i in range(start, end):
                self.iter += 1
                if nums[i] < pivotValue:
                    nums[i], nums[pivotIndex] = nums[pivotIndex], nums[i]
                    self.show1(pivotIndex, i)
                    self.tags[i], self.tags[pivotIndex] = self.tags[pivotIndex], self.tags[i]
                    pivotIndex += 1
            nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
            self.show1(pivotIndex, end)
            self.tags[pivotIndex], self.tags[end] = self.tags[end], self.tags[pivotIndex]
            for i in range(start, end + 1):
                self.c.itemconfig(self.tags[i], fill=self.colors_scheme[self.all_color][1])
            return pivotIndex

        def quicksort(nums, start, end):
            if start >= end: return


            index = partition(nums, start, end)

            p =multiprocessing.Process(target=quicksort, args=(nums, start, index - 1))
            p.start()
            pr.append(p)
            # quicksort(nums, start, index - 1)

            t = multiprocessing.Process(target=quicksort,args=(nums, index + 1, end))
            t.start()
            pr.append(t)

            # quicksort(nums, index + 1, end)
            for i in pr:
                try:
                    i.join()
                except:
                    pass
        lock = multiprocessing.Lock
        pr = []
        multiprocessing.Pool(5)
        quicksort(self.height_prym, 0, self.kol - 1)
        self.c.update()



root_main = Tk()
#                           0,     1,          2,          3,      4
#                            bg, normal_color, choise1, chois2, ok_color
colors_scheme = {"dracula": ("white", "#A9B7C6", "#A94826", "#8888C6", "#8DB897"),
                 "normal": ("white", "#C61B0C", "#1FA2C6", "#C67000", "#25A90D")}
diveders = [int(i) for i in range(2, root_main.winfo_screenwidth() - 36) if (root_main.winfo_screenwidth() - 36) % i == 0]
height = int(root_main.winfo_screenheight() - 100)
width = int(root_main.winfo_screenwidth() - 36)
kol = diveders[-3]
root_main.geometry(
    '{}x{}+{}+{}'.format(width, height, (root_main.winfo_screenwidth() - width - 100) // 2,
                         (root_main.winfo_screenheight() - height - 100) // 2))
root_main.resizable(False, False)
inc = QuickSort(width, height, kol, name=root_main, color_scheme="dracula")
inc.sort_no_async()
root_main.mainloop()