from tkinter import *
from database import get_db
from tkinter import messagebox

def dele2():

    def remove():
        conn = get_db()
        cur = conn.cursor()
        if (delete_entry.get() == ""):
            messagebox.showinfo('user', "Enter the ID :")
        else:
            cur.execute(f"delete from bus where bus_no={delete_entry.get()}")
            conn.commit()
            messagebox.showinfo('user', "Bus Removed Successfully")
        conn.close()

    root = Toplevel()
    root.title("delete_buses")
    root.geometry("800x430")
    photo = PhotoImage(file="assests/del_bus.png")
    p1 = Label(root, image=photo)
    p1.pack()
    delete_entry = Entry(root, bg='white', fg='blue', width=35)
    delete_entry.place(x=420, y=185, height=20)
    delete_button = Button(root, text='REMOVE', font=('arial', 10, 'bold'), command=remove, width=12, bg="red")
    delete_button.place(x=643, y=267, height=30)

    root.mainloop()
