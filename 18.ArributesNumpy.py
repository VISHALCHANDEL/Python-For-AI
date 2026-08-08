# Attributes of Numpy array
# ndim
# shape
# size
# dtype
# itemsize

import numpy as np
list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1)
print(array1.ndim)
print(array1.shape)

list2 = [[10, 20, 30, 40], [20, 30, 40, 60]]
array2 = np.array(list2)
print(array2.ndim)
print(array2.shape)

list3 = [[[1, 2, 3, 4],[2, 3, 4, 5]],
         [[7, 8, 9, 10], [11, 12, 13, 14]]]
array3 = np.array(list3)
print(array3.shape)
print(array3.size) 
# number of elements in the array
print(array3.dtype)
print(array3.itemsize)