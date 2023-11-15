from tkinter import *
from tkinter import messagebox
import mysql.connector

def viewStudents():

    global id

    window=Tk()
    window.geometry=("1000x400")
    window.title('SRM Central Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'),fg="red", text = "                   View Students")
    greet.grid(row = 0,columnspan = 3)

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()

    sqlquery= "select * from student;"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        
        L = Label(window, font = ('arial', 20), text = "%-10s%-30s%-30s"%('           SID','       Name','      Class'))
        L.grid(row = 1,columnspan = 4)

        L = Label(window, font = ('arial', 20), text = "-----------------------------------------------")
        L.grid(row = 2,columnspan = 4)

        x=4
        for i in cursor:
            L = Label(window, font = ('arial', 15), text = "%-10s%-30s%-30s"%(i[0],i[1],i[2]))
            L.grid(row = x,columnspan = 4)
            x+=1   

    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    print("view")
    pass
