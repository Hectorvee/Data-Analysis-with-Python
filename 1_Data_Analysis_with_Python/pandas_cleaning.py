import pandas as pd
import numpy as np

# Print the pandas version and the configuration
print("Pandas Version: ", pd.__version__)

# Detecting null values
print("\n---------- Detecting null values ----------")
# Create a pandas Series with the following data: [1, 2, np.nan, 4, np.nan]
X = pd.Series([1, 2, np.nan, 4, np.nan])
print("Series X:\n", X, "\n")
print("Detecting null values in the given X pandas Series:\n", X.isnull(), "\n")

# isnull() vs isna() methods(These two methods do exactly the same thing)
print("isnull() vs isna() methods:")
print("isnull() method:\n", X.isnull())
print("isna() method:\n", X.isna(), "\n")

# Detecting non-null values
print("Detecting non-null values in the given X pandas Series:\n", X.notnull(), "\n")

# Detecting null values in a DataFrame
# Create a pandas DataFrame with the following data:
# [[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]]
data = [[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]]
df = pd.DataFrame(data)
print("DataFrame df:\n", df, "\n")
print("Detecting null values in the given df pandas DataFrame:\n", df.isnull(), "\n")

# Counting null values
print("\n---------- Counting null values ----------")
# Count the number of null values in the given X pandas Series
print("Count the number of null values in the given X pandas Series:\n", X.isnull().sum(), "\n")

# Drop null values
print("\n---------- Drop null values ----------")
# Drop the null values in the given X pandas Series
print("Drop the null values in the given X pandas Series:\n", X.dropna(), "\n")

# Drop null values in a DataFrame
# Drop the null values in the given df pandas DataFrame
print("Drop the null values in the given df pandas DataFrame:\n", df.dropna(), "\n")


# Dropping null values in a DataFrame(advanced)
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', np.nan, 'Diana', 'Ethan', np.nan, 'George', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, np.nan, 30, 35, np.nan, 28, 40, 22, np.nan, 29],
    'Salary': [50000, 54000, 62000, np.nan, 59000, 60000, np.nan, 57000, 58000, np.nan],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'IT', np.nan, 'Finance', 'Finance', 'HR', np.nan],
    'Joining_Date': ['2020-01-15', '2019-08-09', np.nan, '2018-04-12', '2021-03-18', '2017-11-25', np.nan, '2022-02-15', '2020-12-30', '2019-05-14'],
    'Performance_Rating': [np.nan, 4.2, 3.8, 4.5, 4.0, 4.1, np.nan, 4.3, 3.9, 4.4],
    'Has_Bonus': [True, False, np.nan, True, False, True, np.nan, False, True, np.nan]
}
df = pd.DataFrame(data)
print("DataFrame df:\n", df, "\n")

# Check the details of the DataFrame
print("Information about the DataFrame:")
print(df.info(), "\n")
print("The size of data frame: ", df.size, "\n")
print("Shape of data frame:\n", df.shape, "\n")

# Check the number of null values in the DataFrame
print("Number of null values in the DataFrame:")
print(df.isnull().sum(), "\n")

# Drop the rows with any null values
print("Drop the rows with any null values in the DataFrame:")
print(df.dropna(), "\n")    # This will drop the rows with any null values

# Drop the columns with any null values
print("Drop the columns with any null values in the DataFrame:")
print(df.dropna(axis=1), "\n")    # This will drop the columns with any null values

# Drop the rows with all null values
print("Drop the rows with all null values in the DataFrame:")
print(df.dropna(how='all'), "\n")    # This will drop the rows with all null values

# Drop the columns with all null values
print("Drop the columns with all null values in the DataFrame:")
print(df.dropna(axis=1, how='all'), "\n")    # This will drop the columns with

# Drop the rows with null values in a specific column
print("Drop the rows with null values in the Department column in the DataFrame:")
print(df.dropna(subset=['Department']), "\n")    # This will drop the rows with null values in the Department column

# Drop the rows with threshold
print("Drop the rows with at least 5 non-null values in the DataFrame:")
print(df.dropna(thresh=5), "\n")    # This will drop the rows with at least 5 non-null values


# Fill null values
print("\n---------- Fill null values ----------")

# Display the DataFrame
print("DataFrame df:\n", df, "\n")

# Fill null values with a arbitrary value
print("Fill null values with 0 in the DataFrame:")
print(df.fillna(0), "\n")    # This will fill the null values with 0

# Fill null values with the mean of the numeric column
print("Fill null values with the mean of the numeric column in the DataFrame:")
print(df.fillna(df[["Age", "Salary", "Performance_Rating"]].mean()), "\n")    # This will fill the null values with the mean of the numeric column

# Fill null values with backward fill and forward fill
print("Fill null values with backward fill in the DataFrame:")
# print(df.fillna(method='bfill'), "\n")    # This will fill the null values with backward fill (This will fill the null values with the next value)
print("Fill null values with forward fill in the DataFrame:")
# print(df.fillna(method='ffill'), "\n")    # This will fill the null values with forward fill (This will fill the null values with the previous value)


# Cleaning not null values
print("\n---------- Cleaning not null values ----------")
# First create dataframe of sex and age
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 450, -5, 35, 120, 80, 15, 40, 999, 29],  # Invalid ages: 450, -5, 999, 120
    'Sex': ['F', 'M', 'X', 'F', 'M', 'F', 'Male', 'M', 'Unknown', 'Female']  # Invalid: 'X', 'Unknown', 'Male', 'Female'
}

df = pd.DataFrame(data)
print("DataFrame df:\n", df, "\n")

# Finding unique values
# The fist step to clean invalid values is to notice them, then identify them then finally clean them.
print("Unique values in the Sex column:")
print(df["Sex"].unique(), "\n")    # This will print the unique values in the Age column
print(df["Sex"].value_counts(), "\n")   # This will print the count of unique values in the Age column

# Replace invalid values
# Replace the invalid values in the sex column
print("Replace 'X' with 'M', 'Male' with 'M', 'Female' with 'F', 'Unknown' with 'M': ")
print(df["Sex"].replace({"X": "M", 'Male': 'M', 'Female': 'F', 'Unknown': 'M'}))

# Cleaning the Age column
# Cleaning the Age column by removing the invalid values
print("Clean the Age column by removing the invalid values:")
valid_ages = df['Age'][(df['Age'] > 0) & (df['Age'] < 100)]
average_age = valid_ages.mean()

# Replace the invalid ages with the average age
df['Age'] = df['Age'].apply(lambda x: average_age if x <= 0 or x >= 100 else x)
print("DataFrame df after cleaning the Age column:\n", df, "\n")

# Duplicate values
print("\n---------- Duplicate values ----------")
# Create a pandas series with the following data:
ambassadors = pd.Series(
    ['France', 'UK', 'UK', 'Italy', 'Germany', 'Germany', 'Germany'],
    index=['Gérard Araud', 'Kim Darroch', 'Kim Darroch', 'Armando Varricchio', 'Peter Wittig', 'Peter Wittig', 'Peter Wittig']
)

print("Series ambassadors:\n", ambassadors, "\n")

# Detect duplicate values
print("Detect duplicate values in the given ambassadors pandas Series:\n", ambassadors.duplicated(), "\n")  # This will detect the duplicate values
print("Detect duplicate values in the given ambassadors pandas Series:\n", ambassadors.duplicated(keep='last'), "\n")   # This will detect the duplicate values and keep the last one
print("Detect duplicate values in the given ambassadors pandas Series:\n", ambassadors.duplicated(keep=False), "\n")    # This will detect the duplicate values and mark all of them as duplicate

# Drop duplicate values
print("Drop duplicate values in the given ambassadors pandas Series:\n", ambassadors.drop_duplicates(), "\n")    # This will drop the duplicate values
print("Drop duplicate values in the given ambassadors pandas Series:\n", ambassadors.drop_duplicates(keep='last'), "\n")    # This will drop the duplicate values and keep the last one
print("Drop duplicate values in the given ambassadors pandas Series:\n", ambassadors.drop_duplicates(keep=False), "\n")    # This will drop the duplicate values and mark all of them as duplicate















































