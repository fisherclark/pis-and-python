from gpiozero import Button, LED
from time import sleep
from signal import pause
import tm1637
import random
from rpi_lcd import LCD

display = tm1637.TM1637(clk=21, dio=13)
button = Button(17)
led = LED(18)
rigged = False
lcd = LCD()

def loop():
	if rigged:
		rigged_loop()
		return
	if len(set(random_numbers())) == 1:
		win()
def win():
	lcd.text("You Won!", 2)
	for i in range(10):
		led.on()
		sleep(0.1)
		led.off()
		sleep(0.1)
def rig():
	global rigged
	rigged = True
def rigged_loop():
	if len(set(random_numbers(random.randint(0,1)))) == 1:
		win()
def random_numbers(win = False):
	lcd.clear()
	for i in range(10):
		if i == 9:
			numbers = str((1111**win)*random.randint(0000,9999//(1111**win)))
		else:
			numbers = str(random.randint(0000,9999))
		while len(numbers) < 4:
			numbers = "0" + numbers
		display.show(numbers)
		lcd.text(numbers, 1)
		sleep(0.01)
	return numbers

button.when_pressed = loop

try:
	while True:
		code = input("")
		if code.lower() == "++--<><>ba":
			rig()
except KeyboardInterrupt:
	print("\nDone")
	display.write([0, 0, 0, 0])
	lcd.clear()
