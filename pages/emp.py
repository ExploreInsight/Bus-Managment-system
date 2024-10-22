from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
if conn.is_connected():
    print("connection established")
else:
    print("connection failed")
cur = conn.cursor()
cur.execute("SHOW tables")
for x in cur:
    print(x)


def funct(win):
    global_img_path = ""
    def select_image():
            nonlocal global_img_path
            img = filedialog.askopenfilename()
            image1 = Image.open(img)
            image0_resized = image1.resize((100, 100))
            photo0 = ImageTk.PhotoImage(image0_resized)
            photo_label.config(image=photo0)
            photo_label.image = photo0
            global_img_path = img

    def validate_email():
        email = t5.get()
        if "@" and "." in email:
            messagebox.showinfo("valid","Email Identified")
        else:
            messagebox.showwarning("Warning","Input valid Email Format")

    def submit():
        name_emp = t2.get()
        father_name = t3.get()
        dob = t4.get()
        email = t5.get()
        validate_email()
        gender = var.get()
        phone_no = t6.get()
        marital_status = t7.get()
        address = t8.get()
        insert_query = f"INSERT INTO add_emp (name_emp,father_name,dob,email,gender,phone_no,desiganation,address, image) VALUES ('{name_emp}','{father_name}','{dob}','{email}','{gender}','{phone_no}','{marital_status}','{address}', '{global_img_path}') "
        cur.execute(insert_query)
        messagebox.showinfo("Data submitted","Data submitted successfully")
        conn.commit()

    def clear():
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)
        t7.delete(0, END)
        t8.delete(0, END)

    root = Toplevel(win)
    root.title("Employee registration")
    root.geometry("833x504")
    photo1 = PhotoImage(file="emp_reg.png")
    l1 = Label(root, image=photo1)
    l1.place(x=0,y=0)
    t1 = Entry(root,width='25',bg='white')
    t1.place(x=485,y=38)
    t2 = Entry(root, width='25', bg='white')
    t2.place(x=520, y=87)
    t3 = Entry(root, width='25', bg='white')
    t3.place(x=490, y=134)
    t4 = DateEntry(root, width='25', bg='white', date_pattern="yyyy-mm-dd")
    t4.place(x=495, y=175)
    t5 = Entry(root, width='25', bg='white')
    t5.place(x=450, y=265)
    t6 = Entry(root, width='25', bg='white')
    t6.place(x=518, y=318)
    t7 = ttk.Combobox(root, width='25')
    t7['values'] = ("Driver", "Conductor")
    t7.current(newindex=1)
    t7.place(x=484, y=365)

    var = StringVar(value='M')
    Radiobutton(root, text='Male', variable=var, value='M', width='5', bg='white').place(x=440, y=220)
    Radiobutton(root, text='Female', variable=var, value='F', width='6', bg='white').place(x=510, y=220)

    t8 = Entry(root, width='25', bg='white')
    t8.place(x=445, y=417)

    # create a photo_image
    image_path = r"c:\Users\Lenovo\Pictures\Saved Pictures\oip.jpg"
    image = Image.open(image_path)
    image_resized = image.resize((118, 100))
    photo = ImageTk.PhotoImage(image_resized)
    photo_label = Label(root, image=photo)
    photo_label.place(x=690, y=30)
    photo_button = Button(root, text='SELECT PHOTO',width=14, font=('arial', 10, 'bold'), bg="blue",command=select_image)
    photo_button.place(x=690, y=130)

    b1 = Button(root, text='SUBMIT', font=('arial', 10, 'bold'), width=15, bg='blue',command=submit)
    b1.place(x=685, y=470)
    b2 = Button(root, text="CLEAR ", font=('arial', 10, 'bold'), width=15, command=clear, bg="red")
    b2.place(x=535, y=470)

    root.mainloop()

