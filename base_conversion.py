# Changing bases
# This program converts a base 10 number into another base specified by the user using a recursive function
# Aiden Dow
# 12/13/2019 - Revised 12/21/2020

import datetime

def baseConvert(num, base):
    """Convert a number into a different base"""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return ""
    else:
        return baseConvert(num // base, base) + " " + digits[num % base]

def main():
    print("This program converts a base 10 number into another base")
    cont = True
    while cont:
        print()
        num = int(input("What number to convert (larger than 0): "))
        base = int(input("Which base to convert into(between 2 and 26): "))
        print(f"The resulting digits are {baseConvert(num, base)}")
        cont = input("Calculate another number[Yn]? ").strip().lower() != "n"


if __name__ == "__main__":
    main()

    print()
    print("Aiden Dow")
    print(datetime.datetime.now())