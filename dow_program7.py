"""
Program name: Easter Calculator
Author: Aiden Dow
Class: CIS-110
Description: Easter Calculator 1900 - 2099
Date created/modified: 11/2/19
Notes:
"""

import datetime

def easterDate(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    return 22 + d + e

def main():
    print("Easter Calculator 1900 - 2099\n")

    year = int(input("What year? "))
    if year < 2100 and year >= 1900:
        date = easterDate(year)
        if year == 1981 or year == 1954 or year == 2049 or year == 2076:
            date -= 7
        if date > 31:
            month = "April"
            date -= 31
        else:
            month = "March"
        print("Easter is {} {}".format(month, date))
    else:
        print("That date is not in the range 1900 - 2099")

    print()


    print()
    print("Aiden Dow")
    print("CIS-110")
    print("Program 7")
    print(datetime.datetime.now())

main()
