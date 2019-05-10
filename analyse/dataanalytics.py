import hx711 as hx
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

num_readings = 10000

hx = hx.HX711(
    dout_pin=13, pd_sck_pin=19, gain_channel_A=128, select_channel='A')

# Get readings
def getreadings(nr):
    readings = []
    for i in range(nr):
        readings.append(hx._read())
        print(i)
    return readings
print('reading..')
readings = getreadings(num_readings)

# Save to textfile
f = open("dataset5_totang.py", "a")
f.write('data = [')
for val in readings:
    f.write('{}, '.format(val))
f.write(']')
f.close()
