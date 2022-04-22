# The intention of this file is to call other python scripts/files,
# so that by running this one file you can output all the files that you need.
# 
# Fabio Fabrizi


# import from the other files
from converter2 import *
from EDA import *


# Convert the data first
convert_data()

# Exploratory Data Analysis next
exploratory()

# Print Preliminary results to text file - see analysis.txt in folder
eda_to_text()