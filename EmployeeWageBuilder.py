'''
@Author : Priyanka
@Date : 2022-04-04  18:40:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-04  19:00:00
@Title :Store the daily wage along with the total wage.
'''

import random

print("Welcome to the employee wage computation program")

fullDayEmpHours = 8
halfDayEmpHours = 4
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
dailyWage = []


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


def totalWorkingHours():
    """
            Description:
                Calculating total working hours.
            Parameter:
                None
            Return:
                return total working hours in month
    """

    totalWorkingDays = 0
    totalEmpHours = 0
    totalEmpWage = 0
    NUM_OF_WORKING_DAYS = 20
    MAX_HOURS_IN_MONTH = 100

    while (totalEmpHours < MAX_HOURS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS):
        empCheck = random.randint(0, 1)
        employeeWage = empPresentyCheck(empCheck)
        if empCheck == 0:
            employeeWage
        else:
            employeeWage[0]
            employeeWage[1]
            totalEmpWage += employeeWage[1]
            dailyWage.append(employeeWage[1])
            totalEmpHours += employeeWage[2]
            totalWorkingDays += 1
    print("Total working days is", totalWorkingDays)
    print("Total employee wage for {} days is {}".format(totalWorkingDays, totalEmpWage))
    print("Daily employee wage is", dailyWage)
    return totalEmpHours


print("Total Employee working Hours in a month is", totalWorkingHours())