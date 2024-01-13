from tkinter import *
import empoption,busopt,customer_reg,cancel_payment,status_opt
import tkinter .font as font
from PIL import ImageTk,Image

import payment
import route_menu


def next(win):
# def next():
    def fun():
        empoption.func(win)

    def bus():
        busopt.bus_opt(win)

    def route():
        route_menu.route_menu(win)

    def customer_1():
        customer_reg.custom0(win)

    def pay():
        payment.pay_ment(win)

    def cancel():
        cancel_payment.cancel(win)

    def inquiry0():
        status_opt.status(win)

    root = Toplevel()
    # root =  Tk()
    root.title("Bus Management System")
    root.geometry("885x612")
    myFont = font.Font(weight='bold')
    photo= PhotoImage(file='dashboard.png')
    l1 = Label(root,image=photo).pack()

    image_path0 = r"em.jpeg"
    image = Image.open(image_path0)
    resized0 = image.resize((138,95))
    p0 = ImageTk.PhotoImage(resized0)
    l0 = Label(root,image=p0)
    l0.place(x=475,y=80)

    b1= Button(root,text='Employee', width=13, command=fun, bg='lightgreen')
    b1['font']=myFont
    b1. place(x=475,y=160)

    image_path5 = r"bus.jpeg"
    image = Image.open(image_path5)
    resized1 = image.resize((138,95))
    p = ImageTk.PhotoImage(resized1)
    l1 = Label(root,image=p)
    l1.place(x=680,y=80)

    b2= Button(root,text='Buses', width=13,bg='lightgreen',command=bus)
    b2['font']=myFont
    b2.place(x=680,y=160)

    image_path2 = r"routes.jpeg"
    image = Image.open(image_path2)
    resized2 = image.resize((138,95))
    p2 = ImageTk.PhotoImage(resized2)
    l2 = Label(root,image=p2)
    l2.place(x=475,y=205)

    b3= Button(root,text='Routes', width=13,bg='lightgreen',command=route)
    b3['font']=myFont
    b3.place(x=475,y=290)

    image_path6 = r"book.jpeg"
    image6 = Image.open(image_path6)
    resized6 = image6.resize((138,90))
    p6 = ImageTk.PhotoImage(resized6)
    l6 = Label(root,image=p6)
    l6.place(x=680,y=205)

    b5= Button(root,text='Booking', width=13,bg='lightgreen',command=customer_1)
    b5['font']=myFont
    b5.place(x=680,y=290)

    image_path3 = r"payment.jpeg"
    image = Image.open(image_path3)
    resized3 = image.resize((138,95))
    p3 = ImageTk.PhotoImage(resized3)
    l3 = Label(root,image=p3)
    l3.place(x=475,y=340)
    b6= Button(root,text='Payment', width=13,bg='lightgreen',command=pay)
    b6['font']=myFont
    b6.place(x=475,y=435)

    image_path4 = r"cancel.jpeg"
    image = Image.open(image_path4)
    resized4 = image.resize((138,95))
    p4 = ImageTk.PhotoImage(resized4)
    l4 = Label(root,image=p4)
    l4.place(x=680,y=340)
    b7= Button(root,text='Cancel Booking', width=13,bg='lightgreen',command=cancel)
    b7['font']=myFont
    b7.place(x=680,y=435)

    image_path7 = r"status.jpeg"
    image7 = Image.open(image_path7)
    resized7 = image7.resize((138,90))
    p7 = ImageTk.PhotoImage(resized7)
    l7 = Label(root,image=p7)
    l7.place(x=475,y=480)

    b8= Button(root,text='Status', width=13,bg='lightgreen',command=inquiry0)
    b8['font']=myFont
    b8.place(x=475,y=570)

    root.mainloop()
# next()