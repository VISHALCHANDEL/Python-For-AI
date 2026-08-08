import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
print(array1[0])
print(array1[1])
print(array1[-1])

array2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(array2[1,2])
print(array2[0, :])
print(array2[:,1])