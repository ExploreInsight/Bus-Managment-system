from tkinter import *
from tkinter import ttk
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='madhu123', database='emp')
cur = conn.cursor()


def s_route():
    root = Tk()
    root.title("Routes Status")
    root.geometry("860x440")
    width = 860
    height = 460

    tv = ttk.Treeview(root)

    def get_route_info():
        """return list of tuples"""
        cur.execute(f"select routes.route_no,  route_name, route_distance, start, end from emp.routes ")
        return cur.fetchall()

    # specify columns, where each element in tuple is treeViewID
    tv['columns'] = ('route_no', 'route_name', 'route_distance', 'start', 'end')

    # format columns using treeViewID
    # column with #0ID is a ghost column
    tv.column('#0', width=-30, minwidth=0)
    tv.column('route_no', width=20, minwidth=5)
    tv.column('route_name', width=40, minwidth=20)
    tv.column('route_distance', width=40, minwidth=20)
    tv.column('start', width=14, minwidth=10)
    tv.column('end', width=40, minwidth=20)

    # specify headings to columns
    tv.heading('route_no', text="Route Number")
    tv.heading('route_name', text="Route Name")
    tv.heading('route_distance', text="Distance")
    tv.heading('start', text="Location")
    tv.heading('end', text="Destination")

    # inserting data into treeView
    rows = get_route_info()
    for row in rows:
        tv.insert(parent='', index='end', values=row)

    sb = ttk.Scrollbar(tv, orient='vertical')
    sb.config(command=tv.yview)
    tv.config(yscrollcommand=sb.set)
    sb.pack(side='right', fill='y')

    tv.place(x=0, y=0, width=width, height=height - 40)


    root.mainloop()