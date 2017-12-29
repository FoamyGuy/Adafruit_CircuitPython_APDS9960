import board
import busio
import digitalio
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.SCL, board.SDA)
int_pin = digitalio.DigitalInOut(board.A2)
apds = APDS9960(i2c, interrupt_pin=int_pin)

apds.enable_proximity = True
apds.proximity_interrupt_threshold = (10, 175)
apds.enable_proximity_interrupt = True

while True:
    # print the proximity reading when the interrupt pin goes low
    if not int_pin.value:
        prox_value = apds.proximity()
        if prox_value:
            print(prox_value)

        # clear the interrupt
        apds.clear_interrupt()