from tkinter import *
from tkinter import ttk
from database import get_db


def emp():
    root = Tk()
    root.title("Employee Status")
    root.geometry("860x440")
    width = 860
    height = 460

    tv = ttk.Treeview(root)

    def get_route_info():
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"select id_emp,name_emp,father_name,dob,email,gender,phone_no,desiganation,address from add_emp")
        rows = cur.fetchall()
        conn.close()
        return rows

    tv['columns'] = ('id_emp', 'name_emp', 'father_name', 'dob', 'email', 'gender', 'phone_no', 'desiganation','address')

    tv.column('#0', width=-30, minwidth=0)
    tv.column('id_emp', width=20, minwidth=5)
    tv.column('name_emp', width=40, minwidth=20)
    tv.column('father_name', width=40, minwidth=20)
    tv.column('dob', width=14, minwidth=10)
    tv.column('email', width=40, minwidth=20)
    tv.column('gender', width=40, minwidth=20)
    tv.column('phone_no', width=40, minwidth=20)
    tv.column('desiganation', width=40, minwidth=20)
    tv.column('address', width=40, minwidth=20)

    tv.heading('id_emp', text="Employee Id")
    tv.heading('name_emp', text="Employee Name")
    tv.heading('father_name', text="Father Name")
    tv.heading('dob', text="D.O.B")
    tv.heading('email', text="E-mail")
    tv.heading('gender', text="Gender")
    tv.heading('phone_no', text="Phone Number")
    tv.heading('desiganation', text="Job")
    tv.heading('address', text=" Address")

    rows = get_route_info()
    for row in rows:
        tv.insert(parent='', index='end', values=row)

    sb = ttk.Scrollbar(tv, orient='vertical')
    sb.config(command=tv.yview)
    tv.config(yscrollcommand=sb.set)
    sb.pack(side='right', fill='y')

    tv.place(x=0, y=0, width=width, height=height - 40)


    root.mainloop()
