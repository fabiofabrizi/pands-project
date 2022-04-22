# Exploratory Data Analysis (EDA) On the Iris Data set
# 
# The methods below are common to all the data visualisation articles I've come across
# Fabio Fabrizi

# Import pandas
import pandas as pd

# Read the csv file - note that in this project it's in the same folder
df = pd.read_csv("iris2.csv")

# Print the top 5 rows
print("\nBelow are the top 5 rows of the dataset.\nYou can also see the column headers\n")
print(df.head())

# Check for any missing values
print("\nBelow we're checking for any missing values in the dataset\n")
print(df.isnull().sum())

# Check for any duplicate data
print("\nBelow we're checking if any duplicate data exists\n")
data = df.drop_duplicates(subset="species",)
print(data)
print("\nWe can see that there's three unique species")

# Check if the dataset is balanced - ie. 
# Is there more of one particular species in this case?
print("\nIs the dataset balanced?\nie are there equal numbers of species\n")
print(df.value_counts("species"))

# Get the shape of the dataset
# The output of the below shows us rows and columns
print("\nWhat we want to see now are how many rows and columns\nthere are in the dataset\n")
print(df.shape)

# Get the info of the dataset
# This command tells us what type of data is inside the columns
print("\nWe also need to know the type of data inside\nthe dataset ie numerical, text, etc\n")
print(df.info())

# From running the above, we see that there's 4 columns of 
# numerical data and 1 column of categorical data (i.e. the type of species of Iris)
# sepal_length
# sepal_width
# petal_length
# petal_width
# class

# After all that, we now use the describe() method to perform general descriptive statistics:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
# This includes max/min/mean, standard deviation and percentiles. Missing values or NaN are skipped
print("\nFinally, we use the pandas method describe() to\nperform general descriptive statistics\n")
print(df.describe())

# NB:
# df.head() might not be necessary, but it's just a 
# quick way of seeing the columns/rows of the dataset