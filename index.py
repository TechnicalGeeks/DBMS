choice=1
while(choice!=5):
    print("Welcome to Attendance Management System ")
    print("Enter your Choice ")
    print("1. For adding new student. ")
    print("2. For updating attendance or student information. ")
    print("3. For searching attendance of particular student. ")
    print("4. To get list of defaulter students. ")
    print("5. Exit ")
    choice=int(input())
    if choice==1:
        import insert1
    elif choice==2:
        import update
    elif choice==3:
        import search
    elif choice==4:
        import defaulter

