from tkinter import *
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()


def cancel(win):
# def cancel():
    def enter():
        if (login_name.get == ""):
            messagebox.showerror("Error", "Please Enter The Login Name ?")
        else:
            cur.execute(
                f"select start, end, seat_no, route_no, bus_no from emp.booking where login_name='{login_name.get()}'")
            row = cur.fetchone()
            loc.insert(0, row[0])
            det.insert(0, row[1])
            seat_nums = row[2].split(" ")
            seat_nums = seat_nums[0:-1]
            seat.insert(0, ",".join(seat_nums))
            route_no = row[3]
            bus_no = row[4]
            bus.insert(0, bus_no)

            cur.execute(
                f"select dep_time, reach_time from emp.route_duty_allotment where route_no='{route_no}' and bus_no='{bus_no}'")
            row = cur.fetchone()
            dep.insert(0, row[0])
            rec.insert(0, row[1])

            cur.execute(f"select route_distance from emp.routes where route_no='{route_no}'")
            row = cur.fetchone()
            charge_multiplier = 2
            total_charges = int(row[0]) * charge_multiplier
            charges.insert(0, total_charges)

    def cancel_pay():
        cur.execute(f"select * from emp.pay where login_name='{login_name.get()}'")
        row = cur.fetchone()
        print(row)
        if (login_name.get() == ""):
            messagebox.showinfo('user', "Enter the ID :")
        else:
            cur.execute(f"delete from booking where login_name={login_name.get()}")
            conn.commit()
            messagebox.showinfo('user', "employee deleted successfully")



    root = Toplevel()
    # root = Tk()
    root.title("cancel booking")
    root.geometry("810x430")
    photo = PhotoImage(file="assests/cancel_payment.png")
    label = Label(root, image=photo)
    label.pack()

    login_name_l = Label(root, text="1. Login Name:", font=("arial", 14, "bold"), bg="white")
    login_name_l.place(x=250, y=20)
    login_name = Entry(root, width=25, bg="white")
    login_name.place(x=400, y=25)

    b = Button(root, text='Search', command=enter, width=15, bg="blue", font=("arial", 10, "bold"))
    b.place(x=535, y=25, height=19)

    bus_l = Label(root, text="2.Bus No:", font=("arial", 14, "bold"), bg="white")
    bus_l.place(x=250, y=65)
    bus = Entry(root, width=25, bg="white")
    bus.place(x=400, y=70)

    loc_l = Label(root, text="3. Location:", font=("arial", 14, "bold"), bg="white")
    loc_l.place(x=250, y=110)
    loc = Entry(root, width=25, bg="white")
    loc.place(x=400, y=115)

    det_l = Label(root, text="4.Destination:", font=("arial", 14, "bold"), bg="white")
    det_l.place(x=250, y=155)
    det = Entry(root, width=25, bg="white")
    det.place(x=400, y=160)

    charges_l = Label(root, text="5.Departure Date:", font=("arial", 14, "bold"), bg="white")
    charges_l.place(x=250, y=200)
    charges = Entry(root, width=25, bg="white")
    charges.place(x=420, y=205)

    dep_l = Label(root, text="6.Departure Time:", font=("arial", 14, "bold"), bg="white")
    dep_l.place(x=250, y=245)
    dep = Entry(root, width=25, bg="white")
    dep.place(x=430, y=250)

    rec_l = Label(root, text="7.Reaching Time:", font=("arial", 14, "bold"), bg="white")
    rec_l.place(x=250, y=290)
    rec = Entry(root, width=25, bg="white")
    rec.place(x=430, y=295)

    seat_l = Label(root, text="8.Seat No:", font=("arial", 14, "bold"), bg="white")
    seat_l.place(x=250, y=335)
    seat = Entry(root, width=25, bg="white")
    seat.place(x=400, y=340)

    charges_l = Label(root, text="9.Total charges:", font=("arial", 14, "bold"), bg="white")
    charges_l.place(x=250, y=375)
    charges = Entry(root, width=25, bg="white")
    charges.place(x=420, y=385)

    b1 = Button(root, text='Cancel', command=cancel_pay, width=13, bg="red", font=("arial", 12, "bold"))
    b1.place(x=665, y=396, height=30)

    root.mainloop()

# cancel()