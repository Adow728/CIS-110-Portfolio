# Cost of a pizza
# This program calculates costs related to a pizza
# Aiden Dow
# Unknown - Revised 12/16/2020

import math

def main():
    print("This program computes the cost per slice and per square inch of a round pizza .")
    print()

    # Input
    diam = float(input("Enter the diameter of the pizza (in inches): "))
    price = float(input("Enter the price of the pizza: $"))

    # Calculate the area and cost per square inch
    area = math.pi * (diam / 2.0) ** 2
    cost = price / area
    print()
    
    # Output
    print("Each slice (assuming 8 slices) costs $", round(price/8, 2))
    print("The cost is $", round(cost, 2), " per square inch of pizza.")

main()
