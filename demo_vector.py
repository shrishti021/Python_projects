import numpy as np

#create a vector
v = np.array([3,4])
print("vector: ", v)

# Vector length (magnitude)
length = np.linalg.norm(v)
print("length: ", length)   # Length: 5.0

# Why 5? → √(3² + 4²) = √(9+16) = √25 = 5
# Classic 3-4-5 triangle!

user_features = np.array([25,50000,8.5])
print("user_vector:" ,user_features)

########################################################################

a = np.array([1,2])
b = np.array([3,1])

#combine 2 vectors
result = a + b 
print(result)

#subtract 2 vectors
subt = a-b
print(subt)

#Scaling — multiply all values
scale = 2 * a
print(scale)

# # Normalize — make length = 1 (very common in AI!)
# Step-by-step:
# Length of a:
# √(1² + 2²) = √5 ≈ 2.236
# Divide each element:
# [1/2.236, 2/2.236] ≈ [0.447, 0.894]

normalize =a / np.linalg.norm(a)
print("normalized: ", normalize)    # [0.447, 0.894]
print("length now: ", np.linalg.norm(normalize))   # 1.0


##########################################################################################

p = np.array([1, 2, 3])
q = np.array([4, 5, 6])
r = np.array([-1, -2, -3])  # opposite of a

# Dot product
print("a · b =", np.dot(p, q))  # 32 (similar direction)
print("a · c =", np.dot(p, r))  # -14 (opposite!)

# Cosine similarity — normalized dot product
# Used in search engines and recommendation AI
def cosine_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

# Range: -1 (opposite) to 0 (unrelated) to 1 (identical)
print("sim(p, q):", cosine_similarity(p, q))  # 0.974 (very similar!)
print("sim(p, r):", cosine_similarity(p, r))  # -1.0 (exact opposites)
