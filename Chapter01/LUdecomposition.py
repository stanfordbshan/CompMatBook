import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Define matrix A and vector b
A = np.array([[1, 6, 0, 3], 
              [0, 2, 0, 4],
              [-1, -6, 3, -3], 
              [0, -2, 0, 8]])
b = np.array([[5],[4],[5],[4]])

# Perform LU decomposition and factorization of A
lu, piv = lu_factor(A)

# Solve Ax = b using LU decomposition
x = lu_solve((lu, piv), b)

print("Matrix A:")
print(A)

print("\nVector b:")
print(b)

print("\nSolution vector x:")
print(x)