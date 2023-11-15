import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='archis2004')
mycursor=conn.cursor()
conn.autocommit = True
mycursor.execute("create database library")
mycursor.execute("use library")
mycursor.execute("create table books(bid varchar(10) primary key,title varchar(50) Not null,author varchar(50) not null,available varchar(5) default 'YES')")
mycursor.execute("create table issue(bid varchar(10) primary key,studentName varchar(50) Not null foreign key(bid) references books(bid))")
mycursor.execute("alter table student(stud_id bigint,term varchar(20),english int,physics int,chemistry int,maths_bio int,comp_pe int)")
print ("table created")
