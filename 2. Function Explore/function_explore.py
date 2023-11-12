'''VERSION 1'''

'''Version 1: 
            - Measuring functions and user input are not yet detailed
            - not yet using docstring (Document String) for ease of use of function ('def')
            - The script code tends to be a bit long'''

import os
os.system("cls")
# # PRACTICE FUNCTION ("def"): PROGRAM FOR MEASUREMENT OF AREAS & CIRCUMFERENCES OF RECTANGLES

# Header Program
def header():
    print()
    print(19*"-")
    print(f"{'PROGRAM PENGUKURAN':^21}")
    print(f"{'LUAS DAN KELILING':^19}")
    print(f"{'PERSEGI PANJANG':^19}")
    print(19*"-")
    print()

def ukur():
    # Input User
    PANJANG = int(input("Masukkan panjangnya (cm):\n==> "))
    LEBAR   = int(input("Masukkan lebarnya (cm):\n==> "))
    # Function Areas
    LUAS = PANJANG * LEBAR
    KELILING = 2*(LEBAR + PANJANG)
    print()
    print(38*"-")
    print(f"Luasnya : {LUAS} cm | Kelilingnya : {KELILING} cm")
    print(38*"-")
    print()

# main PROGRAM

while True:
    header()
    ukur()
    print()
    question = input("Masih ingin mengukur lagi?\n==> ")
    if question == "Tidak" or question == "No":
        break
print()    
print("Terima kasih sudah menggunakan layanan jasa kami! <3")
print()

'''VERSION 2'''

'''Versi 2:
            - Has implemented a more detailed function ('def') with 1 objective
              and assigned functions
            - Already using docstring
            - More simple and effective!!'''
# import os
# os.system("cls")
# PRACTICE FUNCTION ("def"): PROGRAM FOR MEASUREMENT OF AREAS & CIRCUMFERENCES OF RECTANGLES

# Header Program
def header():
    '''Header Pengukuran'''
    print()
    print(19*"-")
    print(f"{'PROGRAM PENGUKURAN':^21}")
    print(f"{'LUAS DAN KELILING':^19}")
    print(f"{'PERSEGI PANJANG':^19}")
    print(19*"-")
    print()

def luas():
    '''Pengukuran Luas Persegi Panjang'''
    PANJANG = int(input("Masukkan panjangnya (cm):\n==> "))
    LEBAR   = int(input("Masukkan lebarnya (cm):\n==> "))
    print()
    print(40*"-")
    return PANJANG * LEBAR

def keliling():
    '''Pengukuran Keliling Persegi Panjang'''
    PANJANG = int(input("Masukkan panjangnya (cm):\n==> "))
    LEBAR   = int(input("Masukkan lebarnya (cm):\n==> "))
    print()
    print(40*"-")
    return 2*(LEBAR + PANJANG)

def input_user():
    '''Input User: untuk angka yang akan diukur'''

    lrk = input("Ingin mengukur luas persegi panjang atau kelilingnya? (L/K)\n==> ")
    if lrk == "L":
        print(f"Keliling dari persegi panjangnya adalah:\n==> {keliling()}")
        print(40*"-")
    elif lrk == 'K':
        print(f"Luas dari persegi panjangnya adalah:\n==> {luas()}")
        print(40*"-")
    else:
        print("Mohon maaf. Tidak dapat ditentukan")

# main PROGRAM

while True:
    header()
    input_user()
    print()
    question = input("Masih ingin mengukur lagi?\n==> ")
    if question == "Tidak" or question == "No":
        break
print()    
print("Terima kasih sudah menggunakan layanan jasa kami! <3")
print()


