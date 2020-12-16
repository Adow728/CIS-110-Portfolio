import graphics as g 

class Keypad():
    def __init__(self):
        self.win = g.GraphWin("Keypad", 300, 500)
        self.win.setCoords(0, 5, 3, -1)
        self.text = g.Text(g.Point(1.5, -0.5), "")
        self.text.draw(self.win)

        self.enterButton = g.Button("Enter", g.Point(0.05, 4.05), g.Point(2.95, 4.95))
        self.enterButton.activate()
        self.enterButton.draw(self.win)

        buttonNum = 1
        self.buttonKeys = []
        for y in range(3):
            for x in range(3):
                b = g.Button(str(buttonNum), g.Point(x+0.05, y+0.05), g.Point(x+0.95, y+0.95))
                b.draw(self.win)
                b.activate()
                self.buttonKeys.append(b)

                buttonNum += 1
        zeroKey = g.Button("0", g.Point(1.05, 3.05), g.Point(1.95, 3.95))
        zeroKey.activate()
        zeroKey.draw(self.win)
        dotKey = g.Button(".", g.Point(0.05, 3.05), g.Point(0.95, 3.95))
        dotKey.activate()
        dotKey.draw(self.win)
        self.buttonKeys.append(zeroKey)
        self.buttonKeys.append(dotKey)

        self.backButton = g.Button("Back", g.Point(2.05, 3.05), g.Point(2.95, 3.95))
        self.backButton.activate()   
        self.backButton.draw(self.win)     

    def query(self):
        click = g.Point(0, 0)
        ret = ""
        while True:
            if click != None:
                if self.enterButton.clicked(click):
                    break
                elif self.backButton.clicked(click):
                    ret = ret[:-1]
                ret += self.whichButton(click)
            self.text.setText(ret)
            click = self.win.checkMouse()
        self.text.setText("")
        return ret

    def whichButton(self, click):
        for button in self.buttonKeys:
            if button.clicked(click):
                return button.getText()
        return ""

if __name__ == "__main__":
    print(Keypad().query())