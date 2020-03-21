from math import sin, cos, pi, ceil
from tkinter import *

root = Tk()
root.geometry("600x500+300+200")
c = Canvas(root, height=600, width=500)
c.pack()
x1, y1, x2, y2 = 100, 100, 300, 300
x0, y0 = x1 + abs(x2 - x1) / 2, y1 + abs(y2 - y1) / 2
r = (x2 - x1) / 2
c.create_oval(x1, y1, x2, y2)
c.create_line(x0, y0, x0, y1)
corner = 0
q = 0
colors = ['white', "black", "#222222", "#333333", "#555555", "red"]
World = int(input())
countries = [int(i) for i in input().split()]
for i in countries:
    c.create_line(x0, y0, x0 + (r * (sin(2 * i / World * pi + corner))), y0 - (r * cos(2 * i / World * pi + corner)))
    c.update()
    # c.create_arc(x1, y1, x2, y2, start=corner,
    #              extent=-2 * i / World * 180 - corner, outline=colors[q], fill=colors[q], width=2)
    # c.update()
    q += 1
    corner += 2 * i / World * pi
    print(ceil(1000 * i / World) / 10, "%", end=" ")
root.mainloop()
