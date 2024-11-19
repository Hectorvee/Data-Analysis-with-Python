import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Print the pandas version and the configuration
print("Pandas Version: ", pd.__version__)

# ---------- Reading CSV Files ----------
print("\n---------- Reading CSV Files ----------")
df = pd.read_csv("data/btc-market-price.csv", header=None)
print("Dataframe df:\n", df, "\n")

df.columns = ["Timestamp", "Price"]
print("Dataframe df:\n", df, "\n")

print("Dataframe df head:\n", df.head(), "\n")    # Print the first 5 rows of the dataframe
print("Dataframe df tail:\n", df.tail(), "\n")    # Print the last 5 rows of the dataframe
print("Dataframe df shape:\n", df.shape, "\n")    # Print the shape of the dataframe
print("Dataframe df describe:\n", df.describe(), "\n")    # Print the summary statistics of the dataframe
print("Dataframe df info:\n", df.info(), "\n")    # Print the concise summary of the dataframe
print("Dataframe df dtypes:\n", df.dtypes, "\n")    # Print the data types of the dataframe

# Change the data type of the Timestamp column to datetime(This is a common practice when working with time series data)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
print("Dataframe df dtypes after changing the data type of the Timestamp column to datetime:\n", df.dtypes, "\n")    # Print the data types of the dataframe

# Set the Timestamp column as the index of the dataframe
df.set_index("Timestamp", inplace=True)   # inplace=True will modify the dataframe directly without creating a new dataframe
print("Dataframe df head after setting the Timestamp column as the index of the dataframe:\n", df.head(), "\n")    # Print the first 5 rows of

# Access the price of Bitcoin on January 1st, 2018
print("Price of Bitcoin on January 1st, 2018:\n", df.loc["2018-01-01"], "\n")    # Print the price of Bitcoin on January 1st, 2018

# Putting it all together
df = pd.read_csv(
    "data/btc-market-price.csv",    # File to read
    header=None,    # Skip the header
    names=["Timestamp", "Price"],   # Name the columns
    index_col=0,    # Set the index to the Timestamp column
    parse_dates=True    # Parse the dates in the Timestamp column
)
print("Dataframe df head after putting it all together:\n", df.head(), "\n")    # Print the first 5 rows of the dataframe

# ---------- Plotting the Data ----------
print("\n---------- Plotting the Data ----------")
# df.plot()   # Plot the dataframe
# plt.show()    # Display the plot
plt.plot(
    df.index, df["Price"]) # Plot the price of Bitcoin over time
plt.show()    # Display the plot





