from tkinter import *
from database import get_db
from tkinter import messagebox
from tkcalendar import DateEntry


def admin0():

    def submit():
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"insert into user(username, password, full_name, email, date_of_registration, contact) values('{user_e.get()}','{password_e.get()}','{name_e.get()}','{email_e.get()}','{dor_e.get()}','{contact_e.get()}')")
        conn.commit()
        conn.close()
        messagebox.showinfo("DONE","Added successfully")


    def remove():
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"delete from user where username='{user_e.get()}'")
        conn.commit()
        conn.close()
        messagebox.showinfo("Remove Admin",message="Admin Removed.")


    root = Tk()
    root.title("Admin operation")
    root.geometry("1000x600")
    user = Label(root,text="Username:")
    user.pack()
    user_e = Entry(root,bg="white")
    user_e.pack()
    password = Label(root,text="Password:")
    password.pack()
    password_e = Entry(root,bg="white")
    password_e.pack()

    name = Label(root, text="Name:")
    name.pack()
    name_e = Entry(root, bg="white")
    name_e.pack()
    email = Label(root,text="Email:")
    email.pack()
    email_e = Entry(root,bg="white")
    email_e.pack()
    dor = Label(root,text="Date of Registration:")
    dor.pack()
    dor_e = DateEntry(root,bg="white")
    dor_e.pack()
    contact = Label(root,text="Contact:")
    contact.pack()
    contact_e = Entry(root,bg="white")
    contact_e.pack()

    button = Button(root,text="Submit",command=submit,bg="lightgreen")
    button.pack()

    button0 = Button(root,text="Delete",command=remove,bg="red")
    button0.pack()
    root.mainloop()
