from tkinter import *


def eventHandler(event):  # Обрабатываем точку клика
    canvas.unbind("<Button-1>")
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y
    if mouseX < 30: mouseX = 30  # Ограничиваем перемещение по X
    if mouseY < 30: mouseY = 30  # и по Y
    moveBall()


def moveBall():
    x, y = canvas.coords(ball)[2], canvas.coords(ball)[3]  # Координаты шара
    x = {
        x < mouseX: 1,
        x == mouseX: 0,
        x > mouseX: -1
    }[True]  # Сдвиг по X
    y = {
        y < mouseY: 1,
        y == mouseY: 0,
        y > mouseY: -1
    }[True]  # Сдвиг по Y
    canvas.move("smile", x, y)  # Двигаем в нужном направлении
    if canvas.coords(ball)[2] != mouseX or canvas.coords(ball)[3] != mouseY:
        root.after(10, moveBall)
    else:
        canvas.bind('<Button-1>', eventHandler)


root = Tk()
mouseX, mouseY = None, None

canvas = Canvas(root, width=500, height=500, bg="white")

ball = canvas.create_oval((5, 5), (35, 35), fill="yellow", outline="yellow", tag="smile")
canvas.create_arc((15, 15), (25, 25), style=ARC, start=210, extent=120, tag="smile")
canvas.create_line((15, 15), (16, 16), tag="smile")
canvas.create_line((25, 15), (26, 16), tag="smile")

canvas.bind('<Button-1>', eventHandler)

canvas.pack()

root.mainloop()