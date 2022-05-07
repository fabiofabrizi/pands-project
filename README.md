# pands-project



<div align="center">
    <h2 align="center">pands-project</h2>
    <p align="center">This is the repository for the programming and scripting module project - The Iris Dataset</p>
    <img src="images/RHS_setosa_1050.jpg" alt="Iris Setosa" width="500" height="500">
</div>


<!-- TABLE OF CONTENTS -->
# Table of Contents
1. **[About The Project](#about-the-project)**
2. **[Aims](#aims)**
3. **[Getting Started](#getting-Started)**
4. **[Research](#research)**
5. **[Methodology](#methodology)**
6. **[Files](#files)**
7. **[Results](#results)**
8. **[Conclusion](#conclusion)**
9. **[References](#references)**



<br>
<br>

## About The Project

This is the project for the Programming and Scripting module - Higher Diploma in Data Analytics.
Fisher's Iris Dataset is to be researched, and documentation (my opinions) and code (Python) must be produced.  
Fisher's Iris Dataset is also known as the *Iris* flower dataset and is a multivariate data set introduced by the 
British statistician and biologist Ronald Fisher in 1936.  

The term *Multivariate* means that multiple variables are in the dataset:  
[1] sepal length  
[2] sepal width  
[3] petal length   
[4] petal width  

All the variables are measured in centimetres (cm).

A sepal is the part of a flower that functions as protection for a flower in bud, and often as support for the petals when in bloom.

<img src="images/640px-sepal.svg.png" alt="Sepal Explanation" >


There are three species of Iris in the data set:  
[1] 'Iris Setosa'  
[2] 'Iris Versicolor'  
[3] 'Iris Virginica'

There are 50 samples of each species, as highlighted by the graph below:

<img src="Data Visualisation/species-plot.png" alt="Bar chart of iris species"> 
<br>  
<br>
Reviewing the numerous blogs and articles written on Fisher's Iris dataset, the common theme is the use of the Python or R languages to analysis and identify any patterns.
This pattern is also common for other data analysis/visualisation projects.  

<br>  
<br>  

## Aims 

The task, is to take the dataset and:  
1) Learn why the data is collected in the first place
2) Use Python to learn about the variables within the dataset
3) Explain to others how to identify what type of Iris they have.

<br>  
<br>  


## Getting Started

I started by creating the Github repository 'pands-project' and added the dataset to it converted from a data file.
The script for conversion is included. 
The dataset has been characterised with python scripts and the use of statistical analysis in order to produce plots of the variables.   
It has been done in this way so that I might infer what variables are responsible for identifying the species and distinguishing them from one another.
  
Explanations of the files in this repository are below.
<br>  
<br>


## Research

**[1] The Mother**

I have no background in horticulture - the furthest my expertise extends to is mowing the grass and a small herb garden.
However, my mother is a keen gardener, she told me about a scenario that occurs fairly often with her:
1) She wants to find out what type of plant/tree/flower/etc she's come across
2) She takes a picture and some measurements and any other relevant information (acidity of soil, type of shade, etc.)
3) She then emails RHS (Royal Horticultural Society - she lives in the UK)
4) Within a few days, someone has responded with the answer. 

So there's a *real-life example* of a data set point being checked against a data set (or many) in order to produce an answer. 

**[2] The internet**  

 
When one googles 'Iris dataset' there's lots of results - Too many for me to examine every single one.

Some have approached the problem from a Machine Learning angle and have applied appropriate libraries in order to develop models, etc so that when a data set of iris species are plugged in, the model can tell you which one it is.

Some have plotted every single histogram/pie chart/scatter plot/etc known to man. 

I have taken neither approach, instead focusing on whether I can find out enough about the three Iris species to explain the differences to colleagues at work and the **minimum most important statistical analysis** that needs to be done in order to do this.   
The reason for me doing so is being aware of time constraints and the fact that my audience might only have two or three minutes to listen to me.

Other relevant links are inluded in the python files and/or in the 'References' section below. 
<br>  
<br>

## Methodology

From all the various articles on data analysis and data visualisation (aimed at beginners in this field) that I've encountered, there's a common pattern:

i) Get the dataset  
ii) Check the dataset for null values and remove them  
iii) Characterise the dataset and associated data - ie How many rows/columns, mean/max/min values etc  
iv) Apply some statistical analysis to get a visual representation of the data  
v) Examine the visual representation - Does it show a pattern or something unique that I can use to understand the data set  

From the process above, one can take a data set and apply the above steps to look for any unique patterns in the data.
<br>  
<br>


## Files

An explanation of the files in this repository is below:

**converter2.py**  
This pulls directly from the main data set archive at UCI (University Of California, Irvine) and converts it to a CSV format with headers.  
The call to the function is commented out because *analysis.py* calls it.
As a precaution, in case there's any issues with reading from remote machine, I've also included
the file 'iris.data' which is from UCI.  
The file does the task of i) from **Methodology**.

**iris2.csv**  
This is the result of converter2.py being run.

**env_var.py**  
This is the script that tells the user what versions of software is installed on the local machine.
The output of this is not printed to analysis.txt as it's only intended to be run if there's something wrong.
If it's run, the output is printed to the terminal.

**EDA.py**  
This is the Exploratory Data Analysis of the Iris Data set. I check for missing values, duplicates, etc.
Descriptive statistics are also generated here so that I can quickly see the following:
- count: (The number of not-empty values)
- mean: (The average (mean)) value
- std: The standard deviation
- min: The minimum value
- 25%: The 25% percentile
- 50%: The 50% percentile
- 75%: The 75% percentile
- max: The maximum value  

The function is called from analysis.py  
This file does the task of ii) and iii) from **Methodology**.


**dataVis.py**  
dataVis.py generates all the visualisations and saves them in the 'Data Visualisation' folder.
The plots saved are '.png' file format.  
Code comments are used to explain what each function does.
This file performs iv) and v) from Preliminary Findings.  
I'm examining: 
- Sepal length and width of the species and looking for patterns,
- Petal length and width and looking for patterns,
- Correlation (if any) between any variables so that I might infer what's important when examining the three species.


**analysis.py**  
This calls the functions from the following files so that only one file needs to be run:  
[1] *converter2.py*  
[2] *EDA.py*  
[3] *dataVis.py*  

I've done it in this way because I've split it up into parts and thought if the project scope changed it would be better for maintenance or bug fixing if analysis.py just did the function calls. 
The file is commented with explanations about the functions.


**analysis.txt**  
This is the text file that's required to be generated - All that is contained in the file is text, and is a quick way to get an overview of the dataset. This file is generated from running *analysis.py* at the command line.

## Folders

There's only three folders, 'Data Visualisation', 'Images' and 'Resources'.  
*Images* has two images:  
[1] The image you see at the top of this file  
[2] The image in the *About The Project' section to explain what a sepal is.  

*Data Visualisation* is where the all the plots have been saved. I've tried to name them as intuitively as possible, so
that one might look at the name and infer what the plot does.

*Resources* contains a the iris dataset in csv and data formats so that if there's any issue with the user running the script to pull the data remotely than they can change the script and point it to the local copy.

## Results

Examining *analysis.txt* indicates whether I can quickly infer anything about the data set, before looking at plots for visual indications of the statistics.  

*Standard deviation* is the average amount of variability for that score, i.e. how far away it is from the mean.  
It can be seen from the general descriptive statistics at the end of *analysis.txt* that sepal width has the smallest standard deviation and petal length the largest.  

However, when the statistics of each species are examined seperately, it can be seen that:
- *'Iris Setosa'* has the smallest deviations in petal length and width but the largest in sepal width.
- *'Iris Virginica'* has the largest deviations in sepal length and petal length.
- *'Iris Versicolor'* is somewhere inbetween the two in terms of standard deviations of it's features.  

From quickly glancing at the minimum and maximum values of the variables, it can be seen that *'Iris Setosa'* is the 
smallest of the three species, whereas with *'Iris Virginica'* there seems to be a large variation in how large the plant (flower) can be.

Further progressing from the above results, further investigations of the variables will indicate whether the layperson can identify any distinguishing features of the three species.
<br>
<br>

**Histograms**

A histogram is a type of plot that visualises the frequency distribution (also known as shape) of a set of data.
A histogram is different to a bar chart because the bars are connected to each other, unlike a bar chart for categorical data. 
It can be thought of as a picture of the data and in the histograms below:
- The height of each bar represents the count of each iris (frequency) of that variable

<img src="Data Visualisation/histograms.svg" alt="Histograms of variables">  

Sepal length and sepal width seem to have the only normal distributions whereas petal length and petal width seem 
to have a distribution below the median (known as negatively skewed).  
<br>

**Box Plots**

A box plot is a type of plot that takes data and shows us the minimum, maximum, median and first and third quartiles. The box plot is included below as a way of visually confirming what was seen in analysis.txt.

<img src="Data Visualisation/box_plots.svg" alt="Box plots of species">  

Analysing the box plots above confirms initial observations about *'Iris Setosa'* - that is, it has the smallest deviations in petal length and width and the largest variation in sepal width.  

Analysis of the box plots also shows that *'Iris Setosa'* and *'Iris Virginica'* are quite seperate to each other in terms of their characteristics - *'Iris Virginica'*, apart from sepal width, has greater variation across all characteristics.

For *'Iris Versicolor'* there's an overlap at the top of the range (4.5 - 5.2cm) with *'Iris Virginica'* as confirmed by the box plot.

Thus, from examination of the box plots, it can be inferred that *petal length* and *petal width* (in cm) are the best variables to distinguish between the species as all the others have overlapping ranges.





**Violin Plots**

Violin plots are used to visualise the frequency distribution of a data set and it's probability density.
This is done to see how the frequency distribution affects the numbers, i.e. are there any outliers that are skewing the data?

The violin plots are overlaid on top of the box plots to have visual representation of the statistics.

<img src="Data Visualisation/box_violin_plots.svg" alt="Box plots of species">

From looking at the above plots it can be observed that:
- *'Iris Setosa'* has some outliers when it comes to sepal width, potentially be skewing the results.
- *'Iris Virginica'* has some outliers around sepal length.  

<br>
<br>
<br>


**Sepal and Petal Relationships: Sepal Width vs Length and Petal Width vs Length**


<img src="Data Visualisation/combined_sepal_petal_relationships.svg" alt="Sepal length and width">



Examining the scatterplot above of *Sepal Width vs Length* it can be observed:  
- *'Iris Setosa'* has larger sepal widths but smaller sepal lengths
- *'Iris Virginica'* has larger sepal lengths but smaller sepal widths
- *'Iris Versicolor'* is somewhere inbetween the two species in terms of sepal length and width.


Examining the scatterplot above of *Petal Width vs Length* it can be observed:  
- *'Iris Setosa'* has smaller petal lengths and widths than the other two species  
- *'Iris Virginica'* has the largest petal lengths and widths of all three species  
- *'Iris Versicolor'* is once again inbetween the two species in terms of petal lengths and widths  


**Sepal and Petal Relationships: Sepal vs Petal Length and Sepal vs Petal Width**  



<img src="Data Visualisation/sepal_petal_relationships.svg" alt="Relationships between sepals and petals">


Examining the plots above: 
*sepal vs petal length* and *sepal vs petal width*
- *'Iris Setosa'* is the smallest of the three species 
- *'Iris Virginica'* is the largest
- *'Iris Versicolor'* is inbetween the two in terms of size.  

The above two plots indicate to the layperson the smallest and largest species of iris in the dataset.
At this point, visual representation of statistics have been used to indicate to the reader which variables should be considered in order to identify between the three species.

Examination of the four plots above indicate that *petal length* and *petal width* are the variables to focus on.  

<br>
<br>


**Pair Plots**

Pair plots are used to observe the relationship between two variables.

<img src="Data Visualisation/pair_plots.svg" alt="Pair plots">

The above plot is  a scatter plot of all pairs of attributes.  
If I could only present one plot to my audience, it would be this one, as it can be seen that petal length and width are highly correlated.
- *'Iris Setosa'* is clearly apart from the other two species as it has the smallest petal lengths and widths.  
- *'Iris Setosa'* also has the smallest sepal lengths but wider sepal widths than the other two species.

**Potential Limitations**
Although the pair plots work well for a data set of this size (150), it's clear that they might not work so well for very large data set sizes for rows that number in the thousands or tens of thousands.
This is dependent on the amount of RAM on the users machine and two workarounds are suggested:  
[1] Take a sample of the dataset and use pair plots to visualise the relationship between the variables  
[2] Use software like Dask to work with tools like pandas, numpy, etc on large datasets

**Petal Length and Width**

Examining the *petal length* and *petal width* variables in more detail, *petal length* has a steeper frequency distribution, indicating that if this variable was chosen instead of *petal width* to distinguish between the species there would be less margin for error.  
However, as each species has only fifty samples and outliers have been observed from the violin plot, I'm going to consider both *petal length* and *petal width*.

The *petal length* and *petal width* variables can be examined in more detail by plotting *Kernel Density Estimation* - which is a way to estimate the probability function of a variable.

<br>
<br>


<img src="Data Visualisation/kde_species_histo.svg" alt="Histogram of each iris species"> 

<br>
<br>

**Examining the *petal length* variable:**  

The plot indicates that the two species *'Iris Versicolor'* and *'Iris Virginica'* have a cross-over at 4.8cm between them.  
Examining the samples of 'Iris Verisicolor' and 'Iris Virginica' above and below the 4.8cm mark for *petal length* respectively:
- *'Iris Versicolor'* would have an estimation error of 12% (6/50 x 100) as 6 samples are over 4.8cm.
- *'Iris Virginica'* would have an estimation error 2% (1/50 x 100) as 1 sample is less than 4.8cm.

Note that these errors would only occur for petal length measurements between 4.6 and 5.2cm and below or above these values there would be no errors distinguishing between the three species.

As a result of the analysis above a formula can be reached with regarding to categorising the three species based on *petal length*:

[1] If 1 < 'petal length' < 1.9, then the iris species is *'Iris Setosa'*  
[2] If 3 < 'petal length' < 4.8, then the iris species is *'Iris Versicolor'*   
[3] If 4.8 < 'petal length' < 6.9, then the iris species is *'Iris Virginica'*
<br>
<br>

**Examining the *petal width* variable:**  

The plot indicates that the two species *'Iris Versicolor'* and *'Iris Virginica'* have a cross-over at 1.7cm between them.
Examining the samples of 'Iris Verisicolor' and 'Iris Virginica' above and below the 1.7cm mark for *petal width* respectively:  
- *'Iris Versicolor'* would have an estimation error of 4% (2/50 x 100) as 2 samples are over 1.7cm.
- *'Iris Virginica'* would have an estimation error of 10% (5/50 x 100) as 5 samples are less than  1.7cm.  

Note that these errors would only occur for *petal width* measurements between 1.4 and 1.8 respectively as above or below these values there would be no errors distinguishing between the three species.
Also note that in real life, measurement error would have to be taken into consideration because the botanist/researcher/etc would be measuring the petal width in millimetres (mm).

As a result of the analysis above a formula can be reached with regarding to categorising the three species based on *petal width*:  

[1] If 0.1 < 'petal width' < 0.6 then the iris species is *'Iris Setosa'*   
[2] If 1 < 'petal width < 1.8 then the iris species is *'Iris Versicolor'*  
[3] If 1.4 < 'petal width < 2.5 then the iris species is *'Iris Virginica'*  


## Conclusion 


*Petal length* and *petal width* are the best variables to distinguish between the three species as confirmed by   
[i] Box plots  
[ii] Scatter plots  
[iii] Pair plots  
[iv] Histograms

The four plots listed above are the ones that I would have in my presentation to colleagues, with possibly the addition of the violin plot overlaid on the box plot to identify any outliers.  

- *'Iris Setosa'* could be seperated from the other species by looking at the basic statistics in *analysis.txt* (it's the smallest)
- *'Iris Setosa'* is the only species that can clearly (visually) be separated from the other two species by *petal length* and *petal width*.


The dataset was first collected to learn more about the three Iris species - whether as part of taxonomy of the species and/or for research.

Python was used along with libraries like matplotlib, numpy and seaborn to learn more about the variables in the data set and the relationship(s) between each other.  

Visually representing the statistical analysis allows the layperson to infer characteristics of the data without being a statistics expert.

From analysis of the variables, *petal length* and *petal width* were identified as being able to identify between the three iris species with an acceptable degree of error.

The methodology applied to the analysis of this dataset can also be applied to other datasets.
<br>
<br>
<br>

## References

**[Fishers Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)**  
**[Maths is fun](https://www.mathsisfun.com/data/standard-deviation.html)**  
**[Statistics and Standard Deviation](https://www.statisticshowto.com/probability-and-statistics/standard-deviation/)**  
**[Choosing the right visualisation techniques for extracting data insights](https://medium.com/analytics-vidhya/choosing-the-right-visualization-techniques-for-extracting-data-insights-34466c9f26e4)**  
**[Pandas describe() method](https://www.w3schools.com/python/pandas/ref_df_describe.asp#:~:text=The%20describe()%20method%20returns,The%20average%20(mean)%20value.)**  
**[Box Plots](https://www.w3schools.com/statistics/statistics_box_plots.php?msclkid=c53adf08c60711ec81a7efa0203468fb)**  
**[A Complete Guide to Violin Plots](https://chartio.com/learn/charts/violin-plot-complete-guide/#:~:text=Violin%20plots%20are%20used%20when%20you%20want%20to,to%20see%20where%20groups%20are%20similar%20or%20different.?msclkid=2e64438ec60a11ecbbceb90391cc19fe)**  
**[How to fix title being cut off in Seaborn](https://github.com/mwaskom/seaborn/issues/2072)**  
**[Probability Density Function](https://en.wikipedia.org/wiki/Probability_density_function)**
**[Kernel Density Estimation (KDE)](https://en.wikipedia.org/wiki/Kernel_density_estimation#:~:text=In%20statistics%2C%20kernel%20density%20estimation,on%20a%20finite%20data%20sample.)**  
**[Statistics by Jim](https://statisticsbyjim.com/basics/percentiles/#:~:text=Percentiles%20indicate%20the%20percentage%20of,91%20percent%20of%20other%20scores.)**  
**[What is a Sepal?](https://en.wikipedia.org/wiki/Sepal)**  
**[Markdown guide](https://www.markdownguide.org/basic-syntax/)**  
**[Limitations of sns.pairplot for large datasets](https://www.kaggle.com/questions-and-answers/182729)**  
**[Seaborn Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)**