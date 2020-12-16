"""
Program name: Bank Account
Author: Aiden Dow
Class: CIS-110
Description: An object modeling a bank account
Date created/modified: 11/21/2019
Notes:
"""

import datetime
class Account():
    """An object modeling a bank account"""

    def __init__(self, balance):
        self.bal = float(balance)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount may not be smaller than zero. Please use the withdraw function")
        self.bal += amount
        return amount
    
    def withdraw(self, amount):
        self.bal -= amount
        if self.bal < 0:
            raise ValueError("Account overdrawn")
        return amount

    def transfer(self, amount, account):
        self.withdraw(amount)
        account.deposit(amount)
        return amount

    def balance(self):
        return self.bal

def main():
    savings = Account()
    checking = Account()
    cash = 0.00
    print("You have ${} cash, ${} in your savings, and ${} in your checking account".format(cash, savings.balance(), checking.balance()))
    checking.deposit(500)
    savings.deposit(100)
    checking.transfer(150, savings)
    cash += checking.withdraw(250)
    cash += savings.withdraw(100)
    savings.transfer(75, checking)
    print("You have ${} cash, ${} in your savings, and ${} in your checking account".format(cash, savings.balance(), checking.balance()))
    
    print()
    print("Aiden Dow")
    print("CIS-110")
    print("Program 10")
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()
