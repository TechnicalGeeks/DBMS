import sqlite3


conn = sqlite3.connect('Attendance.db')
print ("Opened database successfully");


# conn.execute('''
#             Create table student (
#                 s_id number ,
#                 name varchar2(20),
#                 mobile number(10)
#             );        
#             ''')


# print ("Table Created  successfully");


conn.execute("""insert into student (s_id,name,mobile) values (1,'Rohan',9999999999)""" )

print("\n__________ Printing table content _______________\n")

cursor = conn.execute("SELECT  s_id,name,mobile from student")

for row in cursor:
    print("ID     : ",row[0])
    print("Name   : ",row[1])
    print("Mobile : ",row[2])



print("Operation done successfully")
conn.close()