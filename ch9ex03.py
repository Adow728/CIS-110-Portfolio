"""
Program name: Volleyball Simulation
Author: Aiden Dow
Class: CIS-110
Description: This program simulates a game of volleyball between two
players called "A" and "B". The abilities of each player is
indicated by a probability (a number between 0 and 1) that
the player wins the point when serving. Player A always
has the first serve.
Date created/modified: 11/13/2019
Notes: I added a conversion from percentage to decimal in getInputs.
"""

import datetime
from random import random

def printIntro():
	print("This program simulates a game of volleyball between two")
	print('players called "A" and "B". The abilities of each player is')
	print("indicated by a probability (a number between 0 and 1) that")
	print("the player wins the point when serving. Player A always")
	print("has the first serve.")

def getInputs():
	a = eval(input("What is the prob. player A wins a serve? "))
	if a > 1:
		# Convert percentage to decimal
		a /= 100
	b = eval(input("What is the prob. player B wins a serve? "))
	if b > 1:
		# Convert percentage to decimal
		b /= 100
	n = eval(input("How many games to simulate? "))
	return a, b, n

def simNGames(n, probA, probB):
	winsA = 0
	winsB = 0
	while (winsA + winsB) < n:
		scoreA, scoreB = simOneGame(n, probA, probB)
		if scoreA > scoreB:
			winsA = winsA + 1
		else:
			winsB = winsB + 1
	return winsA, winsB

def printSummary(winsA, winsB):
	n = winsA + winsB
	print("\nGames simulated:", n)
	print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
	print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

def simOneGame(n, probA, probB):
	if n%2 == 0: 
		serving = "B"
	else:
		serving = "A"
	scoreA = 0
	scoreB = 0
	while not gameOver(scoreA, scoreB):
		if serving == "A":
			if random() < probA:
				scoreA = scoreA + 1
			else:
				serving = "B"
		else:
			if random() < probB:
				scoreB = scoreB + 1
			else:
				serving = "A"
	print("A = ", scoreA, " B = ", scoreB)
	return scoreA, scoreB

def gameOver(a, b):
	return (a >= 15 and a-b >= 2) or (b >= 15 and b-a >= 2)

def main():
	printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)

	print()
	print("Aiden Dow")
	print("CIS-110")
	print(datetime.datetime.now())

main()
