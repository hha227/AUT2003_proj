import dbcom as db
import numpy as np
import gettemp as t_sensor
import loadcell_config as loadcell
import time
import filter
import interface
import RPi.GPIO as GPIO

#Konfigurerer interrupt ved tastetrykk
button1=11  # Input for knapp
button2=9   # Input for knapp
def setmode0(pin):
    global view
    view=0 # Endre skjermvisning
def setmode1(pin):
    global view
    view=1 # Endre skjermvisning
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button1, GPIO.RISING, callback=setmode0)
GPIO.add_event_detect(button2, GPIO.RISING, callback=setmode1)

#Configuration paramters
sample_time = 10  #Seconds between evry sample
average_time = 60 #Seconds between avaraging data and uploading to DB
no_load_samples = 30 #Number of loadcell samples

view=0


#Function definitions
def getTempSample():
    temp = t_sensor.gettemp()
    return temp

def getGravSample():
    raw_data = loadcell.getreadings(no_load_samples)
    filtered_data = filter.filterData(raw_data)
    return filtered_data

#Init
current_brew_id = db.getCurrentBrewId()
brew_name = db.getBrewInfo('BrewName', current_brew_id)
brewer = db.getBrewInfo('Brewer', current_brew_id)
target_temp = db.getBrewInfo('TargetTemp', current_brew_id)
OG = db.getBrewInfo('OG', current_brew_id)
FG = db.getBrewInfo('TargetFG', current_brew_id)
start_sample_time = time.time()
start_average_time = time.time()
temp_samples = []
grav_samples = []
print(1)

#Take initial spot sample
db.addMeasurement(current_brew_id, getGravSample(), getTempSample()) #Add measurement to DB


#Main loop
while (1):
    time_now = time.time()


    #Take sample
    if (time_now - start_sample_time) > sample_time:
        temp_samples.append(getTempSample())
        grav_samples.append(getGravSample())
        start_sample_time = time_now

    if (time_now - start_average_time) > average_time:
        db.addMeasurement(current_brew_id, np.mean(grav_samples), np.mean(temp_samples)) #Add averagde of measurements from last hour to DB
        start_average_time = time_now
        temp_samples.clear()
        grav_samples.clear()
    #Get
    if len(temp_samples):
        if view==0:
            interface.disp1(temp_samples[-1], brew_name, brewer, grav_samples[-1], target_temp)

        elif view==1:
            interface.disp2(OG, FG, grav_samples[-1])
