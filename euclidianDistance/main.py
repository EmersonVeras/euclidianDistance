import pandas as pd
import math

data = pd.read_csv("circlePoints.csv", sep = ';')

def toSweepData(data):
    dataRange = len(data) - 1
    vector = []
    
    for i in range(dataRange):
        j = i + 1
        distanceResult = math.sqrt((data['X'][j] - data['X'][i])**2 + (data['Y'][j] - data['Y'][i])**2)
        vector.append(distanceResult)
    
    
    return sum(vector)
        
print(toSweepData(data))
     
# print(calcDistanceEuclidian(data))

# def euclidianDistance(data):
    
#     distanceResult = math.sqrt((data['X'][1] - data['X'][0])**2 + (data['Y'][1] - data['Y'][0])**2)
#     return distanceResult


# print(euclidianDistance(data))
