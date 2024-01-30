import numpy as np

A = np.random.randint((2,3))
B = np.random.randint((3,2))
C = np.dot(A, B, out=None)
print(C.transpose())
print(np.dot(B.transpose(), A.transpose(), out=None))