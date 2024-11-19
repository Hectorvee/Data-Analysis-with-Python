import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Enable inline plotting
# %matplotlib inline

# Print the pandas version and the configuration
print(pd.__version__)

# DataFrame creation
# Create an empty pandas DataFrame
empty_df = pd.DataFrame(data=[None], index=[None], columns=[None])
print("Empty DataFrame:\n", empty_df, "\n")

# Create a marvel_df pandas DataFrame with the given marvel data
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

marvel_df = pd.DataFrame(data=marvel_data)
print("marvel_df DataFrame:\n", marvel_df, "\n")

# Add column names to the marvel_df
marvel_df.columns = ["character", "gender", "first_appearance"]
print("marvel_df DataFrame with column names:\n", marvel_df, "\n")

# Add index names to the marvel_df (use the character name as index)
marvel_df.index = marvel_df["character"]
print("marvel_df DataFrame with index names:\n", marvel_df, "\n")

# Drop the name column as it's now the index
marvel_df = marvel_df.drop(["character"], axis=1)
print("marvel_df DataFrame after dropping the character column:\n", marvel_df, "\n")

# Drop 'Namor' and 'Hank Pym' rows
marvel_df = marvel_df.drop(['Namor', 'Hank Pym'])
print("marvel_df DataFrame after dropping 'Namor' and 'Hank Pym' rows:\n", marvel_df, "\n")

# DataFrame selection, slicing and indexation
# Show the first 5 elements on marvel_df
print("First 5 elements on marvel_df:\n", marvel_df.iloc[:5], "\n")

# Show the last 5 elements on marvel_df
print("Last 5 elements on marvel_df:\n", marvel_df.iloc[-5:], "\n")

# Show just the sex of the first 5 elements on marvel_df
print("Sex of the first 5 elements on marvel_df:\n", marvel_df.iloc[:5, 1], "\n")

# Show the first_appearance of all middle elements on marvel_df
print("First appearance of all middle elements:\n", marvel_df.iloc[1:-1, 1], "\n")

# Show the first and last elements on marvel_df
print("The first and last elements:\n", marvel_df.iloc[[0, -1]], "\n")

# DataFrame manipulation and operations
# Modify the first_appearance of 'Vision' to year 1964
marvel_df.loc["Vision", "first_appearance"] = 1964
print("marvel_df DataFrame after modifying the first_appearance of 'Vision' to year 1964:\n", marvel_df, "\n")

# Add a new column to marvel_df called 'years_since' with the years since first_appearance
marvel_df["years_since"] = 2024 - marvel_df["first_appearance"]
print("marvel_df DataFrame after adding the 'years_since' column:\n", marvel_df, "\n")

# DataFrame boolean arrays (also called masks)
# Make a mask showing the female characters
print("Mask showing female characters: \n", marvel_df["gender"] == "female", "\n")

# Get the male characters
male_char = marvel_df[marvel_df["gender"] == "male"]
print("Male characters: \n", male_char, "\n")

# Get the characters with first_appearance after 1970
print("Characters with first_appearance after 1970: \n", marvel_df[marvel_df["first_appearance"] > 1970], "\n")

# Get the female characters with first_appearance after 1970
print("Female Characters with first_appearance after 1970: \n", marvel_df[(marvel_df["first_appearance"] > 1970) & (marvel_df["gender"] == "female")], "\n")

# DataFrame summary statistics
# Show basic statistics of marvel_df
print("Basic statistics of marvel_df: \n", marvel_df.describe(), "\n")

# Show the mean value of first_appearance
print("Mean value of first_appearance: \n", marvel_df["first_appearance"].mean(), "\n")

# Show the min value of first_appearance
print("Minimum value of first_appearance: \n", marvel_df["first_appearance"].min(), "\n")

# Get the characters with the min value of first_appearance
print("Characters with the min value of first_appearance: \n", marvel_df.iloc[marvel_df["first_appearance"].argmin()], "\n")

# DataFrame basic plotting
# Reset index names of marvel_df
print("Reset index names of marvel_df: \n", marvel_df.reset_index(), "\n")

# Plot the values of first_appearance
marvel_df["first_appearance"].plot()
plt.show()

# Plot a histogram with values of first_appearance
plt.hist(marvel_df["first_appearance"])
plt.show()
