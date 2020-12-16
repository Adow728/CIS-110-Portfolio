"""
Program name: Intersection
Author: Aiden Dow
Class: CIS-110
Description: This program computes the intersection between a circle and a line
Date created/modified: 9/26/2019
Notes: All measuments in pixels
"""

import datetime
# Import graphics
from graphics import *
# Import math
import math

def main():
    # Print introduction 
    print("This program computes the intersection between a circle and a line")

    # Get radius and y-intercept
    radius = int(input("Please enter the radius of the circle: "))
    y_int = int(input("Please enter the y-intercept of the line: "))

    # Create graphics window
    win = GraphWin("Result Diagram", 500, 500)

    # Set coordinates
    win.setCoords(-10, -10, 10, 10)

    # Draw circle
    circ = Circle(Point(0, 0), radius)
    circ.draw(win)

    # Draw line at y-intercept
    line = Line(Point(-10, y_int), Point(10, y_int))
    line.draw(win)

    # Calculate x values for intersection
    x1 = math.sqrt(radius ** 2 - y_int ** 2)
    x2 = 0-math.sqrt(radius ** 2 - y_int ** 2)

    # Display x values
    print("X values of the intersections ", x1, x2)

    # Plot points for intersection
    p1 = Point(x1, y_int)
    p1.setOutline("red")
    p1.draw(win)

    p2 = Point(x2, y_int)
    p2.setOutline("red")
    p2.draw(win)

    # Close graphics window after mouse click
    win.getMouse()

    print()
    print("Aiden Dow")
    print("CIS-110")
    print(datetime.datetime.now())

main()
