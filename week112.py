import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from IPython.display import display

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
y=data.target
x_data = pd.DataFrame(data.data, columns=[data.feature_names])

# Load the Breast Cancer dataset
data = load_breast_cancer()
x = data.data
y = data.target

# TODO1: print feature names
print("Assignment 2.1")
features = data.feature_names
print(features)

# TODO2: print target names
print("Assignment 2.2")
target_names = data.target_names
print(target_names)

# TODO 3 Convert data to PyTorch tensors
print("Assignment 2.3")
x = torch.from_numpy(x)
y = torch.from_numpy(y)
display(x,y)

# TODO 4 check the number of "malignant" data and "benign" data
print("Assignment 2.4")
count_0 = torch.count_nonzero(y == 0).item()
count_1 = torch.count_nonzero(y == 1).item()
print("Malignant num:", count_0)
print("Benign num:", count_1)