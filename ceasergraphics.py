import graphics as g

ENCODE = "encode"
DECODE = "decode"

def ceaser_cipher(message, shift, mode):
    ret = ""
    if mode == DECODE:
        shift *= -1

    for letter in message.upper():
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(letter) - 64
            num += shift
            num %= 26
            
            num += 64
            ret += chr(num)
        else:
            ret += letter
    return ret
        

win = g.GraphWin("Ceaser Cipher", 400, 300)
win.setCoords(-5, 0, 5, 10)

message_box = g.Entry(g.Point(-0.75, 9), 35)
message_box.draw(win)
message_box.setText("Message")
shift_box = g.Entry(g.Point(4, 9), 5)
shift_box.draw(win)
shift_box.setText("Shift")

encode_button = g.Rectangle(g.Point(-4, 8), g.Point(0, 4))
encode_text = g.Text(g.Point(-2, 6), "ENCODE")
encode_button.draw(win)
encode_text.draw(win)

decode_button = g.Rectangle(g.Point(4, 8), g.Point(0, 4))
decode_text = g.Text(g.Point(2, 6), "DECODE")
decode_button.draw(win)
decode_text.draw(win)

output_text = g.Text(g.Point(0, 2), "OUTPUT")
output_text.draw(win)

while win.isOpen():
    click = win.getMouse()
    p1 = encode_button.getP1()
    p2 = encode_button.getP2()

    out = "click a button"
    if click.getX() < max(p1.getX(), p2.getX()) and click.getX() > min(p1.getX(), p2.getX()) \
        and click.getY() < max(p1.getY(), p2.getY()) and click.getY() > min(p1.getY(), p2.getY()):
        out = ceaser_cipher(message_box.getText(), int(shift_box.getText()), ENCODE)

    p1 = decode_button.getP1()
    p2 = decode_button.getP2()
    if click.getX() < max(p1.getX(), p2.getX()) and click.getX() > min(p1.getX(), p2.getX()) \
        and click.getY() < max(p1.getY(), p2.getY()) and click.getY() > min(p1.getY(), p2.getY()):
        out = ceaser_cipher(message_box.getText(), int(shift_box.getText()), DECODE)



    output_text.setText(out)


