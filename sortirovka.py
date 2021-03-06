import asyncio
from decimal import Decimal as Des
from random import choice

from create import *


class InsertionSort(Create):
    def __init__(self, width: int, height: int, kol: int, speed: int, **args):
        super().__init__(width=width, height=height, kol=kol, speed=10, name=args["name"],
                         color_scheme=args["color_scheme"], values=args["values"])
        self.speed = 2
        self.iter = 0

    def sort(self):
        self.c.update()
        for i in range(len(self.height_prym)):
            j = i - 1
            self.iter += 1
            key = self.height_prym[i]
            while self.height_prym[j] > key and j >= 0:
                self.iter += 1
                self.create(j, j + 1)
                self.height_prym[j + 1], self.height_prym[j] = self.height_prym[j], self.height_prym[j + 1]
                self.tags[j + 1], self.tags[j] = self.tags[j], self.tags[j + 1]
                j -= 1
            self.c.itemconfig(self.tags[j + 1], fill=self.colors_scheme[self.all_color][4])
            self.c.update()
            # self.height_prym[j + 1] = key
        super().ranbow()


class AsyncQuickSort(Create):
    def __init__(self, width: int, height: int, kol: int, speed: int, **args):
        super().__init__(width=width, height=height, kol=kol, speed=speed, name=args["name"],
                         color_scheme=args["color_scheme"], values=args["values"])
        self.sleep = 30
        self.iter = 0
        self.rand_colors = ('#D0FF00', '#00FFA9', "#E99105", "#E90084", "#09E2E9")

    async def show1(self, first_place, second_place):
        c = Des(1 / Des((90)))
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
        for i in range(90):
            await asyncio.sleep((1 / (((self.speed) * 10) ** 2)))
            self.c.move(self.tags[first_place], self.width_prym * a * abs(first_place - second_place) * c, 0)
            self.c.move(self.tags[second_place], self.width_prym * b * abs(first_place - second_place) * c, 0)
            self.c.update()
        self.c.itemconfig(self.tags[first_place], fill=precolor1)
        self.c.itemconfig(self.tags[second_place], fill=precolor2)
        self.c.update()

    def sort(self):
        async def partition(nums, start, end):
            tmp_color = choice(self.rand_colors)
            for i in range(start, end + 1):
                self.c.itemconfig(self.tags[i], fill=tmp_color)
            pivotIndex = start
            pivotValue = nums[end]
            for i in range(start, end):
                self.iter += 1
                if nums[i] < pivotValue:
                    nums[i], nums[pivotIndex] = nums[pivotIndex], nums[i]
                    await self.show1(pivotIndex, i)
                    self.tags[i], self.tags[pivotIndex] = self.tags[pivotIndex], self.tags[i]
                    pivotIndex += 1
            nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
            await self.show1(pivotIndex, end)
            self.tags[pivotIndex], self.tags[end] = self.tags[end], self.tags[pivotIndex]
            for i in range(start, end + 1):
                self.c.itemconfig(self.tags[i], fill=self.colors_scheme[self.all_color][1])
            return pivotIndex

        async def quicksort(nums, start, end):
            if start >= end: return
            index = await partition(nums, start, end)
            task1 = asyncio.create_task(quicksort(nums, start, index - 1))
            task2 = asyncio.create_task(quicksort(nums, index + 1, end))
            await asyncio.gather(task1, task2)

        asyncio.run(quicksort(self.height_prym, 0, self.kol - 1))
        self.c.update()
class QuickSort(Create):
    def __init__(self, width: int, height: int, kol: int, speed: int, **args):
        super().__init__(width=width, height=height, kol=kol, speed=speed, name=args["name"],
                         color_scheme=args["color_scheme"], values=args["values"])
        self.speed = speed
        self.iter = 0
        self.rand_colors = ('#D0FF00', '#00FFA9', "#E99105", "#E90084", "#09E2E9")


    def showNoAsync(self, firsr_place, second_place):
        c = Des(1 / Des((90)))
        if firsr_place > second_place:
            right_side = -1
            left_side = 1
        else:
            right_side = 1
            left_side = -1
        precolor1 = self.c.itemcget(self.tags[firsr_place], 'fill')
        precolor2 = self.c.itemcget(self.tags[second_place], 'fill')
        self.c.itemconfig(self.tags[firsr_place], fill=self.colors_scheme[self.all_color][2])
        self.c.itemconfig(self.tags[second_place], fill=self.colors_scheme[self.all_color][3])
        for i in range(90):
            sleep(1 / (self.speed * 30))
            self.c.move(self.tags[firsr_place], self.width_prym * right_side * abs(firsr_place - second_place) * c, 0)
            self.c.move(self.tags[second_place], self.width_prym * left_side * abs(firsr_place - second_place) * c, 0)
            self.c.update()
        self.c.itemconfig(self.tags[firsr_place], fill=precolor1)
        self.c.itemconfig(self.tags[second_place], fill=precolor2)
        self.c.update()

    def sort(self):
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
                    self.showNoAsync(pivotIndex, i)
                    self.tags[i], self.tags[pivotIndex] = self.tags[pivotIndex], self.tags[i]
                    pivotIndex += 1
            nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
            self.showNoAsync(pivotIndex, end)
            self.tags[pivotIndex], self.tags[end] = self.tags[end], self.tags[pivotIndex]
            for i in range(start, end + 1):
                self.c.itemconfig(self.tags[i], fill=self.colors_scheme[self.all_color][1])
            return pivotIndex

        def quicksort(nums, start, end):
            if start >= end: return
            index = partition(nums, start, end)
            quicksort(nums, start, index - 1)
            quicksort(nums, index + 1, end)

        quicksort(self.height_prym, 0, self.kol - 1)
        self.c.update()


class ContingSort(Create):
    def __init__(self, width: int, height: int, kol: int, speed: int, **args):
        super().__init__(width=width, height=height, kol=kol, speed=speed, name=args["name"],
                         color_scheme=args["color_scheme"], values=args["values"])
        self.iter = 0
        self.result = []

    def sort(self):
        self.c.update()
        sleep(3)
        count = [0] * self.width
        for i in self.height_prym:
            self.kol += 1
            count[i] += 1
        self.c.delete(ALL)
        tags = []
        index = 0
        for i in range(len(count)):
            self.kol += 1
            try:
                tags += [self.tags[self.height_prym.index(i)]] * count[i]
                self.result += [i] * count[i]
                for _ in range(count[i]):
                    self.draw(index)
                    index += 1
            except:
                pass
        self.tags = tags
        self.height_prym = self.result

    def draw(self, el):
        sleep(0.01)
        self.tags.append(
            self.c.create_rectangle(el * self.width_prym, self.height, el * self.width_prym + self.width_prym,
                                    self.result[el],
                                    fill=self.colors_scheme[self.all_color][1], activefill="#CB602D"))
        self.c.update()


class BubbleSort(Create):
    def __init__(self, width: int, height: int, kol: int, speed: int, **args):
        super().__init__(width=width, height=height, kol=kol, speed=speed, name=args["name"],
                         color_scheme=args["color_scheme"], values=args["values"])
        self.sleep = 1
        self.iter = 0
        self.flag = True

    def sort(self):
        for i in range(self.kol):
            self.flag = True
            for j in range(self.kol - i - 1):
                self.iter += 1
                if self.height_prym[j] > self.height_prym[j + 1]:
                    self.create(j, j + 1)
                    self.height_prym[j + 1], self.height_prym[j] = self.height_prym[j], self.height_prym[j + 1]
                    self.tags[j + 1], self.tags[j] = self.tags[j], self.tags[j + 1]
                self.c.itemconfig(self.tags[-i - 1], fill=self.colors_scheme[self.all_color][4])


            self.c.update()
        self.c.itemconfig(self.tags[-i - 1], fill=self.colors_scheme[self.all_color][4])