#!/usr/bin/env python3
import RPi.GPIO as GPIO # Importerer GPIO
GPIO.setmode(GPIO.BCM)  # BCM-nummerering av pinner
from hx711 import HX711 # Importerer klassen for HX711
                        # Fra https://github.com/gandalf15/HX711.git


# Initierer ny instans av lastcelleklasse.
hx = HX711(
    dout_pin=13, pd_sck_pin=19, gain_channel_A=128, select_channel='A')
hx.reset()                          # Reset HX711 før start
hx.set_gain_A(gain=64)              # Gain for kanal A (64 / 128)
hx.select_channel(channel='A')      # Velger kanal A
hx.zero(readings=30)                # Nullstiller lastcelleverdi

def getreading():                  # Returnerer én måling
    reading = hx._read()
    return reading

def getreadings(nr):
    readings = []
    for i in range(nr):
        readings.append(hx._read())
    return readings


def get_density(hxdata, scale_ratio, OG, OG_data ):   # Regner massetetthet fra data
    density=OG-(scale_ratio*(OG_data-hxdata))
    return density
