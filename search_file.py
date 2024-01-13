
from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
from io import StringIO
import io

conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()

def sea1():

    def view():
        cur.execute(f"select name_emp, father_name,dob,gender,email,phone_no,desiganation,address from add_emp where id_emp='{searchentry.get()}'")
        row = cur.fetchone()
        if row is not None:
            j = 0
            for i in row:
                list[j].set(i)
                j += 1
            show_image()
        else:
            messagebox.showinfo("Not found", "Employee ID does not exist!")

    def show_image():
        print(searchentry.get())
        cur.execute(f"select image from add_emp where id_emp='{searchentry.get()}'")
        r = cur.fetchone()
        if r is not None:
            r = r[0]
            image_path = r
            image = Image.open(image_path)
            image = image.resize((140, 120))
            photo1 = ImageTk.PhotoImage(image)
            photo_label.config(image=photo1)
            photo_label.image = photo1

    root = Toplevel()
    # root = Tk()
    root.title('Search Employee')
    root.geometry('960x515')
    photo = PhotoImage(file='search_emp.png')
    l1 = Label(root, image=photo)
    l1.pack()

    list = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

    searchentry = Entry(root, width=30,bg='white')
    searchentry.place(x=480,y=30)

    search_button = Button(root, text="search",  font=('arial', 10, 'bold'),command=view,bg="blue")
    search_button.place(x=630,y=30,height=18,width=80)

    name_entry = Entry(root,text="emp_name",textvariable=list[0],bg='white',width=30)
    name_entry.place(x=520,y=75)

    father_entry = Entry(root, text="emp_name",textvariable=list[1],bg='white',width=30)
    father_entry.place(x=510,y=120)

    t1= Entry(root, text="emp_name", textvariable=list[2], bg='white', width=30)
    t1.place(x=480, y=165)

    t2= Entry(root, text="emp_name", textvariable=list[3], bg='white', width=30)
    t2.place(x=430, y=215)

    t3 = Entry(root, text="emp_name", textvariable=list[4], bg='white', width=30)
    t3.place(x=435, y=259)

    t4= Entry(root, text="emp_name", textvariable=list[5], bg='white', width=30)
    t4.place(x=500, y=310)

    t5 = Entry(root, text="emp_name", textvariable=list[6], bg="white", width=30)
    t5.place(x=470, y=364)

    t6 = Entry(root, text="emp_name", textvariable=list[7], bg='white', width=30)
    t6.place(x=430, y=410)

    # photo image
    photo_label = Label(root)
    photo_label.place(x=800, y=30)

    # r"c:\Users\Lenovo\Pictures\Saved Pictures\oip.jpg"
    root.mainloop()


# sea1()