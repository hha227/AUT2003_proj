import dbcom as db
import numpy as np
import gettemp as t_sensor
import loadcell_config as loadcell
import time
import filter
import interface
import RPi.GPIO as GPIO


#Configuration paramters
sample_time = 10  #Seconds between evry sample
average_time = 60 #Seconds between avaraging data and uploading to DB
no_load_samples = 30 #Number of loadcell samples



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
print('Initializing')
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

print('Init complete')



#Take initial spot sample
print('Sampling')
initial_temp = getTempSample()
initial_grav = getGravSample()
db.addMeasurement(current_brew_id, initial_grav, initial_temp) #Add measurement to DB
print('Sampling complete')
print('Running')

#Main loop
while (1):
    time_now = time.time()

    #Take sample if sample-time is reached
    if (time_now - start_sample_time) > sample_time:
        print('Sampling')
        #TODO: Insert code for displaying a "busy"-screen
        try:
            temp_samples.append(getTempSample())
        except:
            print('Temperature sensor offline')
            print('Using target temp')
            temp_samples.append(target_temp)
        grav_samples.append(getGravSample())
        start_sample_time = time_now
        print('Running')

    #Average samples and insert to DB if averaging time is reached
    if (time_now - start_average_time) > average_time:
        print('Averaging samples')
        db.addMeasurement(current_brew_id, np.mean(grav_samples), np.mean(temp_samples)) #Add averagde of measurements from last hour to DB
        print('Data added to database')
        start_average_time = time_now
        temp_samples.clear()
        grav_samples.clear()

        print('Running')


    #Update screen
    if view==0:
        try:
            interface.disp1(temp_samples[-1], brew_name, brewer, grav_samples[-1], target_temp)
        except IndexError:
            interface.disp1(initial_temp, brew_name, brewer, initial_grav, target_temp)
    elif view==1:
        try:
            interface.disp2(OG, FG, grav_samples[-1])
        except IndexError:
            interface.disp2(OG, FG, initial_grav)

#
#    if len(temp_samples):
#        if view==0:
#            interface.disp1(temp_samples[-1], brew_name, grav_samples[-1], target_temp)
#
#        elif view==1:
#            interface.disp2(OG, FG, grav_samples[-1])
#
