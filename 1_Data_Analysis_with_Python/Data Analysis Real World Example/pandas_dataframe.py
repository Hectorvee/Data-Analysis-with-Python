import pandas as pd
import numpy as np

# ---------- Basic Pandas DataFrame ----------
print("\n---------- Basic Pandas DataFrame ----------")
# Create a pandas DataFrame of brics countries with their population, GDP, Surface Area, HDI, and Continent
brics_df = pd.DataFrame({
    'Population': [210147125, 143500000, 1252000000, 1357000000, 82673000],
    'GDP': [2147000000000, 1860000000000, 2875000000000, 14340000000000, 350000000000],
    'Surface Area': [8515767, 17098242, 3287590, 9596961, 1221037],
    'HDI': [0.758, 0.824, 0.645, 0.738, 0.705],
    'Continent': ['South America', 'Europe', 'Asia', 'Asia', 'Africa']
}, index=['Brazil', 'Russia', 'India', 'China', 'South Africa']
)
print("BRICS Countries DataFrame:\n", brics_df, "\n")    # Print the DataFrame

# Information about the DataFrame
brics_df.info()    # Print information about the DataFrame
print("\nThe size of data frame: ", brics_df.size, "\n")   # Print the size of the DataFrame (number of elements)
print("Shape of data frame:\n", brics_df.shape, "\n")   # Print the shape of the DataFrame (number of rows and columns)
print("Number of dimensions of data frame:\n", brics_df.ndim, "\n")   # Print the number of dimensions of the DataFrame
print("Columns of data frame:\n", brics_df.columns, "\n")   # Print the columns of the DataFrame
print("Index of data frame:\n", brics_df.index, "\n")   # Print the index of the DataFrame
print("Values of data frame:\n", brics_df.values, "\n")   # Print the values of the DataFrame
print("Data types of data frame:\n", brics_df.dtypes, "\n")   # Print the data types of the DataFrame
print("Memory usage of data frame:\n", brics_df.memory_usage(), "\n")   # Print the memory usage of the DataFrame
print("Statistical summary of data frame:\n", brics_df.describe(), "\n")   # Print the statistical summary of the DataFrame

# Indexing, Selection, and Slicing
print("---------- Indexing, Selection, and Slicing ----------")
# loc: Will access the row by the index name
print("Row of South Africa using loc:\n", brics_df.loc["South Africa"], "\n")  # Print the row of South Africa using loc
print("Population of Brazil using loc:\n", brics_df.loc["Brazil", "Population"], "\n")    # Print the population of Brazil using loc
print("Population of Russia and India using loc:\n", brics_df.loc[["Russia", "India"], "Population"], "\n")    # Print the population of Russia and India using loc

# iloc: Will access the row by the index position
print("\nRow of South Africa using iloc:\n", brics_df.iloc[4], "\n")  # Print the row of South Africa using iloc
print("Population of Brazil using iloc:\n", brics_df.iloc[0, 0], "\n")    # Print the population of Brazil using iloc
print("Population of Russia and India using iloc:\n", brics_df.iloc[[1, 2], 0], "\n")    # Print the population of Russia and India

# Column selection
print("\nPopulation of BRICS Countries:\n", brics_df["Population"], "\n")    # Print the population of BRICS Countries
print("Population and GDP of BRICS Countries:\n", brics_df[["Population", "GDP"]], "\n")    # Print the population and GDP

# Slicing
print("Population of Russia to China using slicing:\n", brics_df["Population"]["Russia":"China"], "\n")    # Print the population of Russia to China using slicing
print("Population of Russia to China using loc:\n", brics_df.loc["Russia":"China", "Population"], "\n")    # Print the population of Russia to China using loc
print("Population of Russia to China using iloc:\n", brics_df.iloc[1:4, 0], "\n")    # Print the population of Russia to China using iloc


