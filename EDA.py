# Exploratory Data Analysis (EDA) On the Iris Data set
# 
# The methods below are common to all the data visualisation articles I've come across
# Fabio Fabrizi

# Import pandas
import pandas as pd

# Read the csv file - note that in this project it's in the same folder
df = pd.read_csv("iris.csv")

# Print the top 5 rows
print(df.head())

# Get the shape of the dataset
print(df.shape)



# NB:
# df.head() might not be necessary, but it's just a 
# quick way of seeing the columns/rows of the dataset