from gpiozero import LED
from gpiozero import Button
import time
import random
import signal

red = LED(18)
yellow = LED(23)
green = LED(24)
blue = LED(25)

rbutton = Button(8, bounce_time=0.2)
ybutton = Button(7, bounce_time=0.2)
gbutton = Button(1, bounce_time=0.2)
bbutton = Button(12, bounce_time=0.2)

def button_pressed(button):
    global sequence
    global player_sequence
    global game_over
    if game_over:
        return ""
    if blinking:
        return ""
    if button.pin == rbutton.pin:
        player_sequence.append(1)
        blink_led(1)
    elif button.pin == ybutton.pin:
        player_sequence.append(2)
        blink_led(2)
    elif button.pin == gbutton.pin:
        player_sequence.append(3)
        blink_led(3)
    elif button.pin == bbutton.pin:
        player_sequence.append(4)
        blink_led(4)
    for i in range(len(player_sequence)):
        if not player_sequence[i]==sequence[i]:
            game_over = True
            print(f"Wrong. Score: {len(sequence)-1}\nPress Ctrl+C to exit")
            return ""
    if len(player_sequence) == len(sequence):
        sequence.append(random.randint(1,4))
        player_sequence = []
        blink_leds()

def blink_leds():
    for i in sequence:
        blink_led(i)
    time.sleep(0.5)

def blink_led(lednum):
        global blinking
        blinking = True
        if lednum == 1:
            red.on()
            time.sleep(0.5)
            red.off()
        elif lednum == 2:
            yellow.on()
            time.sleep(0.5)
            yellow.off()
        elif lednum == 3:
            green.on()
            time.sleep(0.5)
            green.off()
        elif lednum == 4:
            blue.on()
            time.sleep(0.5)
            blue.off()
        time.sleep(0.5)
        blinking = False

rbutton.when_pressed = button_pressed
ybutton.when_pressed = button_pressed
gbutton.when_pressed = button_pressed
bbutton.when_pressed = button_pressed

sequence = []
sequence.append(random.randint(1,4))
player_sequence = []
game_over = False
blinking = True
blink_leds()

try:
    signal.pause()
except KeyboardInterrupt:
    print("\nBye!")
