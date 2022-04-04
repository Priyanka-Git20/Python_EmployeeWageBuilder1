'''
@Author : Priyanka
@Date : 2022-04-04  18:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-04  18:25:00
@Title : Calculate Wages till a condition of total working hours or days is reached for a month.
'''

import random

print("Welcome to the employee wage computation program")

fullDayEmpHours = 8
halfDayEmpHours = 4
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
MAX_HOURS_IN_MONTH = 100
totalWorkingDays= 0
totalEmpHours= 0
totalEmpWage = 0


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
    return "Employee is full day present and employee wage is",empWage,fullDayEmpHours


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
    return "Employee is half day present and employee wage is",empWage,halfDayEmpHours


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


while (totalEmpHours < MAX_HOURS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS):
    # totalWorkingDays += 1
    empCheck = random.randint(0, 1)
    employeeWage = empPresentyCheck(empCheck)
    if empCheck == 0:
        employeeWage
    else:
        employeeWage[0]
        employeeWage[1]
        totalEmpWage += employeeWage[1]
        totalEmpHours += employeeWage[2]
        totalWorkingDays += 1

print("Total employee wage for {} days is {}".format(totalWorkingDays,totalEmpWage))
print("Total employee hours in {} days are {}".format(totalWorkingDays,totalEmpHours))
print("Total working days are",totalWorkingDays)
