import colorsys
from decimal import Decimal as des
from random import randint
from time import sleep
from tkinter import *


class Create():
    def __init__(self, width: int, height: int, kol: int, name, color_scheme: str):
        self.height = height
        self.width = width
        self.width_prym = des(des(width) / des(kol))
        self.tags = []
        self.kol = kol
        self.all_color = color_scheme
        self.colors_scheme = {"dracula": ("#525252", "#A9B7C6", "#A94826", "#8888C6", "#8DB897"),
                              "normal": ("white", "#C61B0C", "#1FA2C6", "#C67000", "#25A90D")}
        # self.height_prym = [int(i) for i in range(10,kol*2+10,2)]
        self.height_prym = [randint(height // 15, height - 10) for i in range(kol)]
        self.c = Canvas(name, height=height, width=width, bg=self.colors_scheme[color_scheme][0])
        self.speed = 90
        self.colors = [0 for i in range(kol)]
        for i in range(kol):
            self.tags.append(
                self.c.create_rectangle(i * self.width_prym, self.height, i * self.width_prym + self.width_prym,
                                        self.height_prym[i],
                                        fill=self.colors_scheme[color_scheme][1], activefill="#CB602D"))
        self.c.pack()

    def ALL_COLOR(self):
        return self.all_color

    def changeSpeed(self, speed):
        self.speed = speed

    def create(self, first_place, second_place, reverse=False):
        rev = des(1 / des((90 // self.speed)))
        if reverse:
            rev = -rev
        precolor1 = self.c.itemcget(self.tags[first_place], 'fill')
        precolor2 = self.c.itemcget(self.tags[second_place], 'fill')
        self.c.itemconfig(self.tags[first_place], fill=self.colors_scheme[self.all_color][2])
        self.c.itemconfig(self.tags[second_place], fill=self.colors_scheme[self.all_color][3])
        for i in range(90 // self.speed):
            sleep(1 / des(((self.speed * 10) ** 2)))
            self.c.move(self.tags[first_place], self.width_prym * rev * abs(first_place - second_place), 0)
            self.c.move(self.tags[second_place], -self.width_prym * rev * abs(first_place - second_place), 0)
            self.c. ()
        self.c.itemconfig(self.tags[first_place], fill=precolor1)
        self.c.itemconfig(self.tags[second_place], fill=precolor2)
        self.c.update()

    def animation(self):
        for i in range(self.kol // 2):
            sleep(0.03)
            self.create(i, self.kol - i - 1)
        sleep(2)
        for i in range(self.kol // 2, self.kol):
            sleep(0.03)
            self.create(i, self.kol - i - 1)

    def ranbow(self):
        ran = (int(i) / 100000 for i in range(0, 100000, 100000 // self.kol))
        # если нужен рандом раскоментить эти строчики  а также строчку 97
        # colors = [int(i) for i in range(self.kol)]
        rendomColors = []
        # while colors != []:
        #     tmp = random.choice(colors)
        #     del colors[colors.index(tmp)]
        #     rendomColors.append(tmp)
        i = 0
        for hue in ran:
            if i >= self.kol:
                break
            sleep(1 / (self.speed * self.speed))
            (r, g, b) = colorsys.hsv_to_rgb(hue, .6, .6)
            R, G, B = int(255 * r), int(255 * g), int(255 * b)
            Rc = "#" + str(hex(R))[2:]
            Gc = str(hex(G))[2:]
            Bc = str(hex(B))[2:]
            if len(Rc) == 2:
                Rc = Rc[0] + '0' + Rc[1]
            if len(Gc) == 1:
                Gc = '0' + Gc
            if len(Bc) == 1:
                Bc = '0' + Bc
            color = Rc + Gc + Bc
            sleep(0.01)
            # self.c.itemconfig(rendomColors[i], fill=color)
            self.c.itemconfig(self.tags[i], fill=color)
            i += 1
            self.c.update()
        sleep(3)
