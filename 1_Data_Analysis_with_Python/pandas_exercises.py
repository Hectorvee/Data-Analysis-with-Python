import numpy as np
import pandas as pd

# Print the pandas version and the configuration
print("Pandas Version: ", pd.__version__)

# ---------- Series creation ----------
print("\n---------- Series creation ----------")
# Create an empty pandas Series
print("Create an empty pandas Series: ", pd.Series(), "\n")

# Given the X python list convert it to an Y pandas Series
X = ['A','B','C']
series = pd.Series(X)
print("List X: ", X)
print("Given the X python list convert it to an Y pandas Series: ", pd.Series(), "\n")

# Given the X pandas Series, name it 'My letters'
X = pd.Series(['A','B','C'])
print("Series X:\n", X)
X.name = "My letters"
print("Given the X pandas Series, name it 'My letters':\n", X, "\n")

# Given the X pandas Series, show its values
X = pd.Series(['A','B','C'])
print("Series X:\n", X)
print("Given the X pandas Series, show its values:\n", X.values, "\n")

# ---------- Series indexation ----------
print("\n---------- Series indexation ----------")
# Assign index names to the given X pandas Series
X = pd.Series(['A','B','C'])
print("Series X:\n", X)
index_names = ['first', 'second', 'third']
X.index = index_names
print("Assign index names to the given X pandas Series:\n", X, "\n")

# Given the X pandas Series, show its first element
X = pd.Series(['A','B','C'], index=['first', 'second', 'third'])
print("Series X:\n", X)
print("Given the X pandas Series, show its first element:\n", X["first"], "\n")

# Given the X pandas Series, show its last element
X = pd.Series(['A','B','C'], index=['first', 'second', 'third'])
print("Series X:\n", X)
print("Given the X pandas Series, show its last element:\n", X.iloc[-1], "\n")

# Given the X pandas Series, show all middle elements
X = pd.Series(['A','B','C','D','E'], index=['first','second','third','forth','fifth'])
print("Series X:\n", X)
print("Given the X pandas Series, show all middle elements:\n", X.iloc[1:-1], "\n")

# Given the X pandas Series, show the elements in reverse position
X = pd.Series(['A','B','C','D','E'], index=['first','second','third','forth','fifth'])
print("Series X:\n", X)
print("Given the X pandas Series, show the elements in reverse position:\n", X.iloc[::-1], "\n")

# Given the X pandas Series, show the first and last elements
X = pd.Series(['A','B','C','D','E'], index=['first','second','third','forth','fifth'])
print("Series X:\n", X)
print("Given the X pandas Series, show the first and last elements:\n", X.iloc[[0, -1]], "\n")

# ---------- Series manipulation ----------
print("\n---------- Series manipulation ----------")
# Convert the given integer pandas Series to float
X = pd.Series([1,2,3,4,5], index=['first','second','third','forth','fifth'])
print("Series X:\n", X)
print("Convert the given integer pandas Series to float:\n", pd.Series(X, dtype=float), "\n")

# Reverse the given pandas Series (first element becomes last)
X = pd.Series([1,2,3,4,5], index=['first','second','third','forth','fifth'])
print("Series X:\n", X)
print("Reverse the given pandas Series (first element becomes last):\n", X[::-1], "\n")

# Order (sort) the given pandas Series
X = pd.Series([4,2,5,1,3], index=['forth','second','fifth','first','third'])
print("Series X:\n", X)
print("Order (sort) the given pandas Series:\n", X.sort_values(), "\n")

# Given the X pandas Series, set the fifth element equal to 10
X = pd.Series([1,2,3,4,5], index=['A','B','C','D','E'])
print("Series X:\n", X)
X.iloc[4] = 10
print("Given the X pandas Series, set the fifth element equal to 10:\n", X, "\n")

# Given the X pandas Series, change all the middle elements to 0
X = pd.Series([1,2,3,4,5], index=['A','B','C','D','E'])
print("Series X:\n", X)
X.iloc[1:-1] = 0
print("Given the X pandas Series, change all the middle elements to 0:\n", X, "\n")

# Given the X pandas Series, add 5 to every element
X = pd.Series([1,2,3,4,5])
print("Series X:\n", X)
X += 5
print("Given the X pandas Series, add 5 to every element:\n", X, "\n")

# ---------- Series boolean arrays (also called masks) ----------
print("\n---------- Series boolean arrays (also called masks) ----------")
# Given the X pandas Series, make a mask showing negative elements
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, make a mask showing negative elements:\n", X<0, "\n")

# Given the X pandas Series, get the negative elements
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, get the negative elements:\n", X[X<0], "\n")

# Given the X pandas Series, get numbers higher than 5
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, get numbers higher than 5:\n", X[X>5], "\n")

# Given the X pandas Series, get numbers higher than the elements mean
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, get numbers higher than the elements mean:\n", X[X>X.mean()], "\n")

# Given the X pandas Series, get numbers equal to 2 or 10
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, get numbers equal to 2 or 10:\n", X[(X==2) | (X==10)], "\n")

# ---------- Logic functions ----------
print("\n---------- Logic functions ----------")
# Given the X pandas Series, return True if none of its elements is zero
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, return True if none of its elements is zero:\n", all(X), "\n")

# Given the X pandas Series, return True if any of its elements is zero
X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print("Series X:\n", X)
print("Given the X pandas Series, return True if any of its elements is zero:\n", any(X), "\n")

# ---------- Summary statistics ----------
print("\n---------- Summary statistics ----------")
# Given the X pandas Series, show the sum of its elements
X = pd.Series([3,5,6,7,2,3,4,9,4])
print("Series X:\n", X)
print("Given the X pandas Series, show the sum of its elements:\n", X.sum(), "\n")

# Given the X pandas Series, show the mean value of its elements
X = pd.Series([1,2,0,4,5,6,0,0,9,10])
print("Series X:\n", X)
print("Given the X pandas Series, show the mean value of its elements:\n", X.mean(), "\n")

# Given the X pandas Series, show the max value of its elements
X = pd.Series([1,2,0,4,5,6,0,0,9,10])
print("Series X:\n", X)
print("Given the X pandas Series, show the max value of its elements:\n", X.max(), "\n")
