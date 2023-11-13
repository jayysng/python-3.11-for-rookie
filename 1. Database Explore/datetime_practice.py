#====================PYTHON PROGRAM: DATE & TIME======================#

import datetime as dt

print("Silahkan masukkan tanggal lahir Anda:\n")

date  = int(input("date\t: "))
month = int(input("month\t: "))
year  = int(input("years\t: "))
print('\n')

birthday = dt.date(year, month, date)
today    = dt.date.today()

#Birthday date
print(f"Your date birhtday is : {birthday}")
print(f"Your birthday is : {birthday:%A}")
#Age
age_days = (today - birthday)
age_month = (age_days.days % 365) // 30
age_years = age_days.days // 365
print(f"Your age is {age_years} years and {age_month} month\n")


