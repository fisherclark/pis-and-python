from gpiozero import Button
from signal import pause
button = Button(12)

def hi():
    print("Hi!")

button.when_pressed = hi

pause()
