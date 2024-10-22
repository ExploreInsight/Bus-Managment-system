from tkinter import *
import tkinter .font as font

import inquiry
import s_bus
import s_emp
import s_routes


def status(win):
    def one():
        s_emp.emp()

    def two():
        s_bus.buses()

    def three():
        s_routes.s_route()

    def avail():
        inquiry.inquiry1(win)

    root = Toplevel()

    root.geometry("740x420")
    root.title("Options")
    photo = PhotoImage(file="assests/s_o.png")
    image_new = Label(root,image=photo)
    image_new.pack()
    my_font = font.Font(weight='bold')
    b1 = Button(root, text="Employee", command=one, bg='lightgreen')
    b1['font'] = my_font

    b1.place(x=345, y=30, width=285, height=65)

    b2 = Button(root, text='Buses', command=two, bg='lightgreen')
    b2['font'] = my_font
    b2.place(x=345, y=115, width=285, height=65)

    b3 = Button(root, text='Routes', command=three, bg='lightgreen')
    b3['font'] = my_font
    b3.place(x=345, y=210, width=285, height=65)

    b4 = Button(root, text='Avail', command=avail, bg='lightgreen')
    b4['font'] = my_font
    b4.place(x=345, y=300, width=285, height=65)
    root.mainloop()