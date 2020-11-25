import csv 
import sqlite3

conn = sqlite3.connect("Attendance.db")
cursor = conn.cursor()
print("Connection successful ... ")

def   insert_class():

    with open ("Data\Classid.csv",'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for rows in csv_reader:
            print(rows[1],rows[2])         
            if i==0 :
                i=2     
            else:
           
                cursor.execute(""" 
                        
                        insert into class (Year,Div) VALUES (?,?);
                        """,(rows[1],rows[2]))

def insert_student():
    with open ("Data\Student.csv",'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for rows in csv_reader:
            print(rows[1],rows[2],rows[3])         
            if i==0 :
                i=2 
            else:
                 cursor.execute(""" 
                        
                        insert into student (Name,roll,cid) VALUES (?,?,?);
                        """,(rows[1],rows[2],rows[3]))

def insert_LectureCount():
    with open ("Data\LectureCount.csv",'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for rows in csv_reader:
            print(rows[0],rows[1],rows[2],rows[3],rows[4])         
            if i==0 :
                i=2 
            else:
                 cursor.execute(""" 
                        
                        insert into lec_count (year,subject,a,b,c) VALUES (?,?,?,?,?);
                        """,(rows[0],rows[1],rows[2],rows[3],rows[4]))


# insert_student()
insert_LectureCount()
conn.commit()
conn.close()