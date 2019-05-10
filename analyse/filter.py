import numpy as np
import statistics as stat

treshold = 3

def removeFalseData(input_data):
    while(1):
        try:
            input_data.remove(False)
        except ValueError:
            break
    return(input_data)

def removeNegatives(input_data):
    processed_data = []
    for val in input_data:
        if val > 0:
            processed_data.append(val)
    return processed_data

def removeOutliers(input_data):
    #dataset = removeNegatives(input_data)
    processed_data = []
    med = stat.median(input_data)
    avg = np.mean(input_data)
    stdev = np.std(input_data)
    for val in input_data:
        score = abs(val-med)
        if score < 1000:
            processed_data.append(val)
    #    z_score = abs(((val) - avg)/stdev)
    #    if z_score < treshold:
    #        processed_data.append(val)
    return processed_data

def filterData(input_data):
    #print(input_data)
    dataset = removeFalseData(input_data)
    dataset = removeOutliers(dataset)
    #print('filtered')
    #print(dataset)
    return np.mean(dataset)
