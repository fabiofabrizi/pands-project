# This is the Data Visualisation part of the project
# 
# Fabio Fabrizi


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# From EDA.py, we know how many species there are: 3
# Lets see it visually, counting the number of each

# Below line is important - it's what allows the rest to work
# as it defines the dataframe that's being examined.
df = pd.read_csv("iris2.csv")

def species():
    sns.countplot(x='species', data=df, )
    plt.title("Iris Species")
    plt.xlabel("Species")
    plt.ylabel("Count")
    plt.savefig('Data Visualisation/species-plot.png')
    return

# Now lets look at sepal length and sepal width
# to see if any patterns are emerging

def sepal_relation():
    sns.scatterplot(x='sepal_length', y='sepal_width',
                hue='species', data=df, )
    # Labels for title, x and y axis
    plt.title("Sepal width & length characteristics of each species")
    plt.xlabel("Sepal Length cm")
    plt.ylabel("Sepal Width cm")
    plt.legend(bbox_to_anchor=(1, 1), loc="best")
    #plt.show()
    plt.savefig('Data Visualisation/sepal_length_width.png')
    return


def petal_relation():
    sns.scatterplot(x='petal_length', y='petal_width',
                hue='species', data=df, )
    # Labels for title, x and y axis
    plt.title("Petal width & length characteristics of each species")
    plt.xlabel("Petal Length cm")
    plt.ylabel("Petal Width cm")
    # Place legend in best spot
    plt.legend(bbox_to_anchor=(1, 1), loc="best")
    #plt.show()
    plt.savefig('Data Visualisation/petal_length_width.png')
    return



# Function calls for testing
# Commented out because analysis.py is 
# doing the calling
#petal_relation() 
#sepal_relation()
#species()


