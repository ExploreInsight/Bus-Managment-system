from tkinter import *
import mysql.connector
from tkinter import messagebox, ttk, filedialog
from tkcalendar import DateEntry
conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()


# def custom(win):
def custom():
    def next_page():
        if phone_num.get() == "" or email.get() == "":
            messagebox.showinfo("Search", "Search first!")
            return
        cur.execute(f"select * from emp.customer where login_name='{login_name.get()}'")
        user_registered = cur.fetchone()
        cur.execute(f"SELECT * FROM emp.booking where login_name='{login_name.get()}'")
        user_booked = cur.fetchone()
        if (user_registered is not None and user_booked is None):
            seats = ""
            for i in booked_seats:
                seats += str(i) + " "

            cur.execute(
                f"select route_no from emp.routes where start='{location.get()}' and end='{destination.get()}' and route_name='{route.get()}'")
            rows = cur.fetchall()
            if rows != None:
                row = rows[0]
                route_no = row[0]

                cur.execute(
                    f"insert into emp.booking(login_name, route_name, start, end, seat_no, route_no, bus_no) values('{login_name.get()}', '{route.get()}', '{location.get()}', '{destination.get()}', '{seats}', '{route_no}', '{bus_no.get()}')")
                conn.commit()

                cur.execute(f"select avail_seats from emp.bus where bus_no='{bus_no.get()}'")
                # cur.execute(f"select avail_seats from emp.bus where bus_no='hp 22 072'")
                avail_seats = cur.fetchone()[0].rstrip()
                avail_seats = avail_seats.split(" ")
                selected_seats = seats

                to_remove_seats = seat_no_values
                print(to_remove_seats)

                r_seats = ""
                for i in to_remove_seats:
                    r_seats += str(i) + " "

                cur.execute(f"update emp.bus set avail_seats='{r_seats}' where bus_no='{bus_no.get()}'")
                conn.commit()

                messagebox.showinfo("Data submitted", "Data submitted successfully,Go To Payment")
        else:
            if (user_registered is None):
                messagebox.showinfo("F", "You are not registered!")
            else:
                messagebox.showinfo("Booked", "You have already booked!")

    def combo_btn():
        search = f"select start from routes"
        cur.execute(search)
        data = []
        for row in cur.fetchall():
            data.append(row[0])
        return data

    def get_route():
        nonlocal r_name
        nonlocal data
        nonlocal b_no
        cur.execute(f"select route_name from emp.routes")
        for row in cur.fetchall():
            r_name.append(row[0])

        cur.execute(f"select bus_no from route_duty_allotment")
        for row in cur.fetchall():
            b_no.append(row[0])
        bus_no['values'] = b_no

        route['values'] = r_name
        search1 = f"select end from routes"
        data = []
        cur.execute(search1)
        for row in cur.fetchall():
            data.append(row[0])
        destination['values'] = data

    root = Toplevel()
    # root = Tk()
    root.title("customer details")
    root.geometry("960x510")
    photo = PhotoImage(file="assests/customer_booking.png")
    l1 = Label(root, image=photo).pack()

    label = Label(root, text="Customer Details", bg="white", font=('arial', 13, 'bold'))
    label.place(x=300, y=15)

    login_name_l = Label(root, text="1.login Name:", bg="white", font=('arial', 12, 'bold'))
    login_name_l.place(x=300, y=50)

    login_name = Entry(root, width=25, bg="white")
    login_name.place(x=415, y=50)

    customer_l = Label(root, text="2.Customer Name:", bg="white", font=('arial', 12, 'bold'))
    customer_l.place(x=300, y=100)
    customer = Entry(root, width=25, bg="white")
    customer.place(x=450, y=100)

    num_l = Label(root, text="3.Phone No:", bg="white", font=('arial', 12, 'bold'))
    num_l.place(x=300, y=150)
    phone_num = Entry(root, width=25, bg="white")
    phone_num.place(x=415, y=150)

    email_l = Label(root, text="4.E-Mail:", bg="white", font=('arial', 12, 'bold'))
    email_l.place(x=300, y=200)
    email = Entry(root, width=25, bg="white")
    email.place(x=400, y=200)

    address_l = Label(root, text="5.Address:", bg="white", font=('arial', 12, 'bold'))
    address_l.place(x=300, y=250)
    address = Entry(root, width=25, bg="white")
    address.place(x=400, y=250)

    label = Label(root, text="Booking Details", bg="white", font=('arial', 13, 'bold'))
    label.place(x=625, y=15)

    route_l = Label(root, text="1.Route Name:", bg="white",font=('arial', 12, 'bold'))
    route_l.place(x=625, y=50)
    route = ttk.Combobox(root, width=25)
    r_name = []
    route['values'] = r_name
    route.place(x=750, y=50)

    bus_no_l = Label(root, text="2.Bus No:",bg="white", font=('arial', 12, 'bold'))
    bus_no_l.place(x=625, y=100)
    bus_no = ttk.Combobox(root, width=25)
    b_no = []
    bus_no['values'] = b_no
    bus_no.place(x=750, y=100)

    location_l = Label(root, text="3.Location:",bg="white", font=('arial', 12, 'bold'))
    location_l.place(x=625, y=150)
    location = ttk.Combobox(root, width=25)
    location['values'] = combo_btn()
    location.current()
    location.place(x=750, y=150)

    destination_l = Label(root, text="4.Destination:",bg="white", font=('arial', 12, 'bold'))
    destination_l.place(x=625, y=200)
    destination = ttk.Combobox(root, width=25)
    data = []
    destination['values'] = data
    destination.current()
    destination.place(x=750, y=200)
    get_route()

    depDate_l = Label(root, text="5.Departure Date:",bg="white", font=('arial', 12, 'bold'))
    depDate_l.place(x=625, y=250)
    depDate = DateEntry(root, width=25, bg="white" ,date_pattern="yyyy-mm-dd")
    depDate.place(x=768, y=250)

    seat_l = Label(root, text="6.Seat No:",bg="white", font=('arial', 12, 'bold'))
    seat_l.place(x=625, y=300)
    seat_no = ttk.Combobox(root, width=25, state="disabled")
    seat_no.place(x=750, y=300)
    seat_no_values = []

    def get_seats(e):
        if bus_no.get() != "":
            nonlocal seat_no_values
            seat_no.config(state="normal")
            cur.execute(f"select avail_seats from emp.bus where bus_no='{bus_no.get()}'")
            # cur.execute(f"select avail_seats from emp.bus where bus_no='hp 22 072'")
            avail_seats = cur.fetchone()[0].rstrip()
            avail_seats = avail_seats.split(" ")

            seat_no_values = [int(i) for i in avail_seats]
            seat_no['values'] = seat_no_values
            print(seat_no_values)

    seat_no.set("--select--")
    bus_no.bind("<<ComboboxSelected>>", get_seats)

    selected_seat_no = Listbox(root, width=30)
    selected_seat_no.place(x=750, y=335)
    # for i in range(len()):
    #      seat_no.insert(END,x[i])
    #      seat_no.itemconfig(i)
    y_scroll = ttk.Scrollbar(selected_seat_no, orient='vertical')
    y_scroll.config(command=selected_seat_no.yview)
    selected_seat_no.config(yscrollcommand=y_scroll.set)

    # y_scroll.pack(side='right', fill='y')

    booked_seats = []

    def selected_seat(e):
        val = seat_no.get()
        val = int(val)
        # print(val)
        # print(seat_no_values)
        seat_no_values.remove(val)
        seat_no['values'] = seat_no_values
        seat_no.set("--select--")
        selected_seat_no.insert(END, val)
        booked_seats.append(val)

        print(booked_seats)

    def deselect_seat(e):
        for i in selected_seat_no.curselection():
            sel_val = int(selected_seat_no.get(i))
            selected_seat_no_idx = i
        try:
            val = sel_val
            # val = selected_seat_no.get(0, END).index(val)
            val = selected_seat_no_idx
            selected_seat_no.delete(val)

            seat_no_values.append(sel_val)
            seat_no_values.sort()

            seat_no['values'] = seat_no_values
            seat_no.set("--select--")
            booked_seats.remove(sel_val)

            print(booked_seats)
        except Exception as e:
            print(e)
            # pass

    seat_no.bind("<<ComboboxSelected>>", selected_seat)
    selected_seat_no.bind("<<ListboxSelect>>", deselect_seat)

    def search_customer():
        if login_name.get() != "":
            cur.execute(
                f"SELECT customer_name, phone_no, email, address FROM emp.customer where login_name='{login_name.get()}'")
            row = cur.fetchone()
            if row is not None:
                customer.insert(0, row[0])
                phone_num.insert(0, row[1])
                email.insert(0, row[2])
                address.insert(0, row[3])
            else:
                messagebox.showinfo("Not found", "Username not found!")
        else:
            messagebox.showinfo("?", "Enter username first!")

    b1 = Button(root, text='Search', command=search_customer, width=27, bg="skyblue", font=('arial', 11, 'bold'))
    b1.place(x=300, y=300)

    b2 = Button(root, text='Book', command=next_page, width=27, bg="lightgreen", font=('arial', 11, 'bold'))
    b2.place(x=300, y=350)
    root.mainloop()


# custom()
