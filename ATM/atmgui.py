import time
import graphics as g
from keypad import Keypad
import cbutton
import user

class ATMGUI():
	def __init__(self):
		self.win = g.GraphWin("ATM", 500, 600)
		self.win.setCoords(0, 12, 10, 0)
		self.keypad = Keypad()
		self.user = False

		

		self.maintext = g.Text(g.Point(5, 1), "Welcome")
		self.maintext.draw(self.win)

		self.options = []
		self.textboxes = []
		self.buttons = [] 
		self.initializeOptions()

		time.sleep(1)
		self.mainMenu()

	def initializeOptions(self):
		y = 3
		for i in range(4):
			initText = ""
			button = cbutton.CButton(g.Point(1, y), 0.5, initText)
			button.draw(self.win)
			text = g.Text(g.Point(5, y), initText)
			text.draw(self.win)
			self.textboxes.append(text)
			self.buttons.append(button)
			self.options.append(initText)
			y += 2

	def chooseOption(self):
		while True:
			click = self.win.getMouse()
			for button in self.buttons:
				if button.clicked(click):
					opt = self.options[self.buttons.index(button)]
					if opt:
						return opt

	def setOptions(self, options):
		buttonNum = 0
		for x in options:
			button = self.buttons[buttonNum]
			button.activate()
			self.options[buttonNum] = x
			self.textboxes[buttonNum].setText(x)
			buttonNum += 1

	def clearOptions(self):
		for button in self.buttons:
			button.deactivate()

		for box in self.textboxes:
			box.setText("")


	def mainMenu(self):
		self.clearOptions()
		if self.user:
			self.mainOptions()
		else:
			self.loginScreen()

	def mainOptions(self):
		self.maintext.setText("Choose Your Action")
		self.setOptions(["Check Balances", "Withdraw or Deposit", "Transfer", "Log out"])
		opt = self.chooseOption()

		if opt == "Log out":
			user.save(self.user)
			self.user = False
		if opt == "Withdraw or Deposit":
			self.withdrawScreen()
		if opt == "Transfer":
			self.transferScreen()
		if opt == "Check Balances":
			self.checkBalances()
		self.mainMenu()

	def checkBalances(self):
		self.clearOptions()
		checkingBalance = str(self.user.checkings.balance())
		savingsBalance = str(self.user.savings.balance())
		self.setOptions([f"Checkings: ${checkingBalance}", f"Savings: ${savingsBalance}"])
		self.chooseOption()

	def withdrawScreen(self):
		self.clearOptions()
		self.maintext.setText("Withdraw or Deposit?")
		self.setOptions(["Withdraw", "Deposit"])
		mode = self.chooseOption()

		self.maintext.setText("Which Account?")
		account = self.findAccount(self.user, f"to {mode}")

		self.clearOptions()
		self.maintext.setText(f"How much to {mode}?")

		value = float(self.keypad.query())
		if mode == "Deposit":
			account.deposit(value)
		elif mode == "Withdraw":
			account.withdraw(value)

	def transferScreen(self):
		self.clearOptions()

		fromAccount = self.findAccount(self.user, "to transfer from")
		
		self.clearOptions()
		self.maintext.setText("Transfer to which account?")
		
		toAccount = self.findAccount(self.user, "To Transfer to", ["Another Person"])
		save = toAccount == "Another Person"
		if save:
			toUser = self.findUser(True)
			toAccount = self.findAccount(toUser, "To transfer to")

		self.clearOptions()
		self.maintext.setText("Enter amount to transfer")
		value = float(self.keypad.query())
		fromAccount.transfer(value, toAccount)
		
		if save:
			user.save(toUser)


	def loginScreen(self):
		self.maintext.setText("Welcome to your local ATM")
		self.setOptions(["Log in", "Register", "Quit"])

		option = self.chooseOption()
		if option == "Log in":
			self.user = self.findUser()
		elif option == "Register":
			self.register()
		else:
			return
		self.mainMenu()

	def register(self):
		self.clearOptions()
		self.maintext.setText("Thank you for choosing your local ATM")
		self.user = user.createUser()
		time.sleep(2)

		self.maintext.setText("Your UID is " + str(self.user.getUID()))
		self.setOptions(["Continue"])
		self.chooseOption()

		self.maintext.setText("Your PIN is " + str(self.user.getPIN()))
		self.setOptions(["Continue"])
		self.chooseOption()

	def findUser(self, auto=False):
		self.clearOptions()
		self.maintext.setText("Enter User ID")
		uid = self.keypad.query()
		new_user = user.load(uid)

		if not auto:
			self.maintext.setText("Enter your PIN")
			pin = int(self.keypad.query())
		
		if new_user and (auto or new_user.verify(pin)):
			return new_user
	
		self.maintext.setText("Not Valid.\nPlease ensure the account information is correct")
		time.sleep(5)  
		return False

	def findAccount(self, aUser, purpose, otherOptions=False):
		self.clearOptions()
		self.maintext.setText("Choose the account " + purpose)
		options = ["Checkings", "Savings"]

		if otherOptions:
			options += otherOptions

		self.setOptions(options)
		
		option = self.chooseOption()
		if option == "Checkings":
			return aUser.checkings
		elif option == "Savings":
			return aUser.savings
		else:
			return option
		

ATMGUI()