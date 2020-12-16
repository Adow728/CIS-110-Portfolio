# button.py
from graphics import *

class CButton:

	"""A button is a labeled circle in a window.
	It is activated or deactivated with the activate()
	and deactivate() methods. The clicked(p) method
	returns true if the button is active and p is inside it."""

	def __init__(self, center, radius, label):
		""" Creates a circular button, eg:
		qb = Button(myWin, centerPoint, radius, 'Quit') """ 
		self.cx = center.getX()
		self.cy = center.getY()
		self.rsquare = radius * radius
		
		self.circ = Circle(center, radius)
		self.circ.setFill('lightgray')
		self.label = Text(center, label)
		self.deactivate()

	def clicked(self, p):
		"Returns true if button active and p is inside"
		dx = p.getX() - self.cx
		dy = p.getY() - self.cy
		return self.active and dx*dx + dy*dy <= self.rsquare

	def getLabel(self):
		"Returns the label string of this button."
		return self.label.getText()

	def activate(self):
		"Sets this button to 'active'."
		self.active = True
		self.circ.setFill("gray")
		self.circ.setOutline("black")

	def deactivate(self):
		"Sets this button to 'inactive'."
		self.circ.setFill("darkgray")
		self.circ.setOutline("darkgray")
		self.active = False

	def draw(self, win):
		self.circ.draw(win)
		self.label.draw(win)