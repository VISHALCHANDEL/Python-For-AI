import numpy as np

array = np.arange(10, 60, 10)
print(array)

array1 = np.arange(10,60, 10).reshape(5,1)
print(array1)

array2 = np.arange(1, 10).reshape(3, 3)
print(array2)

rows = array2.shape[0]
cols = array2.shape[1]

print("Rows: ", rows)
print("Cols: ", cols)

