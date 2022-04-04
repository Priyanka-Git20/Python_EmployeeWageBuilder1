'''
@Author : Priyanka
@Date : 2022-04-04  17:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-04  18:00:00
@Title : Calculate employee wage for a month.
'''

import random

print("Welcome to the employee wage computation program")

fullDayEmpHours = 8
halfDayEmpHours = 4
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
totalEmpWage = 0
totalWorkingDays= 0


def empFullDayWage():
    """
        Description:
            Calculating employee full day wage
        Parameter:
            None
        Return:
            Total employee wage and presenty message.
    """
    empWage = fullDayEmpHours * EMP_RATE_PER_HOUR
    return "Employee is full day present and employee wage is",empWage


def empHalfDayWage():
    """
        Description:
            Calculating employee half day wage
        Parameter:
            None
        Return:
            Total employee wage and presenty message.
    """
    empWage = halfDayEmpHours * EMP_RATE_PER_HOUR
    return "Employee is half day present and employee wage is",empWage


def empPresentyCheck(presentyCheck):
    """
        Description:
             check employee is present or absent.
        Parameter:
             Two random number for employee attendance
        Return:
            returning the check variable
    """
    switcher = {
        0: 'Employee is Absent',
        1: empwageCalculate(random.randint(0, 1))
    }
    return switcher[presentyCheck]


def empwageCalculate(randomCheck):
    """
        Description:
            calculating employees wage
        Parameter:
             two random number for checking full day or half day wage.
        Return:
            return function values from full or half day
    """
    switcher = {
        0: empHalfDayWage(),
        1: empFullDayWage()
    }
    return switcher[randomCheck]

while(totalWorkingDays < NUM_OF_WORKING_DAYS ):
    empCheck = random.randint(0, 1)
    employeeWage = empPresentyCheck(empCheck)
    if empCheck == 0:
        (employeeWage)
    else:
        (employeeWage[0])
        (employeeWage[1])
        totalEmpWage += employeeWage[1]
        totalWorkingDays += 1

print("Total employee wage for {} days is {}".format(totalWorkingDays,totalEmpWage))
