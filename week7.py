import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import math

#1. Use “subplots()” to generate the following plots.

y1 = [1,2,3,4,5]
y2 = [5,4,3,2,1]
fig, ax = plt.subplots(2,2)
ax[0,0].plot(y1)
ax[0,1].plot(y2)
ax[1,0].plot(y2)
ax[1,1].plot(y1)
plt.show()

#2. Create a plot with two lines. One represents y1 = x 
# and the other represents y2 = 0.5x with appropriate labels, axis labels, a title, and a legend. 
# The variable x is a series of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = x
#i2= 0.5*x
i2 = [item * 0.5 for item in x]


plt.plot(i)
plt.title('Assignment 2: Two plots')
plt.plot(i2, 'tab:orange')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#3. Read the data “titanic.csv”. Please generate a histogram of people by age.

data = pd.read_csv('titanic.csv')
dataFrame = pd.DataFrame(data)
ageData = dataFrame["Age"].tolist()

#bins=range(0, 81, 10)
plt.hist(ageData, bins=range(0, 81, 10), edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Number')
plt.title('Assignment 3: Titanic Age Histogram')
plt.show()

#4. Please generate the seaborn heatmap of “my_corr”, 
# and with its data annotation on each cell.

my_corr=data.corr(numeric_only=True)
print(my_corr)
sns.heatmap(my_corr, annot=True)
plt.show()

#5. Set “age_count” to x-axis, and “survived_rate” to y-axis. Generate a line chart of
# age and survival rate, where “age_count” and “survived_rate” are given by following codes.

#age_cut = pd.cut(data['Age'], bins=range(0, 81, 10))
#age_count = age_cut.value_counts()
#age_count.sort_index(inplace=True)
#print(age_count)
#data['Age_Ceil'] = data['Age'].apply(np.ceil)
#survived_count = [len(data[((data['Age_Ceil'] - 1) // 10 == i) & (data['Survived']
#== 1)]) for i in range(8)]
#survived_rate = [survived_count[i] / age_count.tolist()[i] for i in range(8)]

#newAgeList = age_count.index.toList()
#plt.plot.xticks(newAgeList, survived_rate, 'r:o')
#plt.title('Assignment 5')
#plt.xlabel('Age count')
#plt.ylabel('Survived Rate')
#plt.show()


#6. Read the dataset ‘dementia.csv’, where the notations are shown as follows.
#age: age range, total: population by age range, dementia: population with dementia
#Please make a stacked bar chart with the x-axis as the age range and the y-axis as
#the population. Hint: Assign colors to bars using "color='b'" for blue and "color='c'" for cyan.

dataDementia = pd.read_csv('dementia.csv')
dataDementiaFrame = pd.DataFrame(dataDementia)
ageData = dataDementiaFrame["age"].tolist()
populationData = dataDementiaFrame["total"].tolist()
dementiaData = dataDementiaFrame['dementia'].tolist()

fig, ax = plt.subplots()
ax.bar(ageData, dementiaData, color='c')
ax.bar(ageData, populationData, color='b', bottom = dementiaData)
plt.xlabel('Age')
plt.ylabel('Population')
plt.legend()
plt.title('Dementia Demographics')
plt.show()