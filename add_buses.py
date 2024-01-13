from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry

conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()


def funct2(win):
    def submit():
        total_seats = no.get()
        avail_seats = ""
        for i in range(int(total_seats)):
            avail_seats += f"{i+1} "
        insert_query = f" INSERT INTO bus (bus_no,bus_name,no_of_seats,model_no,purchase_date,purchase_cost, avail_seats) VALUES ('{num.get()}','{name.get()}','{no.get()}','{m_num.get()}','{purch_date.get()}','{purch_cost.get()}', '{avail_seats}')"
        cur.execute(insert_query)

        messagebox.showinfo("Data submitted", "Data submitted successfully")
        conn.commit()

    def clear():
        num.delete(0, END)
        m_num.delete(0, END)
        name.delete(0, END)
        no.delete(0, END)
        purch_date.delete(0, END)
        purch_cost.delete(0, END)

    root = Toplevel()
    root.title("Add_buses")
    root.geometry("860x460")
    photo = PhotoImage(file='add_bus.png')
    l1 = Label(root, image=photo)
    l1.pack()

    num_l = Label(root, font=('arial', 16, 'bold'), text="1. Bus No:", bg="white")
    num_l.place(x=300, y=25)
    num = Entry(root, width=25, bg="white")
    num.place(x=420, y=32)
    m_num_l = Label(root, font=('arial', 16, 'bold'), text="2.Model No:", bg="white")
    m_num_l.place(x=300, y=90)
    m_num = Entry(root, width=25, bg="white")
    m_num.place(x=430, y=97)



    name_l = Label(root, font=('arial', 16, 'bold'), text="3.Name Of bus:", bg="white")
    name_l.place(x=300, y=155)
    name = Entry(root, width=25, bg="white")
    name.place(x=460, y=162)

    n_l = Label(root, font=('arial', 16, 'bold'), text="4.Number Of Seats:", bg="white")
    n_l.place(x=300, y=220)
    no = Entry(root, width=25, bg="white")
    no.place(x=500, y=227)

    purch_date_l = Label(root, font=('arial', 16, 'bold'), text="5.Purchase Date:", bg="white")
    purch_date_l.place(x=300, y=285)
    purch_date = DateEntry(root, width=25, text="Purchase Date:", bg="white", date_pattern="yyyy-mm-dd")
    purch_date.place(x=490, y=292)

    purch_cost_l = Label(root, font=('arial', 16, 'bold'), text="6.Purchase Cost:", bg="white")
    purch_cost_l.place(x=300, y=350)
    purch_cost = Entry(root, width=25, text="Purchase Cost:", bg="white")
    purch_cost.place(x=490, y=357)

    b1 = Button(root, text="SUBMIT ", font=('arial', 10, 'bold'), command=submit, bg="blue",width=10)
    b1.place(x=758, y=425)

    b2 = Button(root, text="CLEAR ", font=('arial', 10,"bold"), command=clear, bg="red",width=10)
    b2.place(x=650, y=425)

    root.mainloop()


