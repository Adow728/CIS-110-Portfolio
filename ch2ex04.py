"""
Program name: Average of three w/ loop
Author: Aiden Dow
Class: CIS-110
Description: Computes an average from three scores/values
Date created/modified: 9/11/2019
Notes:
"""

import datetime

def main():
    print("Calculate Farenheit from Celsius!")
    for i in range(5):
        celsius = float(input("What is the Celsius temperature? "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print("The temperature is", round(fahrenheit, 2), "degrees Fahrenheit.")
        print()

    input("Press the <Enter> key to quit. ")

    print()
    print("Aiden Dow")
    print("CIS-110")
    print(datetime.datetime.now())

main()