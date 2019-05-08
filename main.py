import dbcom as db
import numpy as np
import gettemp as t_sensor
import loadcell_config as loadcell
import time
import filter

#Configuration paramters
sample_time = 60  #Seconds between evry sample
average_time = 3600 #Seconds between avaraging data and uploading to DB
no_load_samples = 30 #Number of loadcell samples

#Function definitions
def getTempSample():
    temp = t_sensor.gettemp()
    return temp

def getGravSample():
    raw_data = loadcell.getreadings()
    filtered_data = filter.filterData(raw_data)
    return filtered_data

#Init
current_brew = db.getCurrentBrewId()
start_sample_time = time.time()
start_average_time = time.time()
temp_samples = []
grav_samples = []

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

    #Get
