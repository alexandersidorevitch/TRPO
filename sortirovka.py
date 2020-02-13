from create import Create,ALL
from decimal import Decimal as des
from time import sleep
from random import choice
import asyncio


class InsertionSort(Create):
    def __init__(self, width: int, height: int, kol: int, **args):
        super().__init__(width, height, kol, args["name"], args["color_scheme"])
        self.sleep = 1
        self.iter = 0

    def sort(self, reverse=False):
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
            self.height_prym[j + 1] = key
        super().ranbow()
        super().show()
        print(self.iter)


class QuickSort(Create):
    def __init__(self, width: int, height: int, kol: int, **args):
        super().__init__(width, height, kol, args["name"], args["color_scheme"])
        self.sleep = 1
        self.iter = 0
        self.rand_colors = ('#D0FF00','#00FFA9',"#E99105","#E90084","#09E2E9")

    async def show1(self, place, place2):
        c = des(1 / des((90 // self.speed)))
        if place > place2:
            a = -1
            b = 1
        else:
            a = 1
            b = -1
        precolor1 = self.c.itemcget(self.tags[place], 'fill')
        precolor2 = self.c.itemcget(self.tags[place2], 'fill')
        self.c.itemconfig(self.tags[place], fill=self.colors_scheme[self.all_color][2])
        self.c.itemconfig(self.tags[place2], fill=self.colors_scheme[self.all_color][3])
        for i in range(90 // self.speed):
            await asyncio.sleep((1 / (((self.speed) * 10) ** 2)))
            self.c.move(self.tags[place], self.width_prym * a * abs(place - place2) * c, 0)
            self.c.move(self.tags[place2], self.width_prym * b * abs(place - place2) * c, 0)
            self.c.update()
        self.c.itemconfig(self.tags[place], fill=precolor1)
        self.c.itemconfig(self.tags[place2], fill=precolor2)
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
        print(self.iter)

    def show2(self, place, place2):
        c = des(1 / des((90 // self.speed)))
        if place > place2:
            a = -1
            b = 1
        else:
            a = 1
            b = -1
        precolor1 = self.c.itemcget(self.tags[place], 'fill')
        precolor2 = self.c.itemcget(self.tags[place2], 'fill')
        self.c.itemconfig(self.tags[place], fill=self.colors_scheme[self.all_color][2])
        self.c.itemconfig(self.tags[place2], fill=self.colors_scheme[self.all_color][3])
        for i in range(90 // self.speed):
            sleep((1 / (((self.speed) * 10) ** 2)))
            self.c.move(self.tags[place], self.width_prym * a * abs(place - place2) * c, 0)
            self.c.move(self.tags[place2], self.width_prym * b * abs(place - place2) * c, 0)
            self.c.update()
        self.c.itemconfig(self.tags[place], fill=precolor1)
        self.c.itemconfig(self.tags[place2], fill=precolor2)
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
                    self.show2(pivotIndex, i)
                    self.tags[i], self.tags[pivotIndex] = self.tags[pivotIndex], self.tags[i]
                    pivotIndex += 1
            nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
            self.show2(pivotIndex, end)
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
        print(self.iter)

class ContingSort(Create):
    def __init__(self, width: int, height: int, kol: int, **args):
        super().__init__(width, height, kol, args["name"], args["color_scheme"])
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
                    index+=1
            except:
                pass
        self.tags = tags
        self.height_prym = self.result
        print(self.kol)
    def draw(self,el):
        sleep(0.05)
        self.tags.append(self.c.create_rectangle(el * self.width_prym, self.height, el * self.width_prym + self.width_prym,
                                self.result[el],
                                fill=self.colors_scheme[self.all_color][1], activefill="#CB602D"))
        self.c.update()
class BubbleSort(Create):
    def __init__(self, width: int, height: int, kol: int, **args):
        super().__init__(width, height, kol, args["name"], args["color_scheme"])
        self.sleep = 1
        self.iter = 0
        self.flag = True

    def changeTimeToCompile(self, speed):
        if speed == 3:
            self.sleep = 7
        elif speed == 2:
            self.sleep = 4
        else:
            self.sleep = 1

    def sort(self):
        for i in range(self.kol):
            self.flag = True
            for j in range(self.kol - i - 1):
                self.iter += 1
                if self.height_prym[j] > self.height_prym[j + 1]:
                    self.height_prym[j + 1], self.height_prym[j] = self.height_prym[j], self.height_prym[j + 1]
                    self.create(j, j + 1)
                    self.tags[j + 1], self.tags[j] = self.tags[j], self.tags[j + 1]
            self.c.itemconfig(self.tags[-i - 1], fill=self.colors_scheme[self.all_color][4])
            self.c.update()
        self.create(1, 1)
        # super().ranbow()
        # super().show()
        print(self.iter)
