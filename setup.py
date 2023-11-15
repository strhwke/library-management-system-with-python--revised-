import mysql.connector as sql 
host = 'localhost'
user = 'root'
password = 'archis2004'
db = sql.connect(host ="localhost",user = "root",password = 'archis2004')
cursor = db.cursor()

cursor.execute("create if not exists database library")
cursor.execute("use library")
cursor.execute("""create if not exists table books(
bid varchar(10) primary key default null,
title varchar(10)default null,
author varchar(10)default null,
available varchar(5) default null,
)""")

cursor.execute("""create if not exists table issue(BID varchar(10),
SID varchar(10) default null)
""")

cursor.execute("""create if not exists table student(SID varchar(10) primary key default null, 
sname varchar(30) default null, 
sclass varchar(10) default null)""")

