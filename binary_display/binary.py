from gpiozero import LEDBoard

leds = LEDBoard(18, 23, 24, 25, 12, 16, 20, 21)

def to_binary(n):
	if n == 0:
		return ""
	elif n < 0:
		compliment = ""
		unnotted = to_binary((-1*n)-1)
		while len(unnotted) < 8:
			unnotted = "0" + unnotted
		for i in unnotted:
			compliment = compliment + str(1-int(i))
		return compliment
	else:
		binary = to_binary(n // 2) + str(n % 2)
		return binary
def change_leds(binary_str):
	vals = []
	for i in range(len(binary_str)):
		vals.append(int(binary_str[i]))
	leds.value = (vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7])
try:
	while True:
		while True:
			try:
				decimal = int(input("Decimal number: "))
				break
			except ValueError:
				print("Must be an integer")
		binary = to_binary(decimal)
		while len(binary) < 8:
			binary = "0" + binary
		change_leds(binary[-8:])
		print(f"Binary: {binary}")
except KeyboardInterrupt:
	print("\nBye!")
