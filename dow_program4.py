"""
Program name: American Flag
Author: Aiden Dow
Class: CIS-110
Description: This program displays an American flag
Date created/modified: 9/27/2019
Notes:
"""

import datetime
import graphics as g

def main():
    print("This program displays an American flag.")

    win = g.GraphWin("America the Beautiful", 760, 400)
    win.setCoords(0, 0, 1.9, 1)

    stripeWidth = 0.0769
    stripeColor = "red"
    nextY = 0
    for stripe in range(13):
        p1 = g.Point(0, nextY)
        p2 = g.Point(1.9, nextY + stripeWidth)
        r = g.Rectangle(p1, p2)
        r.setFill(stripeColor)
        r.draw(win)

        nextY += stripeWidth
        if stripeColor == "red":
            stripeColor = "white"
        else:
            stripeColor = "red"

    p1 = g.Point(0, 1)
    p2 = g.Point(0.76, 1-0.5385)
    r = g.Rectangle(p1, p2)
    r.setFill("blue")
    r.draw(win)

    t = 1
    x1 = 0.0633
    y1 = t-0.0538+(0.0616/2)
    p1 = g.Point(x1, y1)

    x2 = 0.0633-(0.0616/10)
    y2 = t-0.0538+(0.0616/5)
    p2 = g.Point(x2, y2)

    x3 = 0.0633-(0.0616/2)
    p3 = g.Point(x3, y2)

    x4 = 0.0633-(0.0616/5)
    y4 = t-0.0538-(0.0616/15)
    p4 = g.Point(x4, y4)

    x5 = 0.0633-(0.0616/3)
    y5 = t-0.0538-(0.0616/2)
    p5 = g.Point(x5, y5)

    y6 = t-0.0538-(0.0616/5)
    p6 = g.Point(x1, y6)

    x7 = 0.0633+(0.0616/3)
    p7 = g.Point(x7, y5)

    x8 = 0.0633+(0.0616/5)
    p8 = g.Point(x8, y4)

    x9 = 0.0633+(0.0616/2)
    p9 = g.Point(x9, y2)

    x10 = 0.0633+(0.0616/10)
    p10 = g.Point(x10, y2)

    star = g.Polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    star.setFill("white")
    star.draw(win)

    s2 = star.clone()
    s2.move(0.0633, -0.0538)
    s2.draw(win)

    for x in range(1, 6):
        star = star.clone()
        
        yStar = star
        for y in range(1, 5):
            yStar = yStar.clone()
            yStar.move(0, -0.0538 * 2)
            yStar.draw(win)
        
        star.move(0.0633 * 2, 0)
        star.draw(win)
    yStar = star
    for y in range(1, 5):
        yStar = yStar.clone()
        yStar.move(0, -0.0538 * 2)
        yStar.draw(win)

    for x in range(1, 5):
        s2 = s2.clone()
        
        yStar = s2
        for y in range(1, 4):
            yStar = yStar.clone()
            yStar.move(0, -0.0538 * 2)
            yStar.draw(win)
        
        s2.move(0.0633 * 2, 0)
        s2.draw(win)
    yStar = s2
    for y in range(1, 4):
        yStar = yStar.clone()
        yStar.move(0, -0.0538 * 2)
        yStar.draw(win)        
        
    win.getMouse()
        

    print()
    print("Aiden Dow")
    print("CIS-110")
    print("Program 4")
    print(datetime.datetime.now())

main()
