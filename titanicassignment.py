import numpy as np
import pandas as pd

#reading titanic.csv and creating a file with the data
data = pd.read_csv('titanic.csv')

dataFrame = pd.DataFrame(data)
print(dataFrame)

#print 10 first row
data_first_10 = data.head(10) 
print(data_first_10)

survivingPassengers = dataFrame["Survived"].value_counts()[1]
survivalRate = survivingPassengers/dataFrame["PassengerId"].size
print(survivalRate)

print(dataFrame.isnull().sum())
missingData = dataFrame.isnull().sum()
removeindex = missingData[missingData > 300].index
titanicData2 = dataFrame.drop(columns=removeindex)
print(titanicData2)
print(titanicData2["Age"].isna().sum()) #isna = is not available