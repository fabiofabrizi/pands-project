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

# At the time of writing, I have the below versions:
# Python: 3.9.12
# numpy: 1.22.3