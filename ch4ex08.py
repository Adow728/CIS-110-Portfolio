"""
Program name: Properties of a line
Author: Aiden Dow
Class: CIS-110
Description: This program calculates the endpoints of a line
Date created/modified: 9/26/2019
Notes:
"""

import datetime
# Import graphics
from graphics import *

# Import math
import math

def main():
    # Print introduction
    print("This program calculates the endpoints of a line") 

    # Create graphics window
    win = GraphWin("Properties of a line", 500, 500)

    # Prompt user to click 2 times anywhere in box  to create a line
    text = Text(Point(250, 475), "Click on endpoints of a line segment")
    text.draw(win)

    # Get x, y for click 1
    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()

    # Get x, y for click 2
    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()

    # Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Draw line
    line = Line(p1, p2)
    line.draw(win)

    # Calculate and mark center
    center = Circle(Point(x1 + (dx / 2), y1 + (dy / 2)), 2)
    center.setFill("cyan")
    center.draw(win)


    # Calculate slope
    slope = round(dy / dx, 2)

    # Calculate length
    length = round(math.sqrt(dx ** 2 + dy ** 2), 2)

    # Print length and slope
    string = "Length: " + str(length) + " Slope: " + str(slope)
    text.setText(string)

    # Close graphics window on mouse click
    win.getMouse()

    print()
    print("Aiden Dow")
    print("CIS-110")
    print(datetime.datetime.now())

main()
