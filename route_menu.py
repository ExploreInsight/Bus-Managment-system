from tkinter import *
import addroutes,update_routes,del_routes,search_routes
import tkinter .font as font


def route_menu(win):

    def fun_route():
        addroutes.funct3(win)

    def upd_route():
        update_routes.upd3()

    def sea_route():
        search_routes.sea3()

    def rem_route():
        del_routes.dele3()

    root = Toplevel(win)

    root.title("bus Option")
    root.geometry("766x420")
    my_font = font.Font(weight='bold')
    photo = PhotoImage(file='route_menu.png')
    l1=Label(root,image=photo).pack()

    b1= Button(root,text="Add routes", command=fun_route, bg='lightgreen')
    b1['font']=my_font
    b1.place(x=345,y=30,width=285,height=65)

    b2= Button(root,text='Update  routes', command=upd_route, bg='lightgreen')
    b2['font']=my_font
    b2.place(x=345,y=210,width=285,heigh=65)
    b3= Button(root,text='Delete  routes',command=rem_route, bg='lightgreen')
    b3['font']=my_font
    b3.place(x=345,y=300,width=285,height=65)

    b4= Button(root,text='Search routes',command=sea_route, bg='lightgreen')
    b4['font']=my_font
    b4.place(x=345,y=115,width=285,height=65)


    root.mainloop()

