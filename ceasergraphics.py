# Ceaser Cipher GUI
# Aiden Dow
# Unknown - Revised 12/20/2020

import graphics as g
import datetime

ENCODE = "encode"
DECODE = "decode"

def ceaser_cipher(message, shift, mode):
    """Encode or decode a ceaser cipher message"""

    ret = ""

    # Decoding is just going the other way from encoding.
    if mode == DECODE:
        shift *= -1

    for letter in message.upper():
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # Turn the char into a number and apply the shift.
            # We have to shift the number down so we can use the mod operator
            num = ord(letter) - 64
            num += shift
            num %= 26
            
            # Shift the number back up to a char ascii code, then convert into a letter and add to the string
            num += 64
            ret += chr(num)
        else:
            ret += letter
    return ret
        
# Create the window
win = g.GraphWin("Ceaser Cipher", 400, 300)
win.setCoords(-5, 0, 5, 10)

# Generate the interface
message_box = g.Entry(g.Point(-0.75, 9), 35)
message_box.draw(win)
message_box.setText("Message")

shift_box = g.Entry(g.Point(4, 9), 5)
shift_box.draw(win)
shift_box.setText("Shift")

encode_button = g.Button( "ENCODE", g.Point(-4, 8), g.Point(0, 4))
encode_button.draw(win)
encode_button.activate()

decode_button = g.Button("DECODE", g.Point(4, 8), g.Point(0, 4))
decode_button.draw(win)
decode_button.activate()

quit_button = g.Button("Quit", g.Point(3, 0.25), g.Point(4.75, 1.25))
quit_button.draw(win)
quit_button.activate()

output_text = g.Text(g.Point(0, 2), "OUTPUT")
output_text.draw(win)

# Check to see if a button is clicked
while win.isOpen():
    click = win.getMouse()
    out = "click a button"
    
    if click and encode_button.clicked(click):
        out = ceaser_cipher(message_box.getText(), int(shift_box.getText()), ENCODE)

    if click and decode_button.clicked(click):
        out = ceaser_cipher(message_box.getText(), int(shift_box.getText()), DECODE)

    if quit_button.clicked(click):
        break

    output_text.setText(out)

print("Aiden Dow")
print(datetime.datetime.now())