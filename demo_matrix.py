# 🤖 A Dataset IS a Matrix
# In machine learning, your entire training dataset is one big matrix.

# Rows = data points (people, images, emails...)
# Cols = features (age, height, income, color...)

# Example — 1000 users, 5 features:
# Matrix shape: (1000, 5)

# [ 25, 50000, 8.5, 1, 0 ]  ← User 1
# [ 32, 75000, 7.2, 0, 1 ]  ← User 2
# [ 28, 62000, 9.1, 1, 1 ]  ← User 3
# ...

# Every time sklearn fits a model on your data, it's doing matrix math!

import numpy as np

#create a 2D array
A = np.array([[1,2],
              [3,4],
              [5,6]])

print("shape: ", A.shape)
print("Rows: ", A.shape[0])
print("columns: ", A.shape[1])

#Access individual elements 
print(A[0,0])
print(A[1,1])
print(A[2,0])

#get entrire row or columns
print(A[0, :])  #[1,2]
print(A[:, 1])  #[2,4,6]

#######################################################################

#Matrix multiplication

P = np.array([[1,2],
              [3,4]])

Q = np.array([[5,6],
              [7,8]])

#Matrix multiplication - use @ operator
R = P @ Q
print("P x Q = ", R)

#or use np.matmul
R2 = np.matmul(P,Q)
print(R2)

#Shape rule check: (2x2) x (2x2) -> (2x2) ✓
print("shape: ", R.shape)    #(2,2)

# WRONG: (2×3) × (2×3) won't work!
# Inner dimensions must match: (2×3) × (3×2) ✓
X = np.array([[1,2,3],[4,5,6]])  #shape (2,3)
Y = np.array([[1,2],[3,4],[5,6]])  #shape(3,2)
print("Results shape: ", (X @ Y).shape) 