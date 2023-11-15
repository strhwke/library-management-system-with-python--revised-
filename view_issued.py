from tkinter import *
from tkinter import messagebox
import mysql.connector

def viewIssuedBooks():

    global id

    window=Tk()
    window.geometry=("1000x400")
    window.title('SRM Central Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'),fg="red", text = "            View Issued Books")
    greet.grid(row = 0,columnspan = 3)

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()

    sqlquery= "select * from issue inner join student on issue.sid=student.sid inner join books on issue.bid=books.bid;"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        
        L = Label(window, font = ('arial', 20), text = "%-10s%-30s%-30s%-30s%-30s"%('BID','Book Title','Author','Student Name', 'Class'))
        L.grid(row = 1,column = 0)

        L = Label(window, font = ('arial', 20), text = "------------------------------------------------------------------------------------------------------------------------------")
        L.grid(row = 2,column = 0)

        x=4
        for i in cursor:
            L = Label(window, font = ('arial', 20), text = "%-10s%-30s%-30s%-30s%-30s"%(i[0],i[6],i[7],i[3],i[4]))
            L.grid(row = x,column = 0)
            x+=1   

    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    print("view")
    pass
