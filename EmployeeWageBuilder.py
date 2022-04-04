'''
@Author : Priyanka
@Date : 2022-04-02  16:55:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-02  17:00:00
@Title : Check employee is present or not.
'''

import random

print("Welcome to the employee wage computation program")

empCheck = random.randint(0,1)

if empCheck == 1:
    print("Employee is present")
else:
    print("Employee is absent")