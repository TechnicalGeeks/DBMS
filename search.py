import sqlite3

conn =sqlite3.connect("Attendance.db")
cursor = conn.cursor()
print("Connection established Successfully ....  ")

def details_student():
    year = input("Enter Year (SE/TE/BE) :  ")
    name1 = input("Enter Name : ")
    name1= '%'+name1+'%'
    flag = cursor.execute(""" 
                select * from student where name like ?
    
            """,(name1,))
    data = cursor.fetchall()
    if data == []:
        print("\n-------   No data found  -----------\n")
    else:
        print(data)    
        

details_student()    