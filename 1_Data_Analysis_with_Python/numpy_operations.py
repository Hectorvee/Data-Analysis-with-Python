import sys
import time
import numpy as np

# Broadcasting and Vectorized Operations
print("\n---------- Broadcasting and Vectorized Operations ----------")
f = np.array([1, 2, 3, 4, 5, 6])
print("Array f:", f)    # Print the array
print("Array f + 1:", f + 1)    # Add 1 to each element of the array
print("Array f - 1:", f - 1)    # Subtract 1 from each element of the array
print("Array f * 2:", f * 2)    # Multiply each element of the array by 2
print("Array f / 2:", f / 2)    # Divide each element of the array by 2
print("Array f ** 2:", f ** 2)    # Square each element of the array
print("Array f % 2:", f % 2)    # Modulus 2 of each element of the array
print("Array f // 2:", f // 2)    # Floor division by 2 of each element of the array
print("Array f + f:", f + f)    # Add each element of the array with corresponding element of the array
print("Array f - f:", f - f)    # Subtract each element of the array from corresponding element of the array
print("Array f * f:", f * f)    # Multiply each element of the array with corresponding element of the array
print("Array f / f:", f / f)    # Divide each element of the array by corresponding element of the array
print("Array f ** f:", f ** f)    # Power each element of the array by corresponding element of the array
print("Array f % f:", f % f)    # Modulus each element of the array by corresponding element of the array
print("Array f // f:", f // f)    # Floor division by each element of the array by corresponding element of the array

# List Comprehensions (Corresponding to Broadcasting and Vectorized Operations but List Comprehensions are slower)
print("\n---------- List Comprehensions ----------")
g = np.array([1, 2, 3, 4, 5, 6])
print("Array g:", g)    # Print the array
print("Array g + 1:", [i + 1 for i in g])    # Add 1 to each element of the array
print("Array g - 1:", [i - 1 for i in g])    # Subtract 1 from each element of the array
print("Array g * 2:", [i * 2 for i in g])    # Multiply each element of the array by 2
print("Array g / 2:", [i / 2 for i in g])    # Divide each element of the array by 2
print("Array g ** 2:", [i ** 2 for i in g])    # Square each element of the array
print("Array g % 2:", [i % 2 for i in g])    # Modulus 2 of each element of the array
print("Array g // 2:", [i // 2 for i in g])    # Floor division by 2 of each element of the array

# 2D Array Broadcasting and Vectorized Operations
print("\n---------- 2D Array Broadcasting and Vectorized Operations ----------")
h = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Array h:", h)    # Print the array
print("Array h + 1:", h + 1)    # Add 1 to each element of the array
print("Array h - 1:", h - 1)    # Subtract 1 from each element of the array
print("Array h * 2:", h * 2)    # Multiply each element of the array by 2
print("Array h / 2:", h / 2)    # Divide each element of the array by 2
print("Array h ** 2:", h ** 2)    # Square each element of the array
print("Array h % 2:", h % 2)    # Modulus 2 of each element of the array
print("Array h // 2:", h // 2)    # Floor division by 2 of each element of the array
print("Array h + h:", h + h)    # Add each element of the array with corresponding element of the array
print("Array h - h:", h - h)    # Subtract each element of the array from corresponding element of the array
print("Array h * h:", h * h)    # Multiply each element of the array with corresponding element of the array
print("Array h / h:", h / h)    # Divide each element of the array by corresponding element of the array
print("Array h ** h:", h ** h)    # Power each element of the array by corresponding element of the array
print("Array h % h:", h % h)    # Modulus each element of the array by corresponding element of the array
print("Array h // h:", h // h)    # Floor division by each element of the array by corresponding element

# Boolean Arrays
print("\n---------- Boolean Arrays ----------")
i = np.array([1, 2, 3, 4, 5, 6])
print("Array i:", i)    # Print the array
print("Array i > 3:", i > 3)    # Check if each element of the array is greater than 3
print("Array i < 3:", i < 3)    # Check if each element of the array is less than 3
print("Array i == 3:", i == 3)    # Check if each element of the array is equal to 3
print("Array i != 3:", i != 3)    # Check if each element of the array is not equal to 3
print("Array i >= 3:", i >= 3)    # Check if each element of the array is greater than or equal to 3
print("Array i <= 3:", i <= 3)    # Check if each element of the array is less than or equal to 3
print("Array i % 2 == 0:", i % 2 == 0)    # Check if each element of the array is even
print("Array i % 2 != 0:", i % 2 != 0)    # Check if each element of the array is odd
print("Array i[i % 2 == 0]:", i[i % 2 == 0])    # Get the elements of the array that are even
print("Array i[i % 2 != 0]:", i[i % 2 != 0])    # Get the elements of the array that are odd
print("Array np.arange(7):", np.arange(7))    # Print the array
print("Array np.arange(1, 7):", np.arange(1, 7))    # Print the array
j = np.arange(5)
print("Array j+20:", j+20)

# Linear Algebra
print("\n---------- Linear Algebra ----------")
k = np.array([
    [1, 2],
    [3, 4]
])
l = np.array([
    [5, 6],
    [7, 8]
])
print("Array k:", k)    # Print the array
print("Array l:", l)    # Print the array
print("Matrix multiplication of k and l:", k.dot(l))    # Matrix multiplication of k and l
print("Matrix multiplication of k and l:", np.dot(k, l))    # Matrix multiplication of k and l
print("Matrix multiplication of k and l:", k @ l)    # Matrix multiplication of k and l
print("Matrix transpose of k:", k.T)    # Matrix transpose of k
print("Matrix determinant of k:", np.linalg.det(k))    # Matrix determinant of k
print("Matrix inverse of k:", np.linalg.inv(k))    # Matrix inverse of k

# Size of objects in Memory
print("\n---------- Size of objects in Memory ----------")
m = np.array([1, 2, 3, 4, 5, 6])
print("Size of NumPy array m:", sys.getsizeof(m))    # Print the size of the NumPy array
print("Size of Python list m:", sys.getsizeof([1, 2, 3, 4, 5, 6]))    # Print the size of the Python list
n = np.array([1, 2, 3, 4, 5, 6], dtype='int8')
print("Size of NumPy array n:", sys.getsizeof(n))    # Print the size of the NumPy array
o = np.array([1, 2, 3, 4, 5, 6], dtype='int64')
print("Size of NumPy array o:", sys.getsizeof(o))    # Print the size of the NumPy array

# Speed Test
print("\n---------- Speed Test ----------")
size_of_vec = 1000000

X = list(range(size_of_vec))    # Create a list of numbers
Y = list(range(size_of_vec))    # Create a list of numbers

Z = np.arange(size_of_vec)      # Create a NumPy array of numbers
W = np.arange(size_of_vec)      # Create a NumPy array of numbers
start_time = time.time()

# Start the timer
for i in range(len(X)):         # Loop through the list
    X[i] = X[i] + Y[i]


print("Time taken for Python list:", (time.time() - start_time) * 1000, "ms")
start_time = time.time()
Z = Z + W
print("Time taken for NumPy array:", (time.time() - start_time) * 1000, "ms")

# Useful NumPy functions
print("\n---------- Useful NumPy functions ----------")
print("Array of zeros:", np.zeros(5))    # Create an array of zeros
print("Array of ones:", np.ones(5))    # Create an array of ones
print("Array of fives:", np.ones(5) * 5)    # Create an array of fives
print("Array of tens:", np.ones(5) * 10)    # Create an array of tens
print("Identity matrix:", np.eye(5))    # Create an identity matrix
print("Random numbers:", np.random.random(5))    # Create an array of random numbers
print("Random integers:", np.random.randint(5, 10, 5))    # Create an array of random integers between 5 and 10 (exclusive)
print("Array of 10 numbers between 1 and 5:", np.linspace(1, 5, 10))    # Create an array of 10 numbers between 1 and 5
print("Array of 10 numbers between 1 and 5:", np.arange(1, 5.1, 0.4))    # Create an array of 10 numbers between 1 and 5
print("Reshape array:", np.arange(1, 10).reshape(3, 3))    # Reshape an array
print("Flatten array:", np.arange(1, 10).reshape(3, 3).flatten())    # Flatten an array
print("Concatenate arrays:", np.concatenate([np.arange(1, 4), np.arange(4, 7)]))    # Concatenate arrays
print("Stack arrays vertically:", np.vstack([np.arange(1, 4), np.arange(4, 7)]))    # Stack arrays vertically
print("Stack arrays horizontally:", np.hstack([np.arange(1, 4), np.arange(4, 7)]))    # Stack arrays horizontally





