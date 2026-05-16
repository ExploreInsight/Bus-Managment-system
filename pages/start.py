from tkinter import *
from database import get_db
import next
from tkinter import messagebox
import tkinter.font as f

def new():
    user = login_name.get()
    pass_word = password1.get()

    if user == "" or pass_word == "":
        messagebox.showinfo('user', "Enter valid details")
    else:
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (user, pass_word))
            result = cur.fetchone()

            if result:
                root.withdraw()
                next.next(root)
                messagebox.showinfo('Info', 'Login Successfully')
            else:
                messagebox.showinfo('Info', 'Invalid Login Credentials')

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cur.close()
            conn.close()

root = Tk()
root.title("Bus Management System")
root.geometry("1020x540")
myFont = f.Font(weight="bold")
photo = PhotoImage(file='assests/start2.png')
l3 = Label(root, image=photo)
l3.pack()

login_name = Entry(root, width=46)
login_name.place(x=587, y=294, width=225, height=38)

password1 = Entry(root, show='*', width=35)
password1.place(x=589, y=375, width=223, height=38)

b1 = Button(root, text='Login', width=21, height=2, command=new, bg="skyblue")
b1["font"] = myFont
b1.place(x=590, y=435, height=37)

root.mainloop()
