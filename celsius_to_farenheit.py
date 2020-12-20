# Celsius to Farenheit converter
# Converts up to 5 celsius temperatures into farenheit
# Aiden Dow
# 9/11/2019 - Revised 12/20/2020

import datetime

def main():
    print("Calculate Farenheit from Celsius!")
    for i in range(5):
        celsius = float(input("What is the Celsius temperature? "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print("The temperature is", round(fahrenheit, 2), "degrees Fahrenheit.")
        print()

    input("Press the <Enter> key to quit. ")

    

main()

print()
print("Aiden Dow")
print(datetime.datetime.now())