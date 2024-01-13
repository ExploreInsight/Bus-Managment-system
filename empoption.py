from tkinter import *
import emp, upd_emp, search_file, del_emp
import tkinter .font as font


def func(win):

    def fun():
        root.withdraw()
        emp.funct(win)

    def upd():
        root.withdraw()
        upd_emp.upd1()

    def sea():
        root.withdraw()
        search_file.sea1()

    def rem():
        root.withdraw()
        del_emp.dele1()

    root = Toplevel(win)

    root.title("Emp Option")
    root.geometry("720x412")
    my_font = font.Font(weight='bold')
    photo = PhotoImage(file='emp_opt.png')
    l1=Label(root,image=photo).pack()

    b1= Button(root,text='Add Employee', command=fun,bg='lightgreen')
    b1['font']=my_font
    b1.place(x=315,y=30,width=285,height=65)

    b2= Button(root,text='Update Employee', command=upd, bg='lightgreen')
    b2['font']=my_font
    b2.place(x=315,y=210,width=285,height=65)

    b3= Button(root,text='Delete Employee',command=rem, bg='lightgreen')
    b3['font']=my_font
    b3.place(x=315,y=300,width=285,height=65)

    b4= Button(root,text='Search Employee',command=sea, bg='lightgreen')
    b4['font']=my_font
    b4.place(x=315,y=115,width=285,height=65)


    root.mainloop()

