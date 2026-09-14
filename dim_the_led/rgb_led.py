from gpiozero import RotaryEncoder, RGBLED, Button, LED
from colorzero import Color
from signal import pause

led = RGBLED(red = 16, green=20, blue=21)
red = LED(12)
switch = Button(17)
rotor = RotaryEncoder(22, 27, wrap=True, max_steps=45)

def change_led():
	led_color = Color.from_hls(1-((rotor.steps+rotor.max_steps)/(2*rotor.max_steps)), 0.5, 1)
	led.color = (led_color.red**2.5,led_color.green**2.5,led_color.blue**2.5)

rotor.when_rotated = change_led
switch.when_pressed = red.on
switch.when_released = red.off
led.color = (1,0,0)
rotor.steps = -rotor.max_steps
print("Press Ctrl+C to stop.")
try:
	pause()
except KeyboardInterrupt:
	print("\n")
