input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    x = a * (x + b) % c
    basic.showNumber(x)
})
let x = 0
let c = 0
let b = 0
let a = 0
a = 7
b = 12
c = 17
x = 19
basic.forever(function on_forever() {
    
})
