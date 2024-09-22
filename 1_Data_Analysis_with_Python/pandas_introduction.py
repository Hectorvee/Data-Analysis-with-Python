import pandas as pd
import numpy as np

# ---------- Basic Pandas Series ----------
print("---------- Basic Pandas Series ----------")
brics_pop = pd.Series([210.147, 143.5, 1252, 1357, 82.67])
print("BRICS Population:\n", brics_pop)    # Print the series
brics_pop.name = "BRICS Population"    # Set the name of the series

# Pandas values: Convert series to numpy array (ndarray) using values attribute
print("\nValues of BRICS Population:\n", brics_pop.values)    # Print the values of the series

# Pandas index: Index of the series is used to label the data points in the series (like dictionary keys)
brics_pop.index = ["Brazil", "Russia", "India", "China", "South Africa"]    # Change the index of the series
print("\nBRICS Population with country names as index:\n", brics_pop)    # Print the series

# Pandas index: Index can be set while creating the series
brics_pop = pd.Series([210.147, 143.5, 1252, 1357, 82.67], index=["Brazil", "Russia", "India", "China", "South Africa"])
print("\nBRICS Population with country names as index:\n", brics_pop)    # Print the series

# Pandas Indexing and Conditional Selection
print("\n---------- Pandas Indexing and Conditional Selection ----------")
print("Population of Brazil:", brics_pop["Brazil"])    # Print the population of Brazil
print("Population of Russia and India:\n", brics_pop[["Russia", "India"]])    # Print the population of Russia and India
print("Population greater than 1000:\n", brics_pop[brics_pop > 1000])    # Print the population greater than 1000

# Numeric position based indexing: iloc
print("\nPopulation of Brazil using iloc:", brics_pop.iloc[0])    # Print the population of Brazil using iloc
print("Population of Russia and India using iloc:\n", brics_pop.iloc[[1, 2]])    # Print the population of Russia and India using iloc

# Slice indexing
print("\nPopulation of Russia to China using slice:\n", brics_pop["Russia":"China"])    # Print the population of Russia to China using slice

# Conditional selection
print("\nPopulation greater than 1000 using conditional selection:\n", brics_pop[brics_pop > 1000])    # Print the population greater than 1000 using conditional selection

# Summary Statistics
print("\n---------- Summary Statistics ----------")
print("Sum of BRICS Population:", brics_pop.sum())    # Print the sum of the series
print("Mean of BRICS Population:", brics_pop.mean())    # Print the mean of the series
print("Standard deviation of BRICS Population:", brics_pop.std())    # Print the standard deviation of the series
print("Minimum value of BRICS Population:", brics_pop.min())    # Print the minimum value of the series
print("Maximum value of BRICS Population:", brics_pop.max())    # Print the maximum value of the series
print("Index of minimum value of BRICS Population:", brics_pop.argmin())    # Print the index of minimum value of the series
print("Index of maximum value of BRICS Population:", brics_pop.argmax())    # Print the index of maximum value of the

# Operations and Methods
print("\n---------- Operations and Methods ----------")
print("BRICS Population multiplied by 2:\n", brics_pop * 2)    # Multiply each element of the series by 2
print("BRICS Population divided by 2:\n", brics_pop / 2)    # Divide each element of the series by 2
# print("BRICS Population squared:\n", brics_pop ** 2)    # Square each element of the series
print("BRICS Population with log:\n", np.log(brics_pop))    # Take log of each element of the series
# print("BRICS Population with exp:\n", np.exp(brics_pop))    # Take exponential of each element of the series

# Modify the series
brics_pop["Brazil"] = 220    # Change the population of Brazil
print("\nBRICS Population after changing population of Brazil:\n", brics_pop)    # Print the series

# ---------- Basic Pandas DataFrame ----------







