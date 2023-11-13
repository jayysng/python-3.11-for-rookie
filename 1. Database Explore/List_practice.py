import datetime
import string
import random
import os


# 1.Database Template
datbes_template = {
    'ID':'0000000',
    'NAME':'Nama',
    'BORNDAY':datetime.datetime(1111,11,1)
}

# 2.Database Inputing using Loops
student_database = {}
while True:
    #Big Header
    os.system("cls")
    print(31*"=")
    print("WELCOME TO THE STUDENT DATABASE")
    print(31*"=")
    print()    

    # 3.Create Dictionary based the template before
    student = dict.fromkeys(datbes_template.keys())

    # 4.Input Data to database
    student['ID'] = int(input("Drop student ID\t\t : "))
    student['NAME'] = input("Drop your name\t\t : ")
    born_year = int(input("Drop your born year\t : "))
    born_month = int(input("Drop your born month\t : "))
    born_day = int(input("Drop your born day\t : "))
    student['BORNDAY'] = datetime.datetime(born_year,born_month,born_day)
    print()
    
    # 5.KEY-ing
    key = ''.join(random.choice(string.ascii_uppercase)for i in range (6))
    student_database.update({key:student})

    # 6.Database Header and Headline
    print(43*"-")
    print(f"{'KEY':<7} {'ID':<7} {'NAME':<18} {'BORNDAY':<8}")
    print(43*"-")

    # 7.Sorting and Showing the Database
    for i in student_database:
        key = i

        stud_id = student_database[i]['ID']
        name    = student_database[i]['NAME']
        bornday = student_database[i]['BORNDAY'].strftime("%x")
        
        print(f"{key:<7} {stud_id:<7} {name:<18} {bornday:<8}")
    print(43*"-")
    print()

    # 8.Follow-Up for Inputing data or no(.?)
    quest= input("Continue to add more data?\n")
    print()
    if quest == "Tidak" or quest == "No":
        break
print("PROGRAM IS ENDED. THANK YOU!")
print()



