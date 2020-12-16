import bankAccount
from random import randint
def load(uid):
    try:
        with open(uid + ".txt", "r") as userFile:
            content = userFile.readlines()
    except FileNotFoundError:
        print(uid + ".txt", "not found")
        return False

    pin = int(content[0])
    checkings = float(content[1])
    savings = float(content[2])
    return User(int(uid), pin, checkings, savings)

def save(user):
    with open(str(user.uid)+".txt", "w") as userFile:
        checkings = user.checkings.balance()
        savings = user.savings.balance()
        userFile.writelines([str(user.pin) +"\n"+ str(checkings) +"\n"+ str(savings)])

def createUser():
    with open("last.txt", "r") as lastNum:
        content = lastNum.readlines()
        lastUID = int(content[0])
        lastPIN = int(content[1])

    newUID = lastUID + randint(1, 7)
    newPIN = lastPIN - randint(1, 7)

    if newUID > 9999 or newPIN < 1111: 
        raise MemoryError("Data limits exceeded")

    with open("last.txt", "w") as lastNum:
        lastNum.writelines([str(newUID)+"\n"+str(newPIN)])

    with open(str(newUID) + ".txt", "w") as newUserFile:
        newUserFile.writelines([str(newPIN) +"\n"+ "0" +"\n"+ "0"])

    return User(newUID, newPIN, 0, 0)

class User():
    def __init__(self, uid, pin, checkings_balance, savings_balance):
        self.uid = uid
        self.pin = pin
        self.checkings = bankAccount.Account(checkings_balance)
        self.savings = bankAccount.Account(savings_balance)

    def verify(self, pin):
        return pin == self.pin

    def getPIN(self):
        return self.pin

    def getUID(self):
        return self.uid
    