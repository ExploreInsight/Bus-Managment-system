from tkinter import *
import mysql.connector
from tkinter import messagebox


def upd3():
    def view():
        conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
        cur = conn.cursor()
        cur.execute(
            f"select start,end,route_distance from routes where route_no='{num.get()}'")
        row = cur.fetchone()
        j = 0
        for i in row:
            list[j].set(i)
            j += 1

    def upd():
            conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
            cur = conn.cursor()
            cur.execute(f"update routes SET start='{start.get()}',end='{end.get()}',route_distance='{dis.get()}' where route_no ='{num.get()}'")
            messagebox.showinfo("Updated", 'updated successfully')
            conn.commit()

    root = Toplevel()
    root.title("update routes")
    root.geometry("795x429")
    photo = PhotoImage(file="update_route.png")
    p1 = Label(root,image=photo)
    p1.pack()
    list = [StringVar(), StringVar(), StringVar(), StringVar()]
    num_l = Label(root, font=('arial', 16, 'bold'), text="1. Route No:", bg="white")
    num_l.place(x=250, y=45)
    num = Entry(root, width=25, bg="white")
    num.place(x=400, y=50)
    search_button = Button(root, text="search", font=('arial', 10, 'bold'), command=view, bg="blue")
    search_button.place(x=550, y=50, height=18, width=80)

    route_name_l = Label(root, text="2. Route Name:", bg="white", font=('arial', 16, 'bold'))
    route_name_l.place(x=250, y=95)
    route = Entry(root, width=25, bg="white", textvariable=list[3])
    route.place(x=410, y=100)

    name_l = Label(root, text="3. Location:", bg="white", font=('arial', 16, 'bold'))
    name_l.place(x=250, y=145)
    start = Entry(root, width=25, bg="white",textvariable=list[0])
    start.place(x=400, y=150)
    n_l = Label(root, text="4. Destination:", bg="white", font=('arial', 16, 'bold'))
    n_l.place(x=250, y=195)
    end = Entry(root, width=25, bg="white",textvariable=list[1])
    end.place(x=400, y=200)
    dis_l = Label(root, text="5. Distance:", bg="white", font=('arial', 16, 'bold'))
    dis_l.place(x=250, y=245)
    dis = Entry(root, width=25, bg="white",textvariable=list[2])
    dis.place(x=400, y=250)

    update_button = Button(root, text='UPDATE', bg="lightgreen", width=13, command=upd)
    update_button.place(x=550, y=300, height=30)

    root.mainloop()
