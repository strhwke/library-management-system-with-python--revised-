from tkinter import *
from tkinter import messagebox
import mysql.connector

def viewBooks():

    global id

    window=Tk()
    window.geometry=("1000x400")
    window.title('SRM Central Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'),fg="red", text = "View Books")
    greet.grid(row = 0,columnspan = 3)

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()

    sqlquery= "select * from books ;"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        
        L = Label(window, font = ('arial', 20), text = "%-10s%-30s%-30s%-30s"%('BID','Title','Author','Available'))
        L.grid(row = 1,column= 0)

        L = Label(window, font = ('arial', 20), text = "---------------------------------------------------------------------------------------------")
        L.grid(row = 2,column = 0)

        x=4
        for i in cursor:
            L = Label(window, font = ('arial', 15), text = "%-10s%-30s%-30s%-30s"%(i[0],i[1],i[2],i[3]))
            L.grid(row = x,column = 0)
            x+=1   

    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    print("view")
    pass
