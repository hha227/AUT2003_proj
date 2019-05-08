import numpy as np

treshold = 3

def removeFalseData(input_data):
    while(1):
        try:
            input_data.remove(False)
        except ValueError:
            break
    return(input_data)

def removeOutliers(input_data):
    dataset = input_data
    processed_data = []
    avg = np.mean(dataset)
    stdev = np.std(dataset)
    for val in dataset:
        z_score = (val - avg)/stdev
        if z_score < treshold:
            processed_data.append(val)
    return processed_data

def filterData(input_data):
    dataset = removeFalseData(input_data)
    dataset = removeOutliers(dataset)
    return np.mean(dataset)
