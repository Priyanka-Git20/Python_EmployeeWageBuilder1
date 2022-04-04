'''
@Author : Priyanka
@Date : 2022-04-02  17:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-02  17:20:00
@Title : Calculate employee wage based on their shift.
'''

import random

print("Welcome to the employee wage computation program")

EMP_RATE_PER_HOUR = 20
fullDayEmpHours = 8
halfDayEmpHours = 4
empHours = 0
empWage = 0

empCheck = random.randint(0,1)

if empCheck == 1:
    print("Employee is present")
    dayCheck = random.randint(0,1)
    if dayCheck == 0:
        empWage = EMP_RATE_PER_HOUR * fullDayEmpHours
        print("Employee is full day present and employee wage for full day is",empWage)
    else:
        empWage = EMP_RATE_PER_HOUR * halfDayEmpHours
        print("Employee is half day present and employee wage is", empWage)
else:
    print("Employee is absent")
