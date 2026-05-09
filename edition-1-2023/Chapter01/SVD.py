import numpy as np

# Define matrix A
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Perform SVD
U, S, Vt = np.linalg.svd(A)

# Create the Sigma matrix with the same shape as A
Sigma = np.zeros(A.shape)
for i in range(min(A.shape)):
    Sigma[i, i] = S[i]

print("Matrix A:")
print(A)

print("\nMatrix U:")
print(U)

print("\nMatrix Sigma:")
print(Sigma)

print("\nMatrix Vt:")
print(Vt)