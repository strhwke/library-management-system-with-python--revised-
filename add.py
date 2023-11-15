from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_db():

    global id
    global title
    global author

    bid=id.get()
    btitle=title.get()
    bauthor=author.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()
    
    print(bid,end='--------')
    print(btitle,end='------------------------------------')
    print(bauthor,end='-----------------------------------')
    print("add")

    sqlquery= "insert into books values('" + bid +"','"+btitle+"','"+bauthor+"','YES');"
    print(sqlquery)
  
    try:
        if bid=="" or btitle=="":
            messagebox.showinfo("Error","Book ID / Title can not be blank")
        else:        
            cursor.execute(sqlquery)
            db.commit()
            messagebox.showinfo('Success',"Book added Successfully")
    except:
        messagebox.showinfo("Error","Duplicate / Invalid Book ID.... Cannot add into Database")
    
    window.destroy()

def addBooks():

    global id
    global title
    global author
    global window

    window=Tk()
    window.title('SRM Central Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "Add Books")
    greet.grid(row = 0,columnspan = 10)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "  ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=10,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    #----------title-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Title: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    title=Entry(window,width=30,font =('arial', 15, 'bold'))
    title.grid(row=4,column=3)

    #----------author-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Author: ")
    L.grid(row = 6, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 6, column = 2)

    author=Entry(window,width=30,font =('arial', 15, 'bold'))
    author.grid(row=6,column=3)
    
    submitbtn=Button(window,text="Submit",command=add_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("add")
    pass
