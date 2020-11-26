import sqlite3

conn =sqlite3.connect("Attendance.db")
cursor = conn.cursor()
print("Connection established Successfully ....  ")

def details_student():
    year = input("Enter Year (SE/TE/BE) :  ").upper()
    # division = input("Enter Division (A/B/C) : ")

    choice = int (input("---  Search By --- \n1.Student ID (SID)\n2.Name\n3.Roll number\nEnter choice : "))


    if choice == 1:
        sid = int (input ("Enter Student ID (SID) : "))

        cursor.execute(""" 
                            select * from {year} inner join  Student on 
                                Student.sid = ? and {year}.sid= ?
        
                            """.format(year=year),(sid,sid))
        
        data = cursor.fetchall()
        if data == [] :
            print("\n______  Sorry !! No DATA FOUND _____\n")
        else :
            print (data)

    elif choice == 2 :
        div = input("Enter division (A/B/C) : ").upper()
        year1 =" " +year +" "
        name1 = input("Enter Name : ").upper()
        name1= '%'+name1+'%'
        print(type(year),div,name1)
        
        flag = cursor.execute(""" 
                    SELECT * from {year} 
                    INNER JOIN StudenT
                    on  {year}.CID= (SELECT  CID from CLASS WHERE CLASS.Year=? and CLASS.Div=?) 
                    and {year}.SID=Student.SID and Student.NAME like ?;                 
                """.format(year=year),(year,div,name1))
        data = cursor.fetchall()
        if data == []:
            print("\n-------   No data found  -----------\n")
        else:
            print(data)    

    else:
        div = input("Enter division (A/B/C) : ").upper()
        roll = int (input("Enter Roll number (EG 101,332): "))

        flag = cursor.execute(""" 
                    SELECT * from {year} 
                    INNER JOIN StudenT
                    on  {year}.CID= (SELECT  CID from CLASS WHERE CLASS.Year=? and CLASS.Div=?) 
                    and {year}.SID=Student.SID and Student.roll = ?;                 
                    """.format(year=year),(year,div,roll))
        data = cursor.fetchall()
        if data == []:
            print("\n-------   No data found  -----------\n")
        else:
            print(data) 



details_student()    

