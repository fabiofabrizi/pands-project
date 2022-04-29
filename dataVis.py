# This is the Data Visualisation part of the project
# 
# Fabio Fabrizi


from regex import R
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# From EDA.py, we know how many species there are: 3
# Lets see it visually, counting the number of each

# Below line is important - it's what allows the rest to work
# as it defines the dataframe that's being examined.
df = pd.read_csv("iris2.csv")


# plt.show() is commented out as it was just for testing
def species():
    sns.set(style="darkgrid")
    ax =sns.countplot(x = 'species', data=df, palette='husl' )
    ax.set_title('Iris Species',fontsize = 16, fontweight='bold' )
    ax.set_xlabel('Individual Species', fontsize = 15)
    ax.set_ylabel('Species count', fontsize = 15)
    #plt.show()
    plt.savefig('Data Visualisation/species-plot.png',  bbox_inches='tight')
    return

# Now lets look at sepal length and sepal width
# to see if any patterns are emerging

def sepal_relation():
    
    sns.FacetGrid(df, hue="species",
                height = 8).map(plt.scatter,
                                'sepal_width',
                                'sepal_length').add_legend()
    # Setting title and labels for x and y axes                            
    plt.title("Sepal Length vs Sepal Width of each species", fontsize = 16, fontweight='bold')
    plt.xlabel("Sepal Width cm", fontsize = 15 )
    plt.ylabel("Sepal Length cm", fontsize = 15)
    #plt.show()
    plt.savefig('Data Visualisation/sepal_length_width.png',  bbox_inches='tight')
    return


def petal_relation():
    sns.FacetGrid(df, hue="species",
                height = 8).map(plt.scatter,
                                'petal_length',
                                'petal_width').add_legend()
    # Setting title and labels for x and y axes
    plt.title("Petal Length vs Petal Width of each species", fontsize = 16, fontweight='bold')
    plt.xlabel("Petal Length cm", fontsize = 15 )
    plt.ylabel("Petal Width cm", fontsize = 15 )
    #plt.show()
    plt.savefig('Data Visualisation/petal_length_width.png', bbox_inches='tight')
    return

# Petal Length and Sepal Length across the three species:
    
def petal_sepal_length_relation():
    plt.figure(figsize=(10,6))
    sns.set(style="darkgrid")
    plt.title("Petal Length vs Sepal Length of each species", fontsize = 16, fontweight='bold')
    sns.color_palette("Paired")
    sns.scatterplot( data= df,
                x="sepal_length", y="petal_length",
                hue="species"
                    )
    plt.xlabel("Sepal Length cm", fontsize = 15 )
    plt.ylabel("Petal Length cm", fontsize = 15 )
    plt.savefig('Data Visualisation/petal_sepal_length.png',  bbox_inches='tight')
    return

def petal_sepal_width_relation():
    plt.figure(figsize=(10,6))
    sns.set(style="darkgrid")
    plt.title("Petal Width vs Sepal Width of each species", fontsize = 16, fontweight='bold')
    sns.color_palette("Paired")
    sns.scatterplot( data= df,
                x="sepal_width", y="petal_width",
                hue="species"
                    )
    plt.xlabel("Sepal Width cm", fontsize = 15 )
    plt.ylabel("Petal Width cm", fontsize = 15 )
    #plt.show()
    plt.savefig('Data Visualisation/petal_sepal_width.png',  bbox_inches='tight')
    return



# Now Let's look at the attributes using a scatterplot within seaborn
def pair_plots():
    # Set title below
    sns.set(style="darkgrid")
    pp = sns.pairplot(df, hue="species", height = 2, palette = 'colorblind')
    #pp.add_legend(title="Relationships between all pairs of variables")
    pp.fig.suptitle("Relationships between all variables", y=1.08, fontsize = 16, fontweight='bold')
    cn = ['setosa', 'versicolor', 'virginica']
    #sns.pairplot(df, hue="species", height = 2, palette = 'colorblind')
    #plt.show()
    plt.savefig('Data Visualisation/pair_plots.png', bbox_inches='tight')
    return

# Box plots to show the median and the quartiles of each variable.
def box_plots():
    sns.set(style="darkgrid")
    sns.set_palette("husl")
    fig, axes = plt.subplots(2, 2, figsize=(16,9))
    fig.suptitle("Box Plots to show the min, max, median and quartiles of each variable", fontsize = 16, fontweight='bold')
    sns.boxplot( y='petal_width', x= 'species', data=df, orient='v' , ax=axes[0, 0])
    sns.boxplot( y='petal_length', x= 'species', data=df, orient='v' , ax=axes[0, 1])
    sns.boxplot( y='sepal_length', x= 'species', data=df, orient='v' , ax=axes[1, 0])
    sns.boxplot( y='sepal_width', x= 'species', data=df, orient='v' , ax=axes[1, 1])
    #plt.show()
    plt.savefig('Data Visualisation/box_plots.png')
    return


# Violin plots overlaid on box plots to show the frequency distribution of the data 
# and how that might affect the numbers that we see.

def box_violin_plots():
    sns.set(style="darkgrid")
    fig, axes = plt.subplots(2, 2, figsize=(16,9))
    fig.suptitle("Violin Plot overlaid on Box Plot to show frequency distribution by species", fontsize = 16, fontweight='bold')
    #plt.title("Violin Plot & Box Plot to show frequency distribution")
    sns.set_palette("husl")
    sns.boxplot( y='petal_width', x= 'species', data=df, orient='v' , ax=axes[0, 0] )
    sns.violinplot( y='petal_width', x= 'species', data=df, orient='v' , ax=axes[0, 0] )
    sns.boxplot( y='petal_length', x= 'species', data=df, orient='v' , ax=axes[0, 1] )
    sns.violinplot( y='petal_length', x= 'species', data=df, orient='v' , ax=axes[0, 1] )
    sns.boxplot( y='sepal_length', x= 'species', data=df, orient='v' , ax=axes[1, 0] )
    sns.violinplot(y='sepal_length', x= 'species', data=df, orient='v' , ax=axes[1, 0] )
    sns.boxplot( y='sepal_width', x= 'species', data=df, orient='v' , ax=axes[1, 1] )
    sns.violinplot(y='sepal_width', x= 'species', data=df, orient='v' , ax=axes[1, 1] )
    #plt.show()
    plt.savefig('Data Visualisation/box_violin_plots.png')
    return

# Histogram testing
# draw a histogram,   the kde =False indicates that the kernel function estimation graph is not displayed. 
# it is set as False.
def histo_plots():
    # Below we're specifying an area for 2x2 plots
    sns.set(style="darkgrid")
    fig, axes = plt.subplots(2, 2, figsize=(16, 9))
    fig.suptitle("Histograms of all the variables", fontsize = 16, fontweight='bold')
    sns.histplot(df.petal_length, color="gold", kde=False, ax=axes[0, 0]).set_xlabel("Petal Length in cm")
    sns.histplot(df.petal_width, color="teal", kde=False, ax=axes[0, 1]).set_xlabel("Petal Width in cm")
    sns.histplot(df.sepal_length, color="skyblue", kde=False, ax=axes[1, 0]).set_xlabel("Sepal Length in cm")
    sns.histplot(df.sepal_width, color="olive", kde=False, ax=axes[1, 1]).set_xlabel("Sepal Width in cm")
    #plt.show()
    plt.savefig('Data Visualisation/histograms.png')
    return

def kde():
    plt.title("Kernel Density Estimation of petal length", y=1.08)
    sns.set(style="darkgrid")
    sns.color_palette("Paired")
    sns.displot(df, x="petal_length", hue="species", kind="kde" )
    plt.xlabel("Petal Length cm")
    #plt.show()
    plt.savefig('Data Visualisation/kde.png', bbox_inches='tight')
    return    

def species_histo():
    sns.set(style="darkgrid")
    sns.color_palette("colorblind")
    sns.histplot(df, x="petal_length", hue="species", bins=30 ).set(title="Histograms of each species")
    plt.xlabel("Petal Length cm")
    #plt.show()
    plt.savefig('Data Visualisation/species_histo.png', bbox_inches='tight')
    return



# Function calls for testing
# Commented out because analysis.py is 
# doing the calling of the functions below.
petal_relation() 
sepal_relation()
species()
petal_sepal_length_relation()
petal_sepal_width_relation()
pair_plots()
box_plots()
box_violin_plots()
histo_plots()
kde()
species_histo()