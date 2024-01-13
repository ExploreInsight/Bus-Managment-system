# from tkinter import *
# import mysql.connector
# from tkinter import messagebox
# from tkcalendar import DateEntry
#
#
# conn = mysql.connector.connect(host="localhost",user="root",password="madhu123",database="emp")
# cur = conn.cursor()
#
#
# def admin0():
#
#     def submit():
#                  # insert# into        # emp.user(username, password, full_name, email, date_of_regestration, contact)# values();
#                  cur.execute(f"insert into emp.user(username,password) values('{user_e.get()}','{password_e.get()}','{name_e.get()}','{email_e.get()}','{dor_e.get()}','{contact_e.get()}')")
#                  conn.commit()
#                  messagebox.showinfo("DONE","Added successfully")
#
#
#     def remove():
#           (cur.execute(f"delete from emp.user where username='{user_e.get()}'"))
#           conn.commit()
#           messagebox.showinfo("Remove Admin",message="Admin Removed.")
#
#
#     root = Tk()
#     # root = Toplevel()
#     root.title("Admin operation")
#     root.geometry("1000x600")
#     user = Label(root,text="Username:")
#     user.pack()
#     user_e = Entry(root,bg="white")
#     user_e.pack()
#     password = Label(root,text="Password:")
#     password.pack()
#     password_e = Entry(root,bg="white")
#     password_e.pack()
#
#     name = Label(root, text="Name:")
#     name.pack()
#     name_e = Entry(root, bg="white")
#     name_e.pack()
#     email = Label(root,text="Email:")
#     email.pack()
#     email_e = Entry(root,bg="white")
#     email_e.pack()
#     dor = Label(root,text="Date of Registration:")
#     dor.pack()
#     dor_e = DateEntry(root,bg="white")
#     dor_e.pack()
#     contact = Label(root,text="Contact:")
#     contact.pack()
#     contact_e = Entry(root,bg="white")
#     contact_e.pack()
#
#     button = Button(root,text="Submit",command=submit,bg="lightgreen")
#     button.pack()
#
#     button0 = Button(root,text="Delete",command=remove,bg="red")
#     button0.pack()
#     root.mainloop()
# admin0()