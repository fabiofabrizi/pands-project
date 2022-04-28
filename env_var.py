# Run this if there's any issues with outputs. Running the script will 
# show you the versions of the packages that you have installed. 
# Resource:
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# 
# Fabio Fabrizi

# Script to check what package versions are being used:

# Python version:
import sys
print('Python: {}'.format(sys.version))

# Numpy version:
import numpy
print('numpy: {}'.format(numpy.__version__))

# Matplotlib version
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

# Pandas 
import pandas
print('pandas: {}'.format(pandas.__version__))

# Seaborn
import seaborn
print('seaborn: {}'.format(seaborn.__version__))
# At the time of writing, I have the below versions:
# Python: 3.9.12
# numpy: 1.22.3
# matplotlib: 3.5.1
# pandas: 1.4.1
# seaborn: 0.11.2