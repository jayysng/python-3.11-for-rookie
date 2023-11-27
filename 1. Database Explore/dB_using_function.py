import datetime as dt
import string
import random
import os
os.system("cls")
# Program Student dB
# print()
# print(21*"-")
# print("PROGRAM DB STUDENT 'X")
# print(21*"-")
# print()

# dB_Template
dB_template = {
    'ID': 111111,
    'NAME': 'name',
    'MAJOR': 'major',
    'BORNDATE': dt.date(1111,11,1),
    'REGION': 'region'
}
# Input Data from user
# student['ID'] = int(input("Drop your student ID:\n==> "))
# student['NAME'] = input("Drop your full name:\n==> ")
# student['MAJOR'] = input("Drop your major:\n==> ")
# born_y = int(input("Drop your born year:\n==> "))
# born_m = int(input("Drop your born month:\n==> "))
# born_d = int(input("Drop your born day:\n==> "))
# student['BORNDATE'] = dt.date(born_y,born_m,born_d)
# student['REGION'] = input("Drop your region:\n==> ")
# print()

# Connecting to dB template (KEY-ing)
key = ''.join(random.choice(string.ascii_uppercase) for i in dB_template)
student = dict.fromkeys(dB_template.keys())

# Creating Function ('def')
def ID():
    '''Input student ID'''
    student['ID'] = int(input("Drop your student ID:\n==> "))

def name():
    '''Input name'''
    student['NAME'] = input("Drop your full name:\n==> ")

def major():
    '''Input name'''
    student['MAJOR'] = input("Drop your major:\n==> ")

def borndate():
    '''Input borndate'''
    born_y = int(input("Drop your born year:\n==> "))
    born_m = int(input("Drop your born month:\n==> "))
    born_d = int(input("Drop your born day:\n==> "))
    student['BORNDATE'] = dt.date(born_y,born_m,born_d)

def region():
    '''Input region'''
    student['REGION'] = input("Drop your region:\n==> ")

dB_template = {
    'ID': 111111,
    'NAME': 'name',
    'MAJOR': 'major',
    'BORNDATE': dt.date(1111,11,1),
    'REGION': 'region'
}

dB_student = {}
# Looping
while True:
    print()
    print(21*"-")
    print("PROGRAM DB STUDENT 'X")
    print(21*"-")
    print()

    key = ''.join(random.choice(string.ascii_uppercase) for i in dB_template)
    student = dict.fromkeys(dB_template.keys())

    ID()
    print()
    name()
    print()
    major()
    print()
    borndate()
    print()
    region()
    print()

    dB_student.update({key:student})
    print(52*"-")
    print(f"{'KEY':<7} {'ID':<7} {'NAME':<16} {'BORNDATE':<11} {'REGION':<14}")  
    print(52*"-")

    for i in dB_student:
        key = i
        
        IDS = dB_student[i]['ID']
        NAME = dB_student[i]['NAME']
        MAJOR = dB_student[i]['MAJOR']
        BORNDATE = dB_student[i]['BORNDATE'].strftime("%x")
        REGION = dB_student[i]['REGION']
        
        print(f"{key:<7} {IDS:<7} {NAME:<16} {BORNDATE:<11} {REGION:<14}")
    print(52*"-")
    print()  
    
    question = input("Continue for input data?(Yes/No)\n==> ")
    if question == "No" or question == "Tidak":
        break
print()
print("THANK YOU! <3")
print()
# end
