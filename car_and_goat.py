# Car vs. Goats
# A guess-the-door game demonstrating the Monty Hall problem
# Aiden Dow
# 11/20/2019 - Revised 12/16/2020


import datetime

from random import randrange
from graphics import GraphWin, Button, Point, Text
from time import sleep

def getDoorPick(win, buttons):
	"""Waits for a click in b1, b2, or b3 and returns the number of the door clicked"""
	choice = None
	while choice == None:
		pt = win.getMouse()
		for button in buttons:
			if button.clicked(pt):
				choice = button
					
	choiceNum = int(choice.getText()[-1])
	return choiceNum    

def showGoat(selected, carDoor, messageBox, buttons):
	"""Shows the player a door that is not the car and deactivates it."""
	goat = randrange(1, 4)

	# If the random number is invalid, generate a new one and check it.
	while goat == carDoor or goat == selected:
		goat = randrange(1, 4)
	
	buttons[goat-1].deactivate()
	messageBox.setText("Well, there is a goat at door {}.\nWhich door should I open?".format(goat))

def checkWin(selectedDoor, carDoor, messageBox):
	"""Find whether player won or lost"""
	if selectedDoor == carDoor:
		messageBox.setText("Congratulations! You have won a car")
	else: 
		messageBox.setText("That's a goat.\nThe car was at Door {}".format(carDoor))

def main():
	#set up interface
	win = GraphWin("Find the Car - Avoid the Goats", 350, 225)
	win.setCoords(0, 0.75, 3.25, 3.25)
	b1 = Button("Door 1", Point(0.25, 2.25), Point(1, 1))
	b1.activate()
	b2 = Button("Door 2", Point(1.25, 2.25), Point(2, 1))
	b2.activate()
	b3 = Button("Door 3", Point(2.25, 2.25), Point(3, 1))
	b3.activate()
	buttons = [b1, b2, b3]
	for button in buttons:
		button.draw(win)
	mess = Text(Point(1.625, 2.75), "Find the Car: Avoid the Goats")
	mess.setStyle("bold")
	mess.draw(win)
	
	sleep(2)
	
	# Initialize the variables
	secret = randrange(1, 4)
	mess.setText("Select a door")

	# Player chooses door, computer reveals goat behind another door.
	selected = getDoorPick(win, buttons)
	showGoat(selected, secret, mess, buttons)

	# Player chooses final door, find out whether win or lose
	selected = getDoorPick(win, buttons)
	checkWin(selected, secret, mess)

	win.getMouse()
	

	win.close()    


	print("Aiden Dow")
	print(datetime.datetime.now()) 

if __name__ == '__main__': main()
