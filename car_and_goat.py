"""
Program name: Doors
Author: Aiden Dow
Class: CIS-110
Description: A guess-the-door game
Date created/modified: 11/20/2019
Notes:
"""

import datetime

from random import randrange
from graphics import *
from button import Button
from time import sleep

def getDoorPick(win, buttons):
	# waits for a click in b1, b2, or b3 and returns the number of the door clicked
	choice = None
	while choice == None:
		pt = win.getMouse()
		for button in buttons:
			if button.clicked(pt):
				choice = button
					
	choiceNum = int(choice.getLabel()[-1])
	return choiceNum    

def showGoat(carDoor, selected, messageBox, buttons):
	goat = randrange(1, 4)
	while goat == carDoor or goat == selected:
		goat = randrange(1, 4)
	buttons[goat-1].deactivate()
	messageBox.setText("Well, there is a goat at door {}.\nWhich door should I open?".format(goat))

def checkWin(selectedDoor, carDoor, messageBox):
	if selectedDoor == carDoor:
		messageBox.setText("Congratulations! You have won a car")
	else: 
		messageBox.setText("That's a goat.\nThe car was at Door {}".format(carDoor))

def main():
	#set up interface
	win = GraphWin("Three Button Monte", 350, 250)
	win.setCoords(0.5,1, 3.5, 3)
	b1 = Button(win, Point(1,2.25), .75, 1, "Door 1")
	b1.activate()
	b2 = Button(win, Point(2,2.25), .75, 1, "Door 2")
	b2.activate()
	b3 = Button(win, Point(3,2.25), .75, 1, "Door 3")
	b3.activate()
	buttons = [b1, b2, b3]
	mess = Text(Point(2, 1.5), "Find the Car: Avoid the Goats")
	mess.setStyle("bold")
	mess.draw(win)
	
	sleep(2)
	

	secret = randrange(1, 4)
	mess.setText("Select a door")
	selected = getDoorPick(win, buttons)
	showGoat(secret, selected, mess, buttons)
	selected = getDoorPick(win, buttons)
	checkWin(selected, secret, mess)

	win.getMouse()
	

	win.close()    


	print()
	print("Aiden Dow")
	print("CIS-110")
	print(datetime.datetime.now()) 

if __name__ == '__main__': main()
