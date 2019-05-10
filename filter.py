import numpy as np
import statistics as stat

def removeFalseData(input_data):
    while(1):
        try:
            input_data.remove(False)
        except ValueError:
            break
    return(input_data)

def removeOutliers(input_data):
    processed_data = []
    med = stat.median(dataset)
    for val in input_data:
        score = abs(val-med)
        if score < 500:
            processed_data.append(val)
    return processed_data

def filterData(input_data):
    dataset = removeFalseData(input_data)
    dataset = removeOutliers(dataset)
    return np.mean(dataset)
