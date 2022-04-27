# This is the Data Visualisation part of the project
# 
# Fabio Fabrizi

from converter2 import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("iris2.csv")


fig, ax = plt.subplots(2, figsize=(10, 16))
ax[0].scatter(x = 'sepal_length', y = 'sepal_width', data=df, )
sns.FacetGrid(df, hue="species",
                height = 6).map(plt.scatter,
                                'sepal_length',
                                'petal_length').add_legend()
ax[0].set_xlabel("Sepal Length cm")
ax[0].set_ylabel("Sepal Width cm")

ax[1].scatter(x = 'petal_length', y = 'petal_width', data=df, )
ax[1].set_xlabel("Petal Length cm")
ax[1].set_ylabel("Petal Width cm")

plt.show()

fig, axes = plt.subplots(2, 2, figsize=(16,9))
sns.boxplot( y='petal_width', x= 'species', data=df, orient='v' , ax=axes[0, 0])
sns.boxplot( y='petal_length', x= 'species', data=df, orient='v' , ax=axes[0, 1])
sns.boxplot( y='sepal_length', x= 'species', data=df, orient='v' , ax=axes[1, 0])
sns.boxplot( y='sepal_width', x= 'species', data=df, orient='v' , ax=axes[1, 1])
plt.show()

"""
sns.scatterplot(x='sepal_length', y='sepal_width',
                hue='species', data=df, )
    # Labels for title, x and y axis
    plt.title("Sepal width & length characteristics of each species")
    plt.xlabel("Sepal Length cm")
    plt.ylabel("Sepal Width cm")
    plt.legend(bbox_to_anchor=(1, 1), loc="best")
    plt.show()
    #plt.savefig('Data Visualisation/sepal_length_width.png')
"""