import numpy as np

# Define matrix A
A = np.array([[2, -1],
              [1, 3]])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(A)

print("Eigenvalues of matrix A:")
print(eigenvalues)