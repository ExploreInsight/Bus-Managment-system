from tkinter import *
import mysql.connector
import next
from tkinter import messagebox
import tkinter.font as f

def new():
    # Get the entered login name and password
    user = login_name.get()
    pass_word = password1.get()

    # Check if login credentials are valid
    if user == "" or pass_word == "":
        messagebox.showinfo('user', "Enter valid details")
    else:
        try:
            # Establish a database connection
            conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
            cur = conn.cursor()

            # Execute a query (replace this with your actual authentication logic)
            query = "SELECT * FROM admin WHERE username = %s AND password = %s"
            cur.execute(query, (user, pass_word))
            result = cur.fetchone()

            if result:
                # If credentials are valid, proceed to the next step
                root.withdraw()
                next.next(root)
                messagebox.showinfo('Info', 'Login Successfully')
            else:
                messagebox.showinfo('Info', 'Invalid Login Credentials')

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            cur.close()
            conn.close()

root = Tk()
root.title("Bus Management System")
root.geometry("1020x540")
myFont = f.Font(weight="bold")
photo = PhotoImage(file='start2.png')
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