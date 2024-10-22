from tkinter import *
import add_buses,update_buses,del_buses,search_buses
import tkinter .font as font


def bus_opt(win):

    def fun_bus():
        root.withdraw()
        add_buses.funct2(win)

    def upd_bus():
        root.withdraw()
        update_buses.upd2()

    def sea_bus():
        root.withdraw()
        search_buses.sea2()

    def rem_bus():
        root.withdraw()
        del_buses.dele2()

    root = Toplevel(win)

    root.title("bus Option")
    root.geometry("790x420")
    my_font = font.Font(weight='bold')
    photo = PhotoImage(file='assests/bus_menu.png')
    l1=Label(root,image=photo).pack()

    b1= Button(root,text="Add buses", command=fun_bus, bg='lightgreen')
    b1['font']=my_font
    b1.place(x=345,y=30,width=285,height=65)

    b2= Button(root,text='Update  buses', command=upd_bus, bg='lightgreen')
    b2['font']=my_font
    b2.place(x=345,y=210,width=285,height=65)

    b3= Button(root,text='Delete  buses',command=rem_bus, bg='lightgreen')
    b3['font']=my_font
    b3.place(x=345,y=300,width=285,height=65)

    b4= Button(root,text='Search buses',command=sea_bus, bg='lightgreen')
    b4['font']=my_font
    b4.place(x=345,y=115,width=285,height=65)


    root.mainloop()




