import mysql.connector 
import admin
import teacher

usr = input("Enter mySQL Username: ") #Taking Username From User
pwd =  input("Enter mySQL  Password: ")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="{}".format(input("Enter your password: ")))
cursor = mydb.cursor()
with open("new.txt") as file:
    for line in file.readlines():
        cursor.execute(line)
    mydb.commit()

print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System ==========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : Run as admin
Enter 2 : Run as teacher  
                """)
    try: #Using Exceptions For Validation
            userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
            exit("\nHey! That's Not A Valid Number") #Error Message
    else:
            print("\n") #Print New Line

    if userInput == 1:
        admin.runAdmin()

    elif userInput == 2:
        teacher.runTeacher()