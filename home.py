from tkinter import *
import mysql.connector

from add import *
from delete import *
from issue import * 
from Return import *
from view import *
from add_student import *
from delete_student import *
from view_student import *
from view_issued import *

db = mysql.connector.connect(host ="localhost",user = "root",password = 'archis2004',database='library')
cursor = db.cursor()

window=Tk()
window.geometry("650x500")
#bg=PhotoImage(file="D8pQK08.gif")
window.title("SRM Central Library Management System")
#label1=Label(window,image=bg)
#label1.place(x=0,y=0)
        
greet = Label(window, font = ('times new roman', 30, 'bold'), fg="red", text = "   Welcome to SRM Central Library")
greet.grid(row = 1,columnspan = 3)

addbtn=Button(window,text="Add Books",command=addBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
addbtn.grid(row=3,column=0)

deletebtn=Button(window,text="Delete Books",command=deleteBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
deletebtn.grid(row=5,column=0)

issuebtn=Button(window,text="Issue Books",command=issueBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
issuebtn.grid(row=7,column=0)

returnbtn=Button(window,text="Return Books",command=returnBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
returnbtn.grid(row=9,column=0)

viewbtn=Button(window,text="View Books",command=viewBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
viewbtn.grid(row=11,column=0)

addstudbtn=Button(window,text="Add Students",command=addStudents,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
addstudbtn.grid(row=3, column=2)

delstudbtn=Button(window,text="Delete Students",command=deleteStudents,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
delstudbtn.grid(row=5, column=2)

viewstudbtn=Button(window,text="View Students",command=viewStudents,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
viewstudbtn.grid(row=7, column=2)

viewissuedbtn=Button(window,text="View Issued Books",command=viewIssuedBooks,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
viewissuedbtn.grid(row=9, column=2)


greet1 = Label(window, font = ('arial', 15, 'bold'), fg='red',text = "")
greet1.grid(row = 13,columnspan = 3)
greet2 = Label(window, font = ('arial', 15, 'bold'), fg='red',text = " ")
greet2.grid(row = 15,columnspan = 3)
greet3 = Label(window, font = ('arial', 15, 'bold'), fg='red',text = "")
greet3.grid(row = 17,columnspan = 3)
greet4 = Label(window, font = ('calibri', 15, 'bold'), fg='red',text = "Developed by : Archisman Hes\n\t         Saloni Bhardwaj\n\t       Shovik Banerjee")
greet4.grid(row = 19,columnspan = 3)

window.mainloop()
