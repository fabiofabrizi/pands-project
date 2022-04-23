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


# plt.show() is commented out as it was just for testing
def species():
    sns.countplot(x='species', data=df, )
    # Setting title and labels for x and y axes
    plt.title("Iris Species")
    plt.xlabel("Species")
    plt.ylabel("Count")
    #plt.show()
    plt.savefig('Data Visualisation/species-plot.png')
    return

# Now lets look at sepal length and sepal width
# to see if any patterns are emerging

def sepal_relation():
    
    sns.FacetGrid(df, hue="species",
                height = 8).map(plt.scatter,
                                'sepal_width',
                                'sepal_length').add_legend()
    # Setting title and labels for x and y axes                            
    plt.title("Sepal Length vs Sepal Width of each species")
    plt.xlabel("Sepal Width cm")
    plt.ylabel("Sepal Length cm")
    #plt.show()
    plt.savefig('Data Visualisation/sepal_length_width.png')
    return


def petal_relation():
    sns.FacetGrid(df, hue="species",
                height = 8).map(plt.scatter,
                                'petal_length',
                                'petal_width').add_legend()
    # Setting title and labels for x and y axes
    plt.title("Petal Length vs Petal Width of each species")
    plt.xlabel("Petal Length cm")
    plt.ylabel("Petal Width cm")
    #plt.show()
    plt.savefig('Data Visualisation/petal_length_width.png')
    return

# Petal Length and Sepal Length across the three species:
def petal_sepal_length_relation():
    sns.FacetGrid(df, hue="species",
                height = 8).map(plt.scatter,
                                'sepal_length',
                                'petal_length').add_legend()
    # Setting title and labels for x and y axes
    plt.title("Petal Length vs Sepal Length of each species")
    plt.xlabel("Sepal Length cm")
    plt.ylabel("Petal Length cm")
    #plt.show()
    plt.savefig('Data Visualisation/petal_sepal_length.png')
    return

def petal_sepal_width_relation():
    sns.FacetGrid(df, hue="species",
                height = 8).map(plt.scatter,
                                'sepal_width',
                                'petal_width').add_legend()
    # Setting title and labels for x and y axes
    plt.title("Petal Width vs Sepal Width of each species")
    plt.xlabel("Sepal Width cm")
    plt.ylabel("Petal Width cm")
    #plt.show()
    plt.savefig('Data Visualisation/petal_sepal_width.png')
    return

# Now we can dig deeper using multivariate analysis
# https://www.mygreatlearning.com/blog/introduction-to-multivariate-analysis/
# Why? Because the data set is multivariate


# Function calls for testing
# Commented out because analysis.py is 
# doing the calling
petal_relation() 
sepal_relation()
species()
petal_sepal_length_relation()
petal_sepal_width_relation()

