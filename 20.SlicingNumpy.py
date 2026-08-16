# In one dimensional Array

import numpy as np
# To check in one dimensional array
array1 = np.array([10, 20, 30, 40, 50, 60, 70])
print(array1[1:3])
print(array1[1:6:2])
print(array1[-1:-4:-1])
# Here -1 in last is mandatory unless it will error
print(array1[::2])
print(array1[::1])


# To check in two dimensional array


array1 = np.array([[15,16,17],
                   [25,26,27],
                   [35,36,37],
                   [45,46,47]])
print(array1[1,])
print(array1[:,1])
print(array1[1:3, 1:3])
print(array1[1:3,])
print(array1[:,1:3])
print(array1[1:3,1])
print(array1[1:3,:1])

