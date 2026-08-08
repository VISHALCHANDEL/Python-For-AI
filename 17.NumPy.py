# NumPy is numerical Python that is widely used for scientific computing, data analysis, and numerical computing tasks

# Homogeneous data
import numpy as np

list1 = [10, 20, 30, 40, 60, 90, 80]
array1 = np.array(list1)
# If any one is char or float then all will be converted
for i in array1:
    print(i)

list2 =   [[10, 20 ,30], [40, 50, 60], [70, 80, 90]]

# print(list2)

# arange(1,8)
# means will give elements like 1 2 3 4 5 ... 7


array1 = np.arange(11, 17).reshape((2, 3))
print(array1)

# for twod array
# array1 = np.ones((4, 2))  rows and cols
 
# np.array(list1, dtype = int) for char 'U32'

array2 = np.arange(1,9)
print(array2)
