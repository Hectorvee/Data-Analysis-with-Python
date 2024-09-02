import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date']) # parse_dates=['Date'] is used to convert the 'Date' column to datetime format

# The data at a glance
print("---------- Data Head ----------")
print(sales.head()) # Display the first 5 rows of the data

print("---------- Data Shape ----------")
print(sales.shape) # Display the number of rows and columns in the data

print("---------- Data Information ----------")
print(sales.info()) # Display the data types of each column and the number of non-null values

print("---------- Data Description ----------")
print(sales.describe()) # Display summary statistics for numerical columns

# Numerical analysis and visualization
print(sales['Unit_Cost'].describe()) # Display summary statistics for the 'Unit_Cost' column
print(sales['Unit_Cost'].mean()) # Calculate the mean of the 'Unit_Cost' column
print(sales['Unit_Cost'].median()) # Calculate the median of the 'Unit_Cost' column



