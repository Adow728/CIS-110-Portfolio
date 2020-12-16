"""
Program name: Changing bases
Author: Aiden Dow
Class: CIS-110
Description: This program converts a base 10 number into another base specified by the user using a recursive function
Date created/modified: 12/13/19
Notes:
"""

import datetime

def baseConvert(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return ""
    else:
        return baseConvert(num // base, base) + " " + digits[num % base]

def main():
    print("This program converts a base 10 number into another base")
    cont = True
    while cont:
        num = int(input("What number to convert (larger than 0): "))
        base = int(input("Which base to convert into(between 2 and 26): "))
        print(f"The resulting digits are {baseConvert(num, base)}")
        cont = input("Calculate another number[Yn]? ").strip() != "n"
        print()


    print()
    print("Aiden Dow")
    print("CIS-110")
    print("Program 13")
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()
