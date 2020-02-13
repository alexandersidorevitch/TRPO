# from tkinter import *
import colorsys
# from time import sleep
# root = Tk()
# height = int(root.winfo_screenheight()-500)
# width = int(root.winfo_screenwidth()-500)
# root.geometry(
#     '{}x{}+{}+{}'.format(width, height, (root.winfo_screenwidth() - width-100) // 2,
#                          (root.winfo_screenheight() - height-100) // 2))
# root.resizable(False, False)
# can = Canvas(root,height=height, width=width, bg="white")
# kvadr = can.create_rectangle(100,100,200,200,fill='green')
# kvadr2 = can.create_rectangle(200,100,300,200,fill='blue')
# can.pack()
# can.update()
# sleep(4)
# speed = 0.9
# a = 1/60
# for i in range(60):
#     sleep(1/((speed*10)**2))
#     can.move(kvadr,100*a,0)
#     can.move(kvadr2,-100*a,0)
#     can.update()
# root.mainloop()
kol = 10
ran = (int(i)/100000 for i in range(0,100000,100000//kol))
for hue in ran:
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    Rc = "#"+str(hex(R))[2:]
    Gc = str(hex(G))[2:]
    Bc = str(hex(B))[2:]
    if Rc == "#0":
        Rc = "#00"
    if Gc == "0":
        Gc = "00"
    if Bc == "0":
        Bc = "00"
    color = Rc+Gc+Bc
