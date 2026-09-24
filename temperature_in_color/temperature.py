import time
import board
import adafruit_dht
import gpiozero
from datetime import datetime

sensor = adafruit_dht.DHT11(board.D13)
red = gpiozero.LED(18)
blue = gpiozero.LED(23)

print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    f = c*1.8+32
    return f

delete = input("Delete past temperature.csv file?(y/n) ")

if delete.strip().lower() == "y":
	with open("temperature.csv", "w") as file:
		file.write("")

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        print("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
        if fahrenheit > 72:
            red.on()
        elif fahrenheit == 72:
            red.on()
            blue.on()
        else:
            blue.on()
        with open("temperature.csv", "a") as file:
            file.write("{0},{1:0.1f}\n".format(current_time.strftime("%H:%M:%S"), fahrenheit))

        try:
            time.sleep(3.0)
        except KeyboardInterrupt:
            break
        red.off()
        blue.off()

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
