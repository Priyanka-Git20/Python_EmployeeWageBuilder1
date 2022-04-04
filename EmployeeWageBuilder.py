'''
@Author : Priyanka
@Date : 2022-04-02  17:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-02  17:10:00
@Title : Calculate daily employee wage.
'''

import random

print("Welcome to the employee wage computation program")

EMP_RATE_PER_HOUR = 20
empHours = 0
empWage = 0
empCheck = random.randint(0,1)

if empCheck == 1:
    print("Employee is present")
    empHours = 8
else:
    print("Employee is absent")
    empHours = 0
empWage = empHours * EMP_RATE_PER_HOUR
print("Employee wage is",empWage)
