import pandas as pd

#A1=["AAA","AAA","BBB","CCC","DDD"]
#A2=[250,250,500,400,600]
#A3=[1,2,3,1,3]
#df1=pd.DataFrame({"B1":A1,"B2":A2,"B3":A3})

#sorting values and resetting index
#print(df1)
#df1 = df1.sort_values(["B2"],ascending=False)
#print(df1)
#df1 = df1.reset_index(drop=True)
#print(df1)

#count unique values & creating new column 
#df1.loc[:,"B4"] = df1.iloc[:,1] / df1.iloc[:,1].sum()
#print(df1)
#counting unique values 
#df1_counts=df1.loc[:,"B2"].value_counts()
#print(df1_counts)
#df1.loc[:,"B5"]=df1.iloc[:,3].cumsum(axis=0)
#print(df1)

#getting dummies !! converting values to 0 or 1 values 
#dummy1 = pd.get_dummies(df1.iloc[:,2],dtype=bool) #true / false
#dummy2 = pd.get_dummies(df1.iloc[:,2],dtype=int) #0 or 1
#print(dummy1)
#print(dummy2)

#concatenating data
#df2=pd.get_dummies(df1.iloc[:,2],dtype=int)
#print(df2)
#df3=pd.concat([df1,df2],axis=1) #concatinating data df1 and df2
#print(df3)
#renaming to make data values clearer 
#df3_ren = df3.rename(columns={'B1': 'B1_name','B2': 'B2_amount','B3': 'B3_class','B4': 'B4_percentage','B5': 'B5_accumulate',})
#print(df3_ren)

#recalling original table and creating a second one 
#A1=["AAA","BBB","EEE"]
#A6=[101,608,705]
#df4=pd.DataFrame({"B1":A1,"B6":A6})
#print(df4)

#merging data: how= inner (default), outer, left, right, cross. Inner = common values (?)
#df5_outer=pd.merge(df1,df4,on='B1',how='outer')
#print(df5_outer)

#df5=pd.merge(df1,df4,on='B1',how='inner')
#print(df5)

#group by on inner 
#print(df5.groupby(['B1']).count())
#print(df5.groupby(['B1']).mean())
#print(df5.groupby(['B1']).sum())

print("Assignment 1.a: \n")
df = pd.read_csv("health.csv")
data = pd.DataFrame(df)
#print(data)
data.loc[:,"Steps per calorie unit"] = data.loc[:,"steps_per_day"] / data.loc[:,"calories"]
#print(data)

print("Assignment 1.b: \n")
def values(x):
    if x < 2.0:
        return 'low'
    if x > 2.0 and x < 4.5:
        return 'medium'
    if x > 4.5:
        return 'high'

data.loc[:, "Health Index"] = data.loc[:, 'Steps per calorie unit'].apply(values)
print(data)

print("Assignment 1.c: \n")
healthData = data.loc[:, "Health Index"]
dummyData = pd.get_dummies(data.loc[:,"Health Index"],dtype=int)
newData = pd.concat([healthData, dummyData], axis=1)
print(newData)

print("assignment 2 \n")

A1_orders = pd.DataFrame({'B1_OrderID': [1, 2, 3, 4],
'B2_ProductID': [101, 102, 101, 103],
'B3_CustomerID': [201, 202, 201, 203],
'B4_Quantity': [3, 2, 4, 1]})
print(A1_orders)
A2_customers = pd.DataFrame({'B3_CustomerID': [201, 202, 203],
'B5_CustomerName': ['Alice', 'Bob', 'Charlie']})
print(A2_customers)
A3_products = pd.DataFrame({'B2_ProductID': [101, 102, 103],
'B6_ProductName': ['Apples', 'Bananas', 'Cherries'],
'B7_PricePerUnit': [1.0, 0.5, 2.0]})
print(A3_products)

print("assignment 2.a \n")
AA = pd.merge(A1_orders, A3_products, on="B2_ProductID", how='inner')
print(AA)

print("assignment 2.b \n")
AB = pd.merge(AA, A2_customers, on='B3_CustomerID', how ='inner')
print(AB)

print("assignment 2.c \n")
#print(df5.groupby(['B1']).count())
AC = AB.groupby(['B6_ProductName']).count()
print(AC)

print("assignment 2.d \n")
AD = AC.reset_index()
print(AD)