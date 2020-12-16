"""
Program name: Fibbonaci 
Author: Aiden Dow
Class: CIS-110
Description: This program calculates the nth Fibonacci value
Date created/modified: 9/19/2019
Notes:
"""

import datetime

def main():
    print("This program calculates the nth Fibonacci value.")
    print()

    n = int(input("Enter the value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr+prev, curr

    print()
    print("The nth Fibonacci number is", curr)

    print()
    print("Aiden Dow")
    print("CIS-110")
    print(datetime.datetime.now())

main()
