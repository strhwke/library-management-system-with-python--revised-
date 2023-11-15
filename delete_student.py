from tkinter import *
from tkinter import messagebox
import mysql.connector

def delete_students():

    global id

    sid=id.get()
    
    db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
    cursor = db.cursor()
    
    print(sid,end='--')
    print("delete")
    
    
    try:
        sqlquery="select * from student where sid='"+sid+"';"
        print(sqlquery)
        cursor.execute(sqlquery)
        cursor.close
        flag=0
        for i in cursor:
            if (i[0]==sid):
                flag=1
                print(flag)
                print (sid)
                break;
        if flag==1:
            delquery1="delete from student where sid='"+sid+"';"
            print(delquery1)
            cursor.execute(delquery1)
            db.commit()
            messagebox.showinfo('Success',"Student removed Successfully")
        else:
            messagebox.showinfo("Error","Student not found")
    except:
        messagebox.showinfo("Error","Student with given id does not exist")
    
    window.destroy()

def deleteStudents():

    global id
    global window

    window=Tk()
    window.geometry("500x300")
    window.title('SRM Central Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), fg="red", text = "         Delete Student")
    greet.grid(row = 0,columnspan = 3)
    
    #----------id-------------------

    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter Student id: ")
    L.grid(row = 2, column = 1)

    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)

    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)

    submitbtn=Button(window,text="Submit",command=delete_students,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("delete")
    pass
