import pandas as pd 
import numpy as np
import os

df = pd.read_csv("20231030_sample.csv")

#check for missing data 
df.isna()
df.isnull()
df.notna()
#print(df.isna())
#print(df.isnull())
#print(df.notna())

#identify duplicated rows 
duplicates = df.duplicated()
#print(duplicates)

#filter data based on conditions 
filtered_data = df[df['Age']>30]
#print(filtered_data)

#drop rows with missing data or duplicates
df_cleanedMissing = df.dropna()
df_cleanedDuplicates = df.drop_duplicates()
#print(df_cleanedMissing)
#print(df_cleanedDuplicates)

#Assign the column, dropping columns with duplicate values 
df_drop_duplicates = df.drop_duplicates(subset="Height")
#print(df)
#print(df_drop_duplicates)

#fill missing values 
df_filled = df.fillna("YRSA")
#print(df_filled)

#fill missing value by mode
from statistics import mode
df['Age'] = df['Age'].fillna(mode(df['Age']))
mode(df['Age'])
df['Age'].fillna(mode(df['Age']))
df['Age'] = df['Age'].fillna(mode(df['Age']))

#create a new column 
new_data = df['Weight']/((df['Height']/100)**2) #bmi
df['BMI'] = new_data.round(2)
#print(new_data)

#Assignment 1 
print("Assignment 1: \n")
data = pd.DataFrame({
'A': [1, 2, 2, np.nan, 4, 5, np.nan, 8, 9],
'B': [5, 6, 6, 7, 8, 8, 9, 10, 11],
'C': [10, np.nan, 12, 13, 14, 15, 16, 17, np.nan]
})

#median value 
print("Original table:")
print(data)
print("")
data = data.fillna(data.median())

#duplicates in A 
data = data.drop_duplicates(subset="A")

#duplicates in C 
data = data.drop_duplicates(subset="C", keep='last')
print("New table:")
print(data)
print("")

#Assignment 2
print("Assignment 2: \n")
df = pd.DataFrame({
'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
'Price (USD)': [75, 60, 45, 90, 55]
})

print("Original table:")
print(df)
print("")
new_data = df['Price (USD)']*0.85 #EUR to USD
df['EUR'] = new_data.round(2)
df = df[df['EUR']>50]
print("New table:")
print(df)
print("")

#Assignment 3 
print("Assignment 3: \n")
df_tsmc = pd.read_csv(os.getcwd() + "/TSMC_dirty.csv")
df_tsmc.head()

df2 = df_tsmc[df_tsmc.duplicated()]
print("The four duplicate rows")
print(df2)
print("")

print("Data length before removal:")
originalRows = len(df_tsmc.axes[0])
print(originalRows)
print("")

print("Data length after removal:")
cleaned_tsmc = df_tsmc.drop_duplicates()
newRows = len(cleaned_tsmc.axes[0])
print(newRows)
