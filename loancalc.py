import time
from datetime import date
from datetime import datetime

# 1. Define the dates of disbursment

'''
dates of disbursment of a student loan are typically 2 times a year
for avg college student. Add dates as needed for years in college, and
amount of loans.
today's date is important also in order to calculate the growing intrest as
of today.
'''

today = date.today()
date1 = "2016-08-19"
date2 = "2017-01-13"
date3 = "2017-08-18"
date4 = "2018-01-12"
# date5 = "2018-09-10"


# 2. add dates to a list and create an empty list
orginaldates = [date1, date2, date3, date4]
finaldays = []

# 3. Transform dates into intergers of days, for these specfic loans the growth is daily
# So it depends how you need to split the loan in order to understand the intrest loan
# the equation is divied by 365 to get a float number for later equation.
# so 700 days / 365 would equal 1.91 years
for ogdate in orginaldates:
    converteddate = datetime.strptime(ogdate, "%Y-%m-%d").date()
    days = (today - converteddate).days / 365
    finaldays.append(days)
# print(finaldays) <--- This is just a test to confrim you are getting the correct values


prinicipal = [14500, 19350]
prinicipalhalf = [7250, 9675]
rates = [5.31, 6.00]
newrates = []

for i in rates:
    decrates = i / 100
    newrates.append(decrates)
# print(newrates) <--- This is just a test to confrim you are getting the correct values

finalloan1 = []
for i in finaldays[0:2]:
    for j in prinicipalhalf[0:1]:
        for k in newrates[0:1]:
            loanvalues = j * (1+(k * i))
    print(loanvalues)
    finalloan1.append(loanvalues)

finalloan2 = []
for i in finaldays[2:4]:
    for j in prinicipalhalf[1:2]:
        for k in newrates[1:2]:
            loanvalues = j * (1+(k * i))
    print(loanvalues)
    finalloan2.append(loanvalues)

sum1 = sum(finalloan1)
sum2 = sum(finalloan2)

intrestgained1 = sum1 - prinicipalhalf[0]*2
intrestgained2 = sum2 - prinicipalhalf[1]*2

print(intrestgained1)
print(intrestgained2)
