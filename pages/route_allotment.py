from tkinter import *
from database import get_db
from tkinter import messagebox
from tkinter import ttk


def allot():
    def submit():
        conn = get_db()
        cur = conn.cursor()
        insert_query = f" INSERT INTO route_duty_allotment (route_no,dep_time,reach_time,bus_no,id_emp) VALUES ('{num.get()}','{dep.get()}','{rec.get()}','{bus.get()}','{id.get()}')"
        cur.execute(insert_query)
        conn.commit()
        messagebox.showinfo("Data submitted", "Route Successfully Allotted")
        conn.close()

    def show_info():
        conn = get_db()
        cur = conn.cursor()
        nonlocal emp_ids
        nonlocal route_nums
        nonlocal bus_nums
        
        cur.execute(f"select id_emp from add_emp")
        rows = cur.fetchall()
        for i in rows:
            emp_ids.append(i[0])

        cur.execute(f"select route_no from routes")
        rows = cur.fetchall()
        for i in rows:
            route_nums.append(i[0])

        bus_nums = []
        cur.execute(f"select bus_no from bus")
        rows = cur.fetchall()
        for i in rows:
            bus_nums.append(i[0])

        id['values'] = emp_ids
        num['values'] = route_nums
        bus['values'] = bus_nums
        conn.close()

    root = Toplevel()
    root.title("route_allotment")
    root.geometry("800x425")
    photo = PhotoImage(file='assests/allotment.png')
    l1 = Label(root, image=photo).pack()
    num_l = Label(root, text="1.Route No:", font=('arial', 16, 'bold'),bg="white")
    num_l.place(x=250, y=25)
    num = ttk.Combobox(root, width=25)
    route_nums = []
    num['values'] = route_nums
    num.place(x=373, y=30)
    name_l = Label(root, text="2.Bus No:", font=('arial', 16, 'bold'),bg="white")
    name_l.place(x=250, y=80)
    bus = ttk.Combobox(root, width=25)
    bus_nums = []
    bus['values'] = bus_nums
    bus.place(x=355, y=87)
    id_l= Label(root, text="3.Employee ID:", font=('arial', 16, 'bold'),bg="white")
    id_l.place(x=250, y=145)
    id= ttk.Combobox(root, width=25)
    emp_ids = []
    show_info()
    id['values'] = emp_ids
    id.place(x=410, y=152)
    dep_l = Label(root, text="4.Departure Time:", font=('arial', 16, 'bold'),bg="white")
    dep_l.place(x=250, y=210)
    dep = Entry(root, width=25, bg="white")
    dep.place(x=440, y=217)
    rec_l = Label(root, text="5.Reaching Time:", font=('arial', 16, 'bold'),bg="white")
    rec_l.place(x=250, y=275)
    rec = Entry(root, width=25, bg="white")
    rec.place(x=430, y=282)
    b1 = Button(root, text="SUBMIT", command=submit, font=('arial', 16, 'bold'),bg="blue",width=11)
    b1.place(x=550, y=340,height=35)

    root.mainloop()
