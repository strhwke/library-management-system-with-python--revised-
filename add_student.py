from tkinter import *
from tkinter import messagebox
from tkinter.tix import WINDOW
import mysql.connector

def add_students():

    global sid
    global sname
    global sclass

    sid=id.get()
    sname=name.get()
    sclass=clas.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()
    
    print(sid,end='--')
    print(sname,end='--')
    print(sclass,end='--')
    print("add")

    sqlquery= "insert into student values('" +sid+"','"+sname+"','"+sclass+"');"
    print(sqlquery)

    try:
        if sid=="" or sname=="":
            messagebox.showinfo("Error","Student ID / NAme can not be blank")
        else:
            cursor.execute(sqlquery)
            db.commit()
            messagebox.showinfo('Success',"Student added Successfully")
    except:
        messagebox.showinfo("Error","Duplicate / Invalid Student ID.... Cannot add into Database")
    
    WINDOW.destroy()

def addStudents():

    global id
    global name
    global clas

    window=Tk()
    window.geometry=("900x400")
    window.title('Shannen School Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), fg="red", text = "Add Students")
    greet.grid(row = 0,columnspan = 10)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Student id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "  ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=8,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    #----------title-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Name: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    name=Entry(window,width=30,font =('arial', 15, 'bold'))
    name.grid(row=4,column=3)

    #----------author-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Class: ")
    L.grid(row = 6, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 6, column = 2)

    clas=Entry(window,width=8,font =('arial', 15, 'bold'))
    clas.grid(row=6,column=3)
    
    submitbtn=Button(window,text="Submit",command=add_students,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=9,columnspan=3)
        
    print("add")
    pass
