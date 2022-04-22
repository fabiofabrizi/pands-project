# This is the Data Visualisation part of the project
# 
# Fabio Fabrizi


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp


# From EDA.py, we know how many species there are: 3
# Lets see it visually, counting the number of each
df = pd.read_csv("iris2.csv")

def species():
    sns.countplot(x='species', data=df, )
    plt.title("Iris Species")
    plt.xlabel("Species")
    plt.ylabel("Count")
    plt.savefig('Data Visualisation/species-plot.png')
    return