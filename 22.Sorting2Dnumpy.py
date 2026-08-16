import numpy as np

x = np.array([[12, 11, 15],
              [21, 25, 20],
              [18, 27, 16]])

# to sort coloumn wise -->0 and by default it is 1 for row wise even no need to write

y = np.sort(x,axis = 0)

x1 = np.array([[12, 11, 15],
               [21, 25, 20],
               [18,27, 16]])
y1 = np.argsort(x, axis = 0)
print(y1)
# this used to ge the indexes

# Sorting in 1D array
# sort --> it will return a sorted copy of any array
# np.argsort() --> it will return the indices that would sort an array
# ndarray.sort() --> use array name and sort it in place

x3 = np.array([7, 2, 4, 10, 1, 0])
y  = np.sort(x)
print(y)

# to reverse() sort(x)[::-1]
y = np.argsort(x)
#  will print the indices

# inplace
x.sort()
print(x)