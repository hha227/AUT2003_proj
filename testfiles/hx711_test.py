#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
import time
from hx711 import HX711  # import the class HX711
from hx711 import outliers_filter
try:
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'

    # If you do not pass any argument 'gain_channel_A' then the default value is 128
    # If you do not pass any argument 'set_channel' then the default value is 'A'
    # you can set a gain for channel A even though you want to currently select channel B
    hx = HX711(
        dout_pin=13, pd_sck_pin=19, gain_channel_A=128, select_channel='A')

    hx.set_gain_A(
        gain=64)  # You can change the gain for channel A  at any time.
    hx.select_channel(
        channel='A')  # Select desired channel. Either 'A' or 'B' at any time.

    while(1):
        data = hx.get_raw_data_mean(readings=30)
        print(data)
        #time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup
