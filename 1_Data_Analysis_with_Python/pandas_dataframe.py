import pandas as pd
import numpy as np

# ---------- Basic Pandas DataFrame ----------
print("\n---------- Basic Pandas DataFrame ----------")
# Create a pandas DataFrame of brics countries with their population, GDP, Surface Area, HDI, and Continent
brics_df = pd.DataFrame({
    'Population': [210_147_125, 143_500_000, 1_252_000_000, 1_357_000_000, 82_673_000],
    'GDP': [2_147_000_000_000, 1_860_000_000_000, 2_875_000_000_000, 14_340_000_000_000, 350_000_000_000],
    'Surface Area': [8_515_767, 17_098_242, 3_287_590, 9_596_961, 1_221_037],
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

# Conditional Selection (Boolean Arrays)
print("Population greater than 1000000000:\n", brics_df[brics_df["Population"] > 1000000000], "\n")    # Print the population greater than 1000000000
print("Population greater than 1000000000 and HDI greater than 0.7:\n", brics_df[(brics_df["Population"] > 1000000000) & (brics_df["HDI"] > 0.7)], "\n")    # Print the population greater than 1000000000 and HDI greater than 0.7

# Dropping rows and columns
print("---------- Dropping rows and columns ----------")
# Drop the row of South Africa
brics_df_drop_row = brics_df.drop("South Africa")
print("BRICS Countries DataFrame after dropping South Africa row:\n", brics_df_drop_row, "\n")    # Print the DataFrame after dropping South Africa row

# Drop the column of Continent
brics_df_drop_column = brics_df.drop("Continent", axis=1)
print("BRICS Countries DataFrame after dropping Continent column:\n", brics_df_drop_column, "\n")    # Print the DataFrame after dropping Continent column

# Operations with series work at the column level
print("---------- Operations with series work at the column level ----------")
crisis = pd.Series([-1_000_000, -0.3], index=["GDP", "HDI"])    # Create a series of crisis
brics_df_crisis = brics_df[["GDP", "HDI"]] + crisis    # Add the series to the DataFrame
print("BRICS Countries DataFrame after adding crisis series:\n", brics_df_crisis, "\n")    # Print the DataFrame after adding crisis series

# Modify the DataFrames
print("---------- Modify the DataFrames ----------")
# Addition of new column
langs = pd.Series(["Portuguese", "Russian", "Hindi", "Mandarin", "English"], index=["Brazil", "Russia", "India", "China", "South Africa"])    # Create a series of languages
brics_df["Language"] = langs    # Add the series to the DataFrame
print("BRICS Countries DataFrame after adding Language column:\n", brics_df, "\n")    # Print the DataFrame after adding Language column

# Replacing values per column
brics_df["Language"] = "English"    # Replace the values of the column with English
print("BRICS Countries DataFrame after replacing Language column with English:\n", brics_df, "\n")    # Print the DataFrame after replacing Language column

# Rename the columns
brics_df = brics_df.rename(
    columns={
        "Language": "Official Language"
    }, index={
        "Brazil": "BR",
        "Russia": "RU",
        "India": "IN",
        "China": "CN",
        "South Africa": "SA"
    }
)    # Rename the columns and index of the DataFrame using rename method with columns and index parameters
print("BRICS Countries DataFrame after renaming columns and index:\n", brics_df, "\n")    # Print the DataFrame after renaming columns and index

# Creating Columns from other columns
brics_df["GDP per capita"] = brics_df["GDP"] / brics_df["Population"]    # Create a new column GDP per capita
print("BRICS Countries DataFrame after adding GDP per capita column:\n", brics_df, "\n")    # Print the DataFrame after adding GDP per capita column






