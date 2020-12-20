# Congress Eligibility Checker
# Aiden Dow
# Unknown - Revised 12/20/2020

import datetime

def main():
    print("Are you eligible for Congress? Let's see!")
    age = int(input("How old are you? "))
    residency = int(input("How many years have you been a resident? "))
    if age >= 30:
        if residency >= 9:
            print("Eligible for Senate and House")
        elif residency >= 7:
            print("Eligible for House")
        else:
            print("Not eligible for Congress")
    elif age >= 25:
        if residency >= 7:
            print("Eligible for House")
        else:
            print("Not eligible for Congress")
    else:
        print("Not eligible for Congress")

main()

print()
print("Aiden Dow")
print(datetime.datetime.now())