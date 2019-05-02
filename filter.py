import numpy as np

treshold = 3

def filterData(inputData):
    dataset = removeOutliers(inputData)
    return np.mean(dataset)


def removeOutliers(inputData):
    dataset = (inputData)
    processedData = []
    mean = np.mean(dataset)
    stdev = np.std(dataset)
    for val in dataset:
        z_score = (val - mean)/stdev
        if z_score < treshold:
            processedData.append(val)
    print(processedData)
    return processedData