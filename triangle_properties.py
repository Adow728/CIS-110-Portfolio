# Properties of a Triangle
# Calculates the corners, perimeter, and area of a user-defined triangle
# Aiden Dow
# Unknown - Revised 12/20/2020

import datetime

import math
from graphics import Point, Polygon, GraphWin, Text

def square(x):
    return x * x

def distance(p1, p2):
    """Returns the distance between two points"""
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def triArea(leg1, leg2, leg3):
    """Returns the area of a triangle, given the lengths of the three sides"""
    s = (leg1 + leg2 + leg3) / 2.0
    return math.sqrt(s * (s - leg1) * (s - leg2) * (s - leg3))

def main():
    win = GraphWin("Draw a Triangle",500,500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

        
    # Calculate the perimeter of the triangle
    d1 = distance(p1,p2)
    d2 = distance(p2,p3)
    d3 = distance(p3,p1)
    message.setText("perimeter: %0.2f  area: %0.2f "
                    % ((d1+d2+d3),triArea(d1,d2,d3)))

    # Wait for another click to exit
    win.getMouse()

main()

print("Aiden Dow")
print(datetime.datetime.now())