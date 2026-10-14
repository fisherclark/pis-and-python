from gpiozero import LED, Button
from signal import pause

button = Button(17)
led = LED(18)

button.when_pressed = led.on
button.when_released = led.off

try:
	pause()
except KeyboardInterrupt:
	print("\nBye")
