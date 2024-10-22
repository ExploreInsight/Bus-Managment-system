from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from tkinter import filedialog

def upd1():

    def view():
        conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
        cur = conn.cursor()
        cur.execute(
            f"select name_emp, father_name,dob,gender,email,phone_no,desiganation,address from add_emp where id_emp={updateentry.get()}")
        row = cur.fetchone()
        j = 0
        for i in row:
            list[j].set(i)
            j += 1

    global_img_path = ""
    def select_image():
        nonlocal global_img_path
        img = filedialog.askopenfilename()
        image1 = Image.open(img)
        image0_resized = image1.resize((118, 100))
        photo0 = ImageTk.PhotoImage(image0_resized)
        photo_label.config(image=photo0)
        photo_label.image = photo0
        global_img_path = img

    def upd():
        conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
        cur = conn.cursor()
        cur.execute(
            f"update add_emp SET name_emp='{update_name.get()}', father_name='{update_father.get()}',dob='{t1.get()}',gender='{t2.get()}',email='{t3.get()}',phone_no='{t4.get()}',desiganation='{t5.get()}',address='{t6.get()}',image='{global_img_path}' where id_emp ='{updateentry.get()}'")
        messagebox.showinfo("Updated", 'updated successfully')
        conn.commit()

    root = Toplevel()
    root.title('Update Employee')
    root.geometry('910x480')
    photo = PhotoImage(file='assests/update_emp.png')
    l1 = Label(root, image=photo)
    l1.pack()
    list = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

    updateentry = Entry(root, bg='white',  width=35)
    updateentry.place(x=450, y=28)
    search_button = Button(root, text="search", command=view,bg="blue",font='bold')
    search_button.place(x=600, y=28, height=18, width=80)

    update_name = Entry(root, bg='white',  width=35,textvariable=list[0])
    update_name.place(x=490, y=73)

    update_father = Entry(root, bg='white',  width=35,textvariable=list[1])
    update_father.place(x=480, y=113)

    t1 = DateEntry(root, text="emp_name", bg='white', width=30,textvariable=list[2])
    t1.place(x=460, y=160)

    t2 = Entry(root, text="emp_name", bg='white', width=30,textvariable=list[3] )
    t2.place(x=400, y=200)
    # var = StringVar(value='M')
    # t2 =Radiobutton(root, text='Male', variable=var, value='M',width='5', bg='white').place(x=400, y=200)
    # t2= Radiobutton(root, text='Female', variable=var, value='F', width='6', bg='white',textvariable=list[3]).place(x=500, y=200)

    t3 = Entry(root, text="emp_name", bg='white',fg='blue', width=30,textvariable=list[4])
    t3.place(x=410, y=250)

    t4 = Entry(root, text="emp_name", bg='white', width=30,textvariable=list[5])
    t4.place(x=478, y=293)

    t5 = ttk.Combobox(root, text="emp_name", width=30,textvariable=list[6])
    t5['values'] = ("Driver", "Conductor")
    t5.current(newindex=1)
    t5.place(x=450, y=345)

    image_path = r"c:\Users\Lenovo\Pictures\Saved Pictures\oip.jpg"
    image = Image.open(image_path)
    image_resized = image.resize((118, 100))
    photo0 = ImageTk.PhotoImage(image_resized)
    photo_label = Label(root, image=photo0)
    photo_label.place(x=750, y=30)

    photo_button = Button(root, text='SELECT PHOTO', width=14, font=('arial', 10, 'bold'), bg="blue", command=select_image)
    photo_button.place(x=750, y=130)

    t6 = Entry(root, text="emp_name", bg='white', width=30,textvariable=list[7])
    t6.place(x=410, y=390)

    update_button = Button(root, text='UPDATE', command=upd, bg="lightgreen",width=11,font="bold")
    update_button.place(x=794, y=446, height=30)

    root.mainloop()


