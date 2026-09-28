import time
import board
import adafruit_dht
from gpiozero import LED
from datetime import datetime

sensor = adafruit_dht.DHT11(board.D13) # Change the pin number to the data pin of your DHT11 
red = LED(18)
blue = LED(23)

print("time,celsius,fahrenheit,humidity,heat index")

def to_fahrenheit(c):
    # TODO: Assign f where f represents the Farienheit equivalent to the input Celcius c
    f = 1.8*c+32
    return f

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        RH = sensor.humidity
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        T = fahrenheit
        if T > 80:
            heat_idx =  -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH - (T<112 and T>80 and RH < 13)(((13-RH)/4)*((17-abs(T-95.))/17)**0.5) + (T<87 and T > 80 and RH > 85)(((RH-85)/10) * ((87-T)/5))
        elif T < 68:
            heat_idx = T
        else:
            heat_idx = 0.5 * (T + 61.0 + ((T-68.0)*1.2) + (RH*0.094))
        print("{0},{1:0.1f},{2:0.1f},{3:0.1f},{4:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit, RH, heat_idx))
        if heat_idx < 72:
            red.on()
        else:
            blue.on()
        try:
            time.sleep(3.0)
        except KeyboardInterrupt:
            print("done")
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
