from tkinter import *
import mysql.connector
from tkinter import messagebox


def dele3():
    def remove():
        conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
        cur = conn.cursor()
        if (delete_entry.get() == ""):
            messagebox.showinfo('user', "Enter the ID :")
        else:
            cur.execute(f"delete from routes where route_no={delete_entry.get()}")
            conn.commit()
            messagebox.showinfo('user', "Route Deleted Successfully")

    # root = Tk()
    root = Toplevel()
    root.title("delete_buses")
    root.geometry("800x430")
    photo = PhotoImage(file="assests/del_route.png")
    p1 = Label(root, image=photo)
    p1.pack()
    delete_entry = Entry(root, bg='white', fg ='blue', width=35)
    delete_entry.place(x=438, y=180, height=20)
    delete_button = Button(root, text='REMOVE', font=('arial', 10, 'bold'), command=remove, width=12, bg="red")
    delete_button.place(x=647, y=264, height=30)

    root.mainloop()
