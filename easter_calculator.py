# Easter Calculator
# Calculates the date of easter any year from 1900 to 2099
# Aiden Dow
# 11/2/2019 - Revised 12/21/2020

import datetime

def easterDate(year):
    # Calculates the date of easter
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = 22 + d + e
    if year == 1981 or year == 1954 or year == 2049 or year == 2076:
        date -= 7

    return date

def main():
    print("Easter Calculator 1900 - 2099\n")

    # Get user input
    year = int(input("What year? "))

    # If user input is valid
    if year < 2100 and year >= 1900:
        # Calculate and display the date
        date = easterDate(year)
        if date > 31:
            month = "April"
            date -= 31
        else:
            month = "March"
        print("Easter is {} {}".format(month, date))
    else:
        # Else print error message
        print("That date is not in the range 1900 - 2099")

main()

print()
print("Aiden Dow")
print(datetime.datetime.now())