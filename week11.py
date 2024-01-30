import numpy as np
import pandas as pd
from sklearn import metrics

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
y=data.target
x_data = pd.DataFrame(data.data, columns=[data.feature_names])

# normalization
x = (x_data - x_data.min())/(x_data.max()-x_data.min())

# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=1)

# 1 knn model
print("Assignment 1.1")
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(x_train,y_train)

prediction = model.predict(x_test)
print(" accuracy_score: {} ".format(metrics.accuracy_score(y_test,prediction)))

# 2 LogisticRegression
print("Assignment 1.2")
from sklearn.linear_model import LogisticRegression
model2 = LogisticRegression(C=0.1)
model2.fit(x_train, y_train)
prediction2 = model2.predict(x_test)
print(" accuracy_score: {} ".format(metrics.accuracy_score(y_test,prediction2)))

# 3 DecisionTreeClassifier
print("Assignment 1.3")
from sklearn.tree import DecisionTreeClassifier
model3 = DecisionTreeClassifier(max_depth = 3)
model3.fit(x_train, y_train)
prediction3 = model3.predict(x_test)
print(" accuracy_score: {} ".format(metrics.accuracy_score(y_test,prediction3)))

