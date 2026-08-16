# Arithmetic Operations on Numpy Arrays
# 1.Addition
# 2.Subtraction
# 3.Multiplication
# 4.Matrix Multiplication
# 5.Division 
# 6.Floor Division 
# 7.Exponentiation
# 8.Modulo 
# 9.Transpose

import numpy as np

x = np.array([[1,2],
               [3,4]])
y = np.array([[11, 12],
             [13, 14]])
z = x + y
# similarly for subtraction operation
# multiplication is similar to addition and sub and not doing matrix multiplication
# ---------for matrix multiplication  use ---@---
# division and floor similar to additon and sub

print(z.transpose())
