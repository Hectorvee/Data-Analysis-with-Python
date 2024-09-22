# Import the numpy package under the name np
import random

import numpy as np
from numpy.ma.core import arange

# Print the numpy version and the configuration
print(np.__version__)

# Array creation
print("\n---------- Array creation ----------")
# Create a numpy array of size 10, filled with zeros.

zeros_array = np.zeros(10)
print("Numpy array of size 10, filled with zeros")
print(zeros_array, "\n")

# Create a numpy array with values ranging from 10 to 49
arr1 = np.arange(10, 50)
print("Numpy array with values ranging from 10 to 49")
print(arr1, "\n")

# Create a numpy matrix of 2*2 integers, filled with ones.
arr2 = np.ones((2, 2), dtype=int)
print("Numpy matrix of 2*2 integers, filled with ones")
print(arr2, "\n")

# Create a numpy matrix of 3*2 float numbers, filled with ones.
arr3 = np.ones((3, 2), dtype=float)
print("Numpy matrix of 3*2 float numbers, filled with ones")
print(arr3, "\n")

# Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
X = np.arange(random.randint(1, 20))
arr4 = np.ones_like(X)
print("Numpy array with the same shape and type as X, filled with ones")
print(arr4, "\n")

# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.
X = np.array([[1, 2, 3], [4, 5, 6]])
arr5 = np.zeros_like(X)
print("Numpy array with the same shape and type as X, filled with zeros")
print(arr5, "\n")

# Create a numpy matrix of 4*4 integers, filled with fives.
arr6 = np.full((4, 4), 5)
# arr6 = np.ones((4, 4)) * 5
print("Numpy matrix of 4*4 integers, filled with fives")
print(arr6, "\n")

# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.
X = np.array([[1, 2], [3, 4]])
arr7 = np.full_like(X, 7)
print("Numpy matrix with the same shape and type as X, filled with sevens")
print(arr7, "\n")

# Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.
arr8 = np.identity(3)
print("3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere")
print(arr8, "\n")

# Create a numpy array, filled with 3 random integer values between 1 and 10.
arr9 = np.random.randint(1, 11, 3)
print("Numpy array filled with 3 random integer values between 1 and 10")
print(arr9, "\n")

# Create a 3*3*3 numpy matrix, filled with random float values.
arr10 = np.random.random((3, 3, 3))
print("3*3*3 numpy matrix, filled with random float values")
print(arr10, "\n")

# Given the X python list convert it to an Y numpy array.
X = [2, 1, 4, 6, 3]
arr12 = np.array(X)
print("Given the X python list convert it to an Y numpy array")
print(arr12, "\n")

# Given the X numpy array, make a copy and store it on Y.
X = np.array([2, 1, 4, 6, 3])
arr13 = np.copy(X)
print("Given the X numpy array, make a copy and store it on Y")
print(arr13, "\n")

# Create a numpy array with numbers from 1 to 10.
arr14 = np.arange(1, 11)
print("Numpy array with numbers from 1 to 10")
print(arr14, "\n")

# Create a numpy array with the odd numbers between 1 and 10.
arr15 = np.arange(1, 11, 2)
print("Numpy array with the odd numbers between 1 and 10")
print(arr15, "\n")

# Create a numpy array with numbers from 1 to 10, in descending order.
arr16 = np.arange(10, 0, -1)
print("Numpy array with numbers from 1 to 10, in descending order")
print(arr16, "\n")

# Create a 3*3 numpy matrix, filled with values ranging from 0 to 8.
arr17 = np.arange(9).reshape(3, 3)
print("3*3 numpy matrix, filled with values ranging from 0 to 8")
print(arr17, "\n")

# Show the memory size of the given Z numpy matrix.
Z = np.zeros((4, 4))
print("Memory size of the given Z numpy matrix")
print(Z.nbytes, "\n")

# Array indexation
print("\n---------- Array indexation ----------")
X_array = np.arange(10)
X_matrix = np.arange(9).reshape(3, 3)
# Given the X numpy array, show its first element.
print("Array: ", X_array)
print("First element: ", X_array[0], "\n")

# Given the X numpy array, show its last element.
print("Array: ", X_array)
print("Last element: ", X_array[-1], "\n")

# Given the X numpy array, show its first three elements.
print("Array: ", X_array)
print("First three elements: ", X_array[:3], "\n")

# Given the X numpy array, show all middle elements.
print("Array: ", X_array)
print("All middle elements: ", X_array[1:-1], "\n")

# Given the X numpy array, show the elements in reverse position.
print("Array: ", X_array)
print("Elements in reverse position: ", X_array[::-1], "\n")

# Given the X numpy array, show the elements in an odd position.
print("Array: ", X_array)
print("Elements in an odd position: ", X_array[::2], "\n")

# Given the X numpy matrix, show the first row elements.
print("Matrix: ", X_matrix)
print("First row elements: ", X_matrix[0, ], "\n")

# Given the X numpy matrix, show the last row elements.
print("Matrix: ", X_matrix)
print("Last row elements: ", X_matrix[-1, ], "\n")

# Given the X numpy matrix, show the first element on the first row.
print("Matrix: ", X_matrix)
print("First element on the first row: ", X_matrix[0, 0], "\n")

# Given the X numpy matrix, show the last element on the last row.
print("Matrix: ", X_matrix)
print("Last element on the last row: ", X_matrix[-1, -1], "\n")

# Given the X numpy matrix, show the middle row elements.
print("Matrix: ", X_matrix)
print("First element on the first row: ", X_matrix[1:-1, ], "\n")

# Given the X numpy matrix, show the first two elements on the first two rows.
print("Matrix: ", X_matrix)
print("First two elements on the first two rows: ", X_matrix[:2, :2], "\n")

# Given the X numpy matrix, show the last two elements on the last two rows.
print("Matrix: ", X_matrix)
print("Last two elements on the last two rows: ", X_matrix[-2:, -2:], "\n")

# Array manipulation
X_array = np.arange(10)
X_matrix = np.arange(9).reshape(3, 3)
print("\n---------- Array manipulation ----------")
# Convert the given integer numpy array to float.
X_array_float = X_array.astype(float)
print("Array: ", X_array)
print("Convert the given integer numpy array to float: ", X_array_float, "\n")

# Reverse the given numpy array (first element becomes last).
X_array_reverse = X_array[::-1]
print("Array: ", X_array)
print("Reverse the given numpy array (first element becomes last): ", X_array_reverse, "\n")

# Order (sort) the given numpy array.
X = np.array([4, 1, 10, 3, 2, 8, 5])
print("Array: ", X)
X.sort()
print("Order (sort) the given numpy array: ", X, "\n")

# Given the X numpy array, set the fifth element equal to 1.
X_array_new = np.copy(X_array)
X_array_new[5] = 1
print("Array: ", X_array)
print("Given the X numpy array, set the fifth element equal to 1: ", X_array_new, "\n")

# Given the X numpy array, change the 50 with a 40.

# Given the X numpy matrix, change the last row with all 1.

# Given the X numpy matrix, change the last item on the last row with a 0.

# Given the X numpy matrix, add 5 to every element.

# Boolean arrays (also called masks)
print("\n---------- Boolean arrays ----------")
# Given the X numpy array, make a mask showing negative elements.

# Given the X numpy array, get the negative elements.

# Given the X numpy array, get numbers higher than 5.

# Given the X numpy array, get numbers higher than the elements mean.

# Given the X numpy array, get numbers equal to 2 or 10.

# Logic functions
print("\n---------- Logic functions ----------")
# Given the X numpy array, return True if none of its elements is zero.

# Given the X numpy array, return True if any of its elements is zero.

# Summary statistics
print("\n---------- Summary statistics ----------")
# Given the X numpy array, show the sum of its elements.

# Given the X numpy array, show the mean of its elements.

# Given the X numpy array, show the max of its elements.

# Given the X numpy array, show the min of its elements.

# Given the X numpy array, show the index of the max of its elements.

# Given the X numpy array, show the index of the min of its elements.

# Given the 4X4 numpy array, show the array after subtracting the mean of each row.
