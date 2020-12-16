"""
Program name: Syracuse Calculation 
Author: Aiden Dow
Class: CIS-110
Description: This program runs the Syracuse calculation from an input n
Date created/modified: 11/6/2019
Notes:
"""

import datetime

def main():
    print("This program runs the Syracuse calculation")
    n = int(input("What starting value of n? "))

    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1, end=" ")
    print()
        

    print()
    print("Aiden Dow")
    print("CIS-110")
    print(datetime.datetime.now())

main()
