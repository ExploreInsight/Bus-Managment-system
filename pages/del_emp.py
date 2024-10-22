from tkinter import *
import mysql.connector
from tkinter import messagebox


def dele1():

    def remove():
        conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
        cur = conn.cursor()
        if(delete_entry.get()==""):
            messagebox.showinfo('user', "Enter the ID :")
        else:
            cur.execute(f"delete from add_emp where id_emp={delete_entry.get()}")
            conn.commit()
            messagebox.showinfo('user', "employee deleted successfully")

    root = Toplevel()
    root.title('Delete Employee')
    root.geometry('800x429')
    photo = PhotoImage(file='assests/delete_emp.png')
    l1 = Label(root, image=photo).pack()

    delete_entry = Entry(root,bg='white',fg='blue',width=35)
    delete_entry.place(x=500,y=190,height=20)
    delete_button = Button(root,text='REMOVE',font=('arial',10,'bold'),command=remove,width=12,bg="red")
    delete_button.place(x=632,y=272,height=30)

    root.mainloop()
