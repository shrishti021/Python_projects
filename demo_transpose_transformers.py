# 🤖 Transpose in Attention Mechanism (Transformers)
# Inside GPT, BERT, and Claude, the attention mechanism does:

# Attention = softmax(Q × Kᵀ / √d) × V

# Where Q = Query matrix, K = Key matrix, V = Value matrix.
# The Kᵀ (K-transpose) is used to compute similarity scores between every word and every other word simultaneously.

# This matrix operation on millions of tokens is what makes modern AI understand context. No transpose → no attention → no ChatGPT!

import numpy as np

A = np.array([[1,2,3],
              [4,5,6]])

print("original shape: ", A.shape)  #(2,3)

#Transpose
At = A.T 
print("Transposed matrix shape: ", At.shape)   #(3,2)
print("Transposed: \n",At)

#Identity matrix
I = np.eye(3)  #3x3 identity
print("Identity: \n", I)

#Any matrix x identity = same matrix
B = np.array([[2,4],
              [5,6]])
I2 = np.eye(2)
print("B x I= \n", B @ I2)

################################################################################

#Problem 3: If A has shape (100, 784) and W
# has shape (784, 128), what is the shape
# of A @ W ? (This is a real neural net layer!)
inputs = np.random.rand(100, 784)   # 100 images
weights = np.random.rand(784, 128)  # weight matrix
output = inputs @ weights
print("P3 output shape:", output.shape)   # (100, 128)