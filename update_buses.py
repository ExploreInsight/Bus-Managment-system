from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry


def upd2():
    def view():
        conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
        cur = conn.cursor()
        cur.execute(
            f"select model_no,bus_name,no_of_seats,purchase_date,purchase_cost from bus where bus_no='{num.get()}'")
        row = cur.fetchone()
        j = 0
        for i in row:
            list[j].set(i)
            j += 1

    def update():
            conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
            cur = conn.cursor()
            cur.execute(
                f"update bus SET model_no ='{m_num.get()}',bus_name='{name.get()}',no_of_seats='{no.get()}',purchase_date='{purch_date.get()}',purchase_cost='{purch_cost.get()}' where bus_no ='{num.get()}'")
            messagebox.showinfo("Updated", 'updated successfully')
            conn.commit()

    root = Toplevel()
    root.title("update_buses")
    root.geometry("860x460")
    photo = PhotoImage(file="update_bus.png")
    p1 = Label(root, image=photo)
    p1.pack()

    list = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

    num_l = Label(root, font=('arial', 16, 'bold'), text="1. Bus No:", bg="white")
    num_l.place(x=300, y=25)
    num = Entry(root, width=25, bg="white")
    num.place(x=420, y=32)
    search_button = Button(root, text="search", font=('arial', 10, 'bold'), command=view, bg="blue")
    search_button.place(x=550, y=32, height=18, width=80)

    m_num_l = Label(root, font=('arial', 16, 'bold'), text="2.Model No:", bg="white")
    m_num_l.place(x=300, y=90)
    m_num = Entry(root, width=25, bg="white", textvariable=list[0])
    m_num.place(x=430, y=97)

    name_l = Label(root, font=('arial', 16, 'bold'), text="3.Name Of bus:", bg="white")
    name_l.place(x=300, y=155)
    name = Entry(root, width=25, bg="white", textvariable=list[1])
    name.place(x=460, y=162)

    n_l = Label(root, font=('arial', 16, 'bold'), text="4.Number Of Seats:", bg="white")
    n_l.place(x=300, y=220)
    no = Entry(root, width=25, bg="white", textvariable=list[2])
    no.place(x=505, y=227)

    purch_date_l = Label(root, font=('arial', 16, 'bold'), text="5.Purchase Date:", bg="white")
    purch_date_l.place(x=300, y=285)
    purch_date = DateEntry(root, width=25, text="Purchase Date:", bg="white", textvariable=list[3], date_pattern="yyyy-mm-dd")
    purch_date.place(x=490, y=292)

    purch_cost_l = Label(root, font=('arial', 16, 'bold'), text="6.Purchase Cost:", bg="white")
    purch_cost_l.place(x=300, y=350)
    purch_cost = Entry(root, width=25, text="Purchase Cost:", bg="white", textvariable=list[4])
    purch_cost.place(x=490, y=357)

    update_button = Button(root, text='UPDATE', command=update, bg="lightgreen", width=13)
    update_button.place(x=740, y=420, height=30)

    root.mainloop()
