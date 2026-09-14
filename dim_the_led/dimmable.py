from gpiozero import PWMLED, RotaryEncoder
from signal import pause

led = PWMLED(12)

rotor = RotaryEncoder(22, 27, wrap=True, max_steps=30)

skip_fraction = 2

def change_led():
	led.value = (rotor.steps/rotor.max_steps)**10
	if rotor.steps >= -rotor.max_steps//skip_fraction and rotor.steps <= 0:
		rotor.steps = rotor.max_steps//skip_fraction
	elif rotor.steps <= rotor.max_steps//skip_fraction and rotor.steps >= 0:
		rotor.steps = -rotor.max_steps//skip_fraction

rotor.when_rotated = change_led

rotor.steps = rotor.max_steps//skip_fraction
print("Press Ctrl+C to stop.")
try:
	pause()
except KeyboardInterrupt:
	print("\n")
