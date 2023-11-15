from tkinter import *
from tkinter import messagebox
import mysql.connector



def issue_db():

    global id
    global Sid
    

    bid=id.get()
    bStudentID=Sid.get()

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()
    
    print(bid,end='--')
    print(bStudentID,end='--')
    print("issue")
    
    try:
        checkavailability="select * from books where available='YES' AND bid='"+bid+"';"
        print(checkavailability)
        cursor.execute(checkavailability)
        
        flag=0
        for i in cursor:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;

        checkstudent="select * from student where sid='"+bStudentID+"';"
        print(checkstudent)
        cursor.execute(checkstudent)
        
        tag=0
        for i in cursor:
            print(i[0])
            if(i[0]==bStudentID):
                tag=1
                break;

        #if tag==0:
        #    messagebox.showinfo ("Error"."Student not found")
        #    break;
        #    if flag==0:
        #        messagebox.showinfo ("Error","Book not available")
        #        break;
        if flag==1 and tag==1:
             updatequery="update books set available='NO' where bid='"+bid +"';"
             print(updatequery)
             cursor.execute(updatequery)
             db.commit()
             addquery="insert into issue values('"+bid+"','"+bStudentID+"');"
             print(addquery)
             cursor.execute(addquery)
             db.commit()
             messagebox.showinfo("Success","Book issued Successfully")
             
        else:
            messagebox.showinfo("Error","INVALID book ID ... ") if flag==0 else messagebox.showinfo("Error","Invalid Student")

    except:
        messagebox.showinfo("Error","Cannot issue given book ")
    window.destroy()

def issueBooks():

    global id
    global Sid
    global window

    window=Tk()
    window.geometry("700x200")
    window.title('SRM Central Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'),fg='red', text = "       Issue Books")
    greet.grid(row = 0,columnspan = 1000)

    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Book id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    #----------Student ID-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Student ID: ")
    L.grid(row = 4, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)

    Sid=Entry(window,width=5,font =('arial', 15, 'bold'))
    Sid.grid(row=4,column=3)
    
    submitbtn=Button(window,text="Submit",command=issue_db,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("issue")
    pass
