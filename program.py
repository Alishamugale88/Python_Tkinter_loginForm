
from tkinter import *
import sqlite3

root=Tk()
root.state('zoomed')
root.title("User Registration Form")

Fullname=StringVar()
Email=StringVar()

def data():
    global Fullname
    global Email
    n=Fullname.get()
    e=Email.get()

    con = sqlite3.connect("new.sqlite3")
    cur =con.cursor()
    data_insert_query=("INSERT INTO reg (Fullname,Email) VALUES (?,?)")
    data_insert_tuple=(n,e)
    cur.execute(data_insert_query,data_insert_tuple)
    con.commit()
    con.close()


l0=Label(root,text="REGISTATION")
l0.place(x=550,y=53)

l1=Label(root,text="Fullname")
l1.place(x=530,y=120)

e1=Entry(root,textvariable=Fullname)
e1.place(x=600,y=130)

l2=Label(root,text="Email")
l2.place(x=530,y=180)

e2=Entry(root,textvariable=Email)
e2.place(x=600,y=180)


Button(root,text="Submit",command=data,bg='blue',fg='white').place(x=540,y=280)


def exit():
    root.destroy()

Button(root,text="Exit",command=exit,bg='red',fg='white').place(x=680,y=280)

root.mainloop()