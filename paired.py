# This is the Data Visualisation part of the project
# 
# Fabio Fabrizi

from converter2 import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("iris2.csv")

"""
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

#plt.show()

"""
"""
# Below is working
fig, axes = plt.subplots(2, 2, figsize=(16,9))
fig.suptitle("Violin Plot & Box Plot to show frequency distribution by species")
#plt.title("Violin Plot & Box Plot to show frequency distribution")
sns.boxplot( y='petal_width', x= 'species', data=df, orient='v' , ax=axes[0, 0] )
sns.violinplot( y='petal_width', x= 'species', data=df, orient='v' , ax=axes[0, 0] )
sns.boxplot( y='petal_length', x= 'species', data=df, orient='v' , ax=axes[0, 1] )
sns.violinplot( y='petal_length', x= 'species', data=df, orient='v' , ax=axes[0, 1] )
sns.boxplot( y='sepal_length', x= 'species', data=df, orient='v' , ax=axes[1, 0] )
sns.violinplot(y='sepal_length', x= 'species', data=df, orient='v' , ax=axes[1, 0] )
sns.boxplot( y='sepal_width', x= 'species', data=df, orient='v' , ax=axes[1, 1] )
sns.violinplot(y='sepal_width', x= 'species', data=df, orient='v' , ax=axes[1, 1] )
plt.show()
"""
"""
# draw a histogram,   the kde =False indicates that the kernel function estimation graph is not displayed. 
# it is set as False.
fig, axes = plt.subplots(2, 2, figsize=(16,9))
sns.displot(df.sepal_length,bins=8, kde=False)
sns.displot(df.sepal_width,bins=13, kde=False)
sns.displot(df.petal_length, bins=5, kde=False)
sns.displot(df.petal_width, bins=5,kde=False)
plt.show()
"""
"""
# Violin plot overlaid on box plot to show frequency distribution
#calyx length 
sns.boxplot(x='species', y='sepal_length', data=df)
sns.violinplot(x='species', y='sepal_length', data=df)
plt.title('SepalLengthCm data by Species')
#calyx width 
sns.boxplot(x='species', y='sepal_width', data=df)
sns.violinplot(x='species', y='sepal_width', data=df)
plt.title('SepalWidthCm data by Species')
#petal length 
sns.boxplot(x='species', y='petal_length', data=df)
sns.violinplot(x='species', y='petal_length', data=df)
plt.title('PetalLengthCm data by Species')
#petals width 
sns.boxplot(x='species', y='petal_width', data=df)
sns.violinplot(x='species', y='petal_length', data=df)
plt.title('PetalWidthCm data by Species')
plt.show()

"""
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
    #plt.savefig('Data Visualisation/petal_sepal_width.png')
    return

#petal_sepal_width_relation()

def histo_plots():
    # Below we're specifying an area for 2x2 plots
    sns.set(style="darkgrid")
    fig, axes = plt.subplots(2, 2, figsize=(16, 9))
    fig.suptitle("Histograms of all the variables")
    sns.histplot(df.sepal_length, color="skyblue", kde=False, ax=axes[0, 0])
    sns.histplot(df.sepal_width, color="olive", kde=False, ax=axes[0, 1])
    sns.histplot(df.petal_length, color="gold", kde=False, ax=axes[1, 0])
    sns.histplot(df.petal_width, color="teal", kde=False, ax=axes[1, 1])
    #plt.show()
    plt.savefig('Data Visualisation/histograms.png')
    return
"""
plt.figure(figsize=(16,9))
sns.set(style="darkgrid")
sns.color_palette("Paired")
sns.scatterplot( data= df,
               x="sepal_width", y="petal_width",
               hue="species"
                ).set(title="Petal Width vs Sepal Width of each species")
plt.xlabel("Sepal Width cm")
plt.ylabel("Petal Width cm")
#plt.show()


plt.figure(figsize=(16,9))
sns.set(style="darkgrid")
sns.color_palette("Paired")
sns.scatterplot( data= df,
            x="sepal_length", y="petal_length",
            hue="species"
                ).set(title="Petal Length vs Sepal Length of each species")
plt.xlabel("Sepal Length cm")
plt.ylabel("Petal Length cm")
#plt.show()

"""

"""
# Petal Length and petal width
plt.figure(figsize=(16,9))
sns.set(style="darkgrid")
sns.color_palette("Paired")
sns.scatterplot( data= df,
            x="petal_length", y="petal_width",
            hue="species"
                ).set(title="Petal Length vs Petal Width of each species")
plt.xlabel("Petal Length cm")
plt.ylabel("Petal Width cm")
plt.show()
"""

"""
# petal length
sns.FacetGrid(df, hue="species", height=5) \
   .map(sns.distplot, "petal_length") \
   .add_legend();
#plt.show()
"""
#plt.figure(figsize=(10,6))
sns.set(style="darkgrid")
sns.color_palette("Paired")
sns.displot(df, x="petal_length", hue="species", kind="kde" )
plt.xlabel("Petal Length cm")
#plt.show()