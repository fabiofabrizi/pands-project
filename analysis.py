# The intention of this file is to call other python scripts/files,
# so that by running this one file you can output all the files that you need.
# 
# Fabio Fabrizi


# import from the other files
from converter2 import *
from EDA import *
from dataVis import *

# Convert the data first
convert_data()

# Exploratory Data Analysis next
exploratory()

# Print Preliminary results to text file - see analysis.txt in folder
eda_to_text()

# Plot of species count - This is just a visual representation of 
# df.value_counts("species")
species()

# Examination of sepal length and width of the three species
petal_relation() 
sepal_relation()
species()