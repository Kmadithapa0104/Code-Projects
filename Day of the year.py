"""
Author: Kholofelo Madithapa
Date: 20 March 2023
Purpose: Determines the nth of the day in a year.
"""

year = int(input("Enter year here: "))
month = int(input("Enter month number here: "))
day = int(input("Enter day of the month here: "))

"""
This function checks if the particular year it receives is a leap year or common year.
Returns true if leap year otherwise false if common year.
"""
def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False

"""
Calculates and returns days in a month.
"""
def days_in_month(year, month):
    #Terminates function if user entered invalid month and/or year
    if year < 1582 or month < 1 or month > 12:
        return None
    
    #A list of days for January to December for a common year
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days  = days[month - 1]

    #For February on a leap year
    if month == 2 and is_year_leap(year):
        month_days = 29

    return month_days

"""
Calculates and returns the day of the year.
"""
def day_of_year(year, month, day):
    #days before the current day
    days = 0
    #traverse months before the currrent month
    for m in range(1, month):
        #stores days in a month
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(year, month, day))