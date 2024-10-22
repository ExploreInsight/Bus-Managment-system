from tkinter import *
import mysql.connector
from tkinter import messagebox
import route_allotment

conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()


def funct3(win):

    def submit():
        insert_query = f" INSERT INTO routes (route_no,start,end,route_name) VALUES ('{num.get()}','{start.get()}','{end.get()}','{dis.get()}','{route.get()}')"
        cur.execute(insert_query)
        messagebox.showinfo("Data submitted", "Data submitted successfully")
        conn.commit()

    def next_new():
        route_allotment.allot()

    def clear():
        num.delete(0, END)
        start.delete(0, END)
        end.delete(0, END)
        dis.delete(0, END)

    root = Toplevel()
    root.title("add_routes")
    root.geometry("800x429")
    photo = PhotoImage(file='assests/add_route.png')
    l1 = Label(root, image=photo).pack()
    num_l = Label(root, font=('arial', 16,'bold'), text="1. Route No:",bg="white")
    num_l.place(x=250, y=45)
    num = Entry(root, width=25, bg="white")
    num.place(x=400, y=50)

    route_name_l = Label(root, text="2. Route Name:", bg="white", font=('arial', 16, 'bold'))
    route_name_l.place(x=250, y=95)
    route = Entry(root, width=25, bg="white")
    route.place(x=410, y=100)

    name_l = Label(root, text="3. Location:",bg="white", font=('arial', 16,'bold'))
    name_l.place(x=250, y=145)
    start = Entry(root, width=25, bg="white")
    start.place(x=400, y=150)

    n_l = Label(root, text="4. Destination:",bg="white", font=('arial', 16,'bold'))
    n_l.place(x=250, y=195)
    end = Entry(root, width=25, bg="white")
    end.place(x=400, y=200)
    dis_l= Label(root, text="5. Distance:",bg="white", font=('arial', 16,'bold'))
    dis_l.place(x=250, y=245)
    dis = Entry(root, width=25, bg="white")
    dis.place(x=400, y=250)

    b = Button(root, text="CLEAR ", font=('arial', 10, 'bold'), width=15, command=clear, bg="red")
    b.place(x=250, y=295)

    b1 = Button(root, text="SUBMIT", command=submit,bg="blue",width=15, font=('arial', 10, 'bold'))
    b1.place(x=400,y=295)

    b2 = Button(root, text="NEXT", command=next_new,bg="green",width=15, font=('arial', 10, 'bold'))
    b2.place(x=550, y=295)

    root.mainloop()
