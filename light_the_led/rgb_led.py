from gpiozero import RGBLED
from time import sleep

# Set pin numbers
r_pin = 16
g_pin = 20
b_pin = 21

led = RGBLED(red=r_pin, green=g_pin, blue=b_pin)

print("Answer with 0-255")
r_bright = float(input("Red: "))/255
g_bright = float(input("Green: "))/255
b_bright = float(input("Blue: "))/255

led.color = (r_bright, g_bright, b_bright)
sleep(5)
led.color = (0, 0, 0)
