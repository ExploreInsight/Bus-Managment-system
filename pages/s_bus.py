from tkinter import *
from tkinter import ttk
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()

def buses():
    root = Tk()
    root.title("Buses Status")
    root.geometry("860x440")
    width = 860
    height = 460

    tv = ttk.Treeview(root)

    def get_bus_info():
        """return list of tuples"""
        cur.execute(f"select bus_no,bus_name,no_of_seats,model_no,purchase_date,purchase_cost from bus")
        return cur.fetchall()

    # specify columns, where each element in tuple is treeViewID
    tv['columns'] = ('bus_no', 'bus_name', 'no_of_seats', 'model_no', 'purchase_date', 'purchase_cost')

    # format columns using treeViewID
    # column with #0ID is a ghost column
    tv.column('#0', width=-30, minwidth=0)
    tv.column('bus_no', width=20, minwidth=5)
    tv.column('bus_name', width=40, minwidth=20)
    tv.column('no_of_seats', width=40, minwidth=20)
    tv.column('model_no', width=14, minwidth=10)
    tv.column('purchase_date', width=40, minwidth=20)
    tv.column('purchase_cost', width=40, minwidth=20)


    # specify headings to columns
    tv.heading('bus_no', text="Bus Number")
    tv.heading('bus_name', text="Bus Name")
    tv.heading('no_of_seats', text="Seats")
    tv.heading('model_no', text="Model Number")
    tv.heading('purchase_date', text="Buying Date")
    tv.heading('purchase_cost', text="Buying Cost")


    # inserting data into treeView
    rows = get_bus_info()
    for row in rows:
        tv.insert(parent='', index='end', values=row)

    sb = ttk.Scrollbar(tv, orient='vertical')
    sb.config(command=tv.yview)
    tv.config(yscrollcommand=sb.set)
    sb.pack(side='right', fill='y')

    tv.place(x=0, y=0, width=width, height=height - 40)



    root.mainloop()