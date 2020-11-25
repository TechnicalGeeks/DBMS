import sqlite3
import csv
import os

conn=sqlite3.connect("Attendance.db")
cursor=conn.cursor()
def update_count(div,subject):
    cursor.execute(f'select {div} from lec_count where subject=?',(subject,))
    count=int(cursor.fetchone()[0])
    print("count=",count)
    cursor.execute(f'update lec_count set {div}={count+1} where subject=?',(subject,))
    print("Lecture Count Successfully Updated")

def update_attendance(year,div,subject):
    cursor.execute('select cid from class where year=? and div=?',(year,div))
    classID=int(cursor.fetchone()[0])
    print(classID)
    cursor.execute(f'select sid,name from student where cid={classID};')
    list=cursor.fetchall()
    with open('Temparary.csv','w') as file:
        write=csv.writer(file,lineterminator="\n")
        write.writerow(['StudentID','Name','P/A'])
        for row in list:
            write.writerow(row)
    print("Created Table")
    os.system('start excel Temparary.csv')
    _=input("Done ?(y/n):")
    with open('1.csv','r') as file:
        read=csv.reader(file)
        for row in read:
            print(row)






# update_count('A','DSA')
update_attendance('SE','C','DSA')
conn.commit()
conn.close()