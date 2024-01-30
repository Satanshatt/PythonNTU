import numpy as np

print("Exercise 2")

heightArray = np.random.randint(150, 190, size=(5))
weightArray = np.random.randint(40, 100, size=(5))
bmiArray = weightArray/(heightArray/100)**2
bmiArray = np.round(bmiArray, 2)
print(heightArray)
print(weightArray)
print(bmiArray)
