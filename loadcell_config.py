#!/usr/bin/env python3
import RPi.GPIO as GPIO # Importerer GPIO
from hx711 import HX711 # Importerer klassen for HX711

GPIO.setmode(GPIO.BCM)  # BCM-nummerering av pinner

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
        

def get_density(OG, hxdata, scale_ratio):   # Regner massetetthet fra data
    density=OG(1-scale_ratio*hxdata)
    return density
while(1):
    print(getreadings())
