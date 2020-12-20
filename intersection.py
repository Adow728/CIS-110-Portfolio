# Intersection
# Computes the intersection between a circle and a line
# Aiden Dow
# 9/26/2019 - Revised 12/20/2020

import datetime
from graphics import GraphWin, Circle, Line, Point
import math

def main():
    # Print introduction 
    print("This program computes the intersection between a circle and a horizontal line")

    # Get radius and y-intercept
    radius = float(input("Please enter the radius of the circle: "))
    y_int = float(input("Please enter the y-intercept of the line: "))

    # Create graphics window
    win = GraphWin("Result Diagram", 500, 500)

    # Set coordinates
    win.setCoords(-10, -10, 10, 10)

    # Draw circle
    circ = Circle(Point(0, 0), radius)
    circ.setWidth(3)
    circ.draw(win)

    # Draw line at y-intercept
    line = Line(Point(-10, y_int), Point(10, y_int))
    line.setWidth(3)
    line.draw(win)

    # Calculate x values for intersection
    x1 = math.sqrt(radius ** 2 - y_int ** 2)
    x2 = 0-x1

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

    

main()

print()
print("Aiden Dow")
print(datetime.datetime.now())