from tkinter import *
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()


def custom0(win):
# def custom0():
    registered = False
    def submit():
        if(login_name.get()!=''):
            cur.execute(f"select * from emp.customer where login_name='{login_name.get()}'")
            if (cur.fetchone()==None):
                if(customer.get()!='' and phone_num.get()!='' and email.get()!='' and address.get()!=''):
                    nonlocal registered
                    insert_query = f"INSERT INTO customer (login_name,customer_name,phone_no,email,address) VALUES ('{login_name.get()}','{customer.get()}','{phone_num.get()}','{email.get()}','{address.get()}')"
                    cur.execute(insert_query)
                    conn.commit()
                    messagebox.showinfo("Yes", "You are registered, now you can start booking!")
                    registered = True
                else:
                    messagebox.showinfo("Nope", "Input fields must not be empty like your brain!")
            else:
                messagebox.showinfo("Go", "You are already registered, go to booking page!")
                registered = True
        else:
            messagebox.showinfo("Nope", "Input fields must not be empty like your brain!")

    def go():
        import customer
        customer.custom()

    # root = Tk()
    root = Toplevel()
    root.geometry("860x460")
    root.title("customer Registration")
    photo = PhotoImage(file="customer_reg.png")
    label = Label(root,image=photo)
    label.pack()
    # label = Label(root, text="Customer Details")
    # label.place(x=350, y=15)

    login_name_l = Label(root, text="1. Login Name:",bg="white",font=("arial",14,"bold"))
    login_name_l.place(x=280, y=20)

    login_name = Entry(root, width=25, bg="white")
    login_name.place(x=430, y=25)

    customer_l = Label(root, text="2. Customer Name:",font=("arial",14,"bold"),bg="white")
    customer_l.place(x=280, y=65)
    customer = Entry(root, width=25, bg="white")
    customer.place(x=470, y=70)

    num_l = Label(root, text="3. Phone No. :",font=("arial",14,"bold"),bg="white")
    num_l.place(x=280, y=110)
    phone_num = Entry(root, width=25, bg="white")
    phone_num.place(x=425, y=120)

    email_l = Label(root, text="4.E-Mail:",font=("arial",14,"bold"),bg="white")
    email_l.place(x=280, y=155)
    email = Entry(root, width=25, bg="white",fg="blue")
    email.insert(END,"@gmail.com")
    email.place(x=375, y=160)

    address_l = Label(root, text="5.Address:",font=("arial",14,"bold"),bg="white")
    address_l.place(x=280, y=200)
    address = Entry(root, width=25, bg="white")
    address.place(x=395, y=205)

    button = Button(root,text="Go To Booking",command=go,width=17,bg="blue",font=("arial",12,"bold"))
    button.place(x=280, y=310,height=30)

    b1 = Button(root, text='Register', command=submit,width=17, bg="skyblue",font=("arial",12,"bold"))
    b1.place(x=280, y=260,height=30)

    root.mainloop()
# custom0()






