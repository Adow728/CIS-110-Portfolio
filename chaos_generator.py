# Chaos Generater
# This program illustrates a chaotic function
# Aiden Dow
# 9/4/2019 - Revised 12/16/2020

def main():
    print("This program illustrates a chaotic function")

    # fetch and verify user input
    x1 = float(input("Enter the first seed between 0 and 1: "))
    while not (x1 > 0 and x1 < 1):
        x1 = float(input("Invalid. Please enter a seed between 0 and 1: "))

    x2 = float(input("Enter the second seed between 0 and 1: "))
    while not (x2 > 0 and x2 < 1):
        x2 = float(input("Invalid. Please enter a seed between 0 and 1: "))

    # prepare display
    print()
    print("input {:7.6f} | {:7.6f}".format(x1, x2))
    print("-------------------------")

    # formula
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("      {:7.6f} | {:7.6f}".format(x1, x2))

main()