# PRACTICE: UGM STUDENT DATABASE PROGRAM USING 'DICTIONARY', 'LOOPS', AND 'INPUT'

import datetime as dt
import os
import string
import random

# Dictionary Template (database)
temp = {
    'ID': 111111,
    'NAME':'name',
    'BORNDATE':dt.date(1111,11,1),
    'MAJOR':'major'
}

# Database Storage
dB_ugm = {}

# Looping
while True:
    print(35*"=")
    print("WELCOME TO THE UGM STUDENT DATABASE")
    print(35*"=")
    print()    
    # os.system("cls")
    # Connecting Original dB to the  template (based)
    key = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    student = dict.fromkeys(temp.keys())

    # Input Data
    student['ID'] = int(input("Drop your student ID:\n==> "))
    student['NAME'] = input("\nDrop your name:\n==> ")
    born_year = int(input("\nDrop your born year:\n==> "))
    born_month = int(input("\nDrop your born month:\n==> "))
    born_day = int(input("\nDrop your born day:\n==> "))
    student['BORNDATE']=dt.date(born_year,born_month,born_day)
    student['MAJOR'] = input("\nDrop your major:\n==> ")
    print()

    # Update Database
    dB_ugm.update({key:student})

    # Print out header
    print(50*"-")
    print(f"{'KEY':<7} {'ID':<7} {'NAME':<16} {'BORNDATE':<10} {'MAJOR':8}")
    print(50*"-")

    # Print out database
    for i in dB_ugm:
        key = i

        ID = dB_ugm[key]['ID']
        NAME = dB_ugm[key]['NAME']
        BORNDATE = dB_ugm[key]['BORNDATE'].strftime("%x")
        MAJOR = dB_ugm[key]['MAJOR']

        print(f"{key:<7} {ID:<7} {NAME:<16} {BORNDATE:<10} {MAJOR:<8}")
    print(50*"-")
    print()

    # Follow-Up Inputing Data to Database
    quest = input("Continue for update the database?\n==> ")
    if quest == "No" or quest == "Tidak" or quest == "no" or quest == "Tidak":
        break
print()
print("Program is ended.\nThankyou for your participate! <3")



