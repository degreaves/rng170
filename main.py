def on_button_pressed_a():
    global x
    x = a * (x + b) % c
    basic.show_number(x)
input.on_button_pressed(Button.A, on_button_pressed_a)

x = 0
c = 0
b = 0
a = 0
a = 7
b = 12
c = 17
x = 19

def on_forever():
    pass
basic.forever(on_forever)
