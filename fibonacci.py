# Fibonacci Finder
# Calculates the nth Fibonacci number
# Aiden Dow
# 9/19/2019 - Revised 12/20/2020

import datetime

def main():
    print("This program calculates the nth Fibonacci value.")
    print()

    n = int(input("Enter the value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr+prev, curr

    print()
    print(f"The {n}th Fibonacci number is", curr) 

main()

print()
print("Aiden Dow")
print(datetime.datetime.now())