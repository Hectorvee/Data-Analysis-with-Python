import numpy as np

# Basic Numpy Arrays
print("---------- Basic Numpy Arrays ----------")
a = np.array([1, 2, 3, 4, 5, 6])
print("Array a:", a)    # Print the array
print("Shape of array a:", a.shape)  # Print the shape of the array e.g. (3,) means 3 elements in 1D array
print("First three elements of array a:", a[0], a[1], a[2])    # Print the elements of the array
a[0] = 5    # Change an element of the array
print("Array a after changing first element to 5:", a)    # Print the array
print("Array a from index 0 to end:", a[0:])    # Print the array from index 0 to end
print("Array a from index 1 to 3:", a[1:3])    # Print the array from index 1 to 3
print("Array a from index 1 to second last:", a[1:-1])    # Print the array from index 1 to second last
print("Array a with step 2:", a[::2])    # Print the array with step 2
print("Array a with specific indexes 0, 2, 4:", a[[0, 2, 4]])    # Print the array with specific indexes

# Array Types
print("\n---------- Array Types ----------")
b = np.array([1, 2, 3, 4, 5, 6])
c = np.array([1, 2.3, 3.4, 4.1, 5, 6])
print("Data type of array b:", b.dtype)  # Print the data type of the array
print("Data type of array c:", c.dtype)  # Print the data type of the array
np.array([1, 2, 3, 4, 5, 6], dtype='float32')    # Create an array with specific data type

# Dimensions and Shapes
print("\n---------- Dimensions and Shapes ----------")
d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Array d:", d)    # Print the array
print("Shape of array d:", d.shape)  # Print the shape of the array e.g. (3, 3) means 3x3 matrix
print("Diagonal elements of array d:", d[0, 0], d[1, 1], d[2, 2])    # Print the elements of the array
d[0, 0] = 5    # Change an element of the array
print("Array d after changing first element to 5:", d)    # Print the array
print("Array d from index 0 to end:", d[0:])    # Print the array from index 0 to end
print("Array d from index 1 to 3:", d[1:3])    # Print the array from index 1 to 3
print("Array d from index 1 to second last:", d[1:-1])    # Print the array from index 1 to second last
print("Array d with step 2:", d[::2])    # Print the array with step 2
print("Array d with specific indexes 0, 2, 4:", d[[0, 2]])    # Print the array with specific indexes
print("Array d with specific indexes 0, 2, 4:", d[[0, 2], [0, 2]])    # Print the array with specific indexes
d[1] = np.array([10, 11, 12])    # Change a row of the array
print("Array d after changing second row:", d)    # Print the array
d[:, 2] = np.array([30, 31, 32])    # Change a column of the array

# Summary Statistics
print("\n---------- Summary Statistics ----------")
e = np.array([1, 2, 3, 4, 5, 6])
print("Array e:", e)    # Print the array
print("Sum of array e:", e.sum())    # Print the sum of the array
print("Mean of array e:", e.mean())    # Print the mean of the array
print("Standard deviation of array e:", e.std())    # Print the standard deviation of the array
print("Minimum value of array e:", e.min())    # Print the minimum value of the array
print("Maximum value of array e:", e.max())    # Print the maximum value of the array
print("Index of minimum value of array e:", e.argmin())    # Print the index of minimum value of the array
print("Index of maximum value of array e:", e.argmax())    # Print the index of maximum value of the array

# Summary statistics for 2D array
print("\n---------- Summary Statistics for 2D array ----------")
f = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Array f:", f)    # Print the array
print("Sum of array f:", f.sum())    # Print the sum of the array
print("Sum of array f along axis 0:", f.sum(axis=0))    # Print the sum of the array along axis 0 (column-wise)
print("Sum of array f along axis 1:", f.sum(axis=1))    # Print the sum of the array along axis 1 (row-wise)
print("Mean of array f:", f.mean())    # Print the mean of the array
print("Mean of array f along axis 0:", f.mean(axis=0))    # Print the mean of the array along axis 0
print("Mean of array f along axis 1:", f.mean(axis=1))    # Print the mean of the array along axis 1
print("Standard deviation of array f:", f.std())    # Print the standard deviation of the array
print("Standard deviation of array f along axis 0:", f.std(axis=0))    # Print the standard deviation of the array along axis 0
print("Standard deviation of array f along axis 1:", f.std(axis=1))    # Print the standard deviation of the array along axis 1




