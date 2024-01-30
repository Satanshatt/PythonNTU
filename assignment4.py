import numpy as np

print("Exercise 1a: reshaped array", "\n")
arr = np.arange(1,11)
arr= np.reshape(arr, (2, 5), order='F')
print(arr)

print("Exercise 1b: element squared", "\n")
arr = np.square(arr)
print(arr, "\n")

print("Exercise 1c: elements larger than 5", "\n")
for x in arr:
    for y in x:
        if(y>5):
            print(y, "\n")

print("Exercise 1d")
arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
print("Before: ", arr1, arr2, "\n")
arr3 = np.concatenate([arr1, arr2])
print("After: ", arr3, "\n")

print("Exercise 1e: Multiply matrices", "\n")
#matrix1 = np.array([1,2,3,4,5,6])
#matrix2 = np.array([6,5,4,3,2,1])
matrix1 = np.random.randint(5, size=(2,3))
matrix2 = np.random.randint(5, size=(3,2))
#np.reshape(matrix1, (3,2), order='C')
#np.reshape(matrix2, (2,3), order='C')
print("Before: ", matrix1)
print("Before: ", matrix2)
matrix3 = np.dot(matrix1, matrix2)
print("Multiplied matrix, 2 by 2:", matrix3, "\n")

#print("Exercise 1f: Diagonal elements", "\n")
#arrF = np.random.randint(0, size=(5,5))
#print(arrF)



