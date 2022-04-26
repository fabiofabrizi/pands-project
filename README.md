# pands-project



<div align="center">
    <h2 align="center">pands-project</h2>
    <p align="center">This is the repo for the programming and scripting module project - The Iris Dataset</p>
    <img src="images/RHS_setosa_1050.jpg" alt="Iris Setosa" width="500" height="500">
</div>


<!-- TABLE OF CONTENTS -->
# Table of Contents
1. **[About The Project]("#about-the-project")**
2. **[Getting Started](#getting-Started)**
3. **[Why - What the task entails](#why-what-the-task-entails)**
4. **[Background](#background)**
5. **[Research](#research)**
6. **[Preliminary Findings](#preliminary-findings)**
7. **[Files](#files)**
8. **[Conclusions](#conclusions)**
9. **[References](#references)**


<!--
<div align="left">

  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
    <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#Why - What the task entails">Why - What the task entails</a>
        <li><a href="#Background">Background</a></li>
        <li><a href="#installation">Research</a></li>
    </li>
    <li><a href="#Preliminary Findings">Preliminary Findings</a></li>
    <li><a href="#Files">Files</a></li>
    <li><a href="#Conclusions">Conclusions</a></li>
    <li><a href="##References">References</a></li>
  </ol>

</div>
-->


## About The Project

This is the project for the Programming and Scripting module - Higher Diploma in Data Analytics.
Fisher's Iris Data set is to be researched, and documentation (my opinions) and code (Python) must be produced.



## Getting Started

I started by creating the Github repository 'pands-project' and added the data set to it converted from a data file.
The script for conversion is included. As I've delved deeper into the project, the repository has increased in size.
An explanation of the files in the repo is further below.



## Why - What the task entails

The task, as I understand it, is to take some data - in this case, about Irises
and interpret it in such a way that:
1) I learn why the data is collected in the first place
2) I can then explain to others, whether they have an interest (or not) in how to 
identify what type of Iris they have.
3) Why Python can be used to learn about the data



## Background

From looking at the many blogs/articles written on Fisher's Iris data set, the common theme amongst all of them is:

[1] A dataset  
[2] Python script(s) to analyse that dataset in order to make sense of the data and/or identify any patterns.  



## Research

[1] The Mother

I have no background in horticulture - the furthest my expertise extends to is mowing the grass and a small herb garden.
However, my mother is a keen gardener, she told me about a scenario that occurs fairly often with her:
1) She wants to find out what type of plant/tree/flower/etc she's come across
2) She takes a picture and some measurements and any other relevant information (acidity of soil, type of shade, etc.)
3) She then emails RHS (Royal Horticultural Society - she lives in the UK)
4) Within a few days, someone has responded with the answer. 

So there's a *real-life example* of a data set point being checked against a data set (or many) in order to produce an answer. 

[2] The internet - specific links are inluded in the python files and/or in the 'References' section below.  
When one googles 'Iris data set' there's lots of results - Too many for me to examine every single one.

Some have approached the problem from a Machine Learning angle and have applied appropriate libraries in order to develop models, etc so that when a data set of iris species are plugged in, the model can tell you which one it is.

Some have plotted every single histogram/pie chart/scatter plot/etc known to man. 

I have taken neither approach, instead focussing on whether I can find out enough about the three Iris species to explain the differences to colleagues at work and the **minimum most important statistical analysis** that needs to be done in order to do this. The reason for me doing so is that everyone is under time constraints, so they have the option of hearing more (digging deeper into the statistics) or ending the meeting because they feel they know enough.



## Preliminary Findings

From all the various articles (aimed at beginners in this field) that I've come across on this topic, there seems to be a common pattern:

i) Get the dataset  
ii) Check the dataset for null values and remove them  
iii) Get a 'feeling' for the dataset and associated data - ie How many rows/columns, mean/max/min values etc  
iv) Apply some statistical analysis to get a visual representation of the data  
v) Examine the visual representation - Does it show a pattern or something unique that we can use to understand the data set.  

From the process above, one can take a data set and apply the above steps to look for any unique patterns in the data.



## Files

There's lots of files - here's an explanation of them:

**converter2.py**  
This pulls directly from the main archive at UCI and converts it to a CSV format with headers
The call to the function is commented out because analysis.py calls it.
As a precaution, in case there's any issues with reading from remote machine, I've also included
the file 'iris.data' which is from UCI.
The file does the task of i) from Preliminary Findings.

**iris2.csv**  
This is the result of converter2.py being run.

**env_var.py**  
This is the script that tells the user what versions of software is installed on the local machine.
The output of this is not printed to analysis.txt as it's only intended to be run if there's something wrong.

**EDA.py**  
This is the Exploratory Data Analysis of the Iris Data set. We check for missing values, duplicates, etc.
Descriptive statistics are also generated here so that one can quickly see the following:
- count: (The number of not-empty values)
- mean: (The average (mean)) value
- std: The standard deviation
- min: The minimum value
- 25%: The 25% percentile
- 50%: The 50% percentile
- 75%: The 75% percentile
- max: The maximum value  

The function is called from analysis.py  
This file does the task of ii) and iii) from Preliminary Findings.


**dataVis.py**  
dataVis.py generates all the visualisations and saves them in the 'Data Visualisation' folder.
The plots saved are 'png' file format.  
Code comments are used to explain what each function does - in my opinion, there's a progression
with regards to the analysis.  
This file performs iv) and v) from Preliminary Findings.
We're examining: 
- Sepal length and width of the species and looking for patterns,
- Petal lengtha and width and looking for patterns,
- Correlation (if any) between any variables so that we might infer what's important when examining the three species.


**analysis.py**  
This calls the functions from the other files so that only one file needs to be run. I've done it in this way
because I've split it up into parts and thought if the project scope changed it would be better for maintenance 
or bug fixing if analysis.py just did the function calls. The file is commented with explanations about the functions.


**analysis.txt**  
This is the text file that's required to be generated - All that is contained in the file is text, and is a quick way to get an overview of the dataset.

## Folders

There's only three folders, 'Data Visualisation', 'Images' and 'Resources'.
*Images* has just one image and it's the image you see at the top of the README file.
*Data Visualisation* is where the all the plots have been saved. I've tried to name them as intuitively as possible, so
that one might look at the name and infer what the plot does.
*Resources* contains a the iris dataset in csv and data formats so that if there's any issue with the user running the script they can change the script and point it to the local copy.

## Conclusions

We can look at *analysis.txt* in order to see if we can quickly infer anything about the data set, before looking at plots and they information that they presented us with.  
*Standard deviation* tells us the average amount of variability for that score, i.e. how far away it is from the mean.  
So we can see from the general descriptive statistics at the end of *analysis.txt* that sepal width has the smallest standard deviation and petal length the largest.  
However, when we dive deeper and look at the statistics of each species seperately, we can see:
- 'Iris Setosa' has the smallest deviations in petal length and width but the largest in sepal width.
- 'Iris Virginica' has the largest deviations in sepal length and petal length.
- 'Iris Versicolor' is somewhere inbetween the two in terms of standard deviations of it's features.  

From quickly glancing at the minimum and maximum values of the variables, it can be seen that 'Iris Setosa' is the 
smallest of the three species, whereas with 'Iris Virginica' there seems to be a large variation in how large the plant (flower) can be.

Further progressing from the above conclusions, we want to see whether a visual representation of the data can indicate 
to the layperson distinguishing features of the three species.




<b>Sepal Relationship</b>

<img src="Data Visualisation/sepal_length_width.png" alt="Iris Setosa">

From looking at the scatterplot in the 'Data Visualisation' folder (sepal_length_width.png) we can determine
the following:
'Iris Setosa' has larger sepal widths but smaller sepal lengths
'Iris Virginica' has larger sepal lengths but smaller sepal widths
'Iris Versicolor' is somewhere inbetween the two species in terms of sepal length and width.

<b>Petal Relationship</b>

<img src="Data Visualisation/petal_length_width.png" alt="Iris Setosa">

From looking at the scatterplot in the 'Data Visualisation' folder (petal_length_width.png) we can determine
the following: 
'Iris Setosa' has smaller petal lengths and widths than the other two species
'Iris Virginica' has the largest petal lengths and widths of all three species
'Iris Versicolor' is once again inbetween the two species in terms of petal lengths and widths


<b>Sepal and Petal Relationships</b>

From looking at the petal vs sepal length (petal_sepal_length.png) and petal vs sepal width (petal_sepal_width.png)
we can see that 'Iris Setosa' is the smallest of the three species and 'Iris Virginica' is the largest, with 'Iris Versicolor' being somewhere inbetween the two in terms of size.
In my opinion, I feel that the above two plots are most important to the layperson or someone (like myself) who knows
nothing about flowers.
You could show anyone the two plots and ask "Which is the smallest?" and "Which is the largest?" and more than likely they would point to 'Iris Setosa' and 'Iris Virginica' respectively.
I believe that, so far, meaning has been extracted from a file, that when opened, just shows numbers and text (iris2.csv)

<b>Pair Plots</b>

<img src="Data Visualisation/pair_plots.png" alt="Iris Setosa">

'pair_plots.png' is a scatter plot of all pairs of attributes.
If I could only present one plot to my audience, it would be this one, as we can see that petal length and width are highly correlated. In addition, it's clear that no matter what variable is examined, 'Iris Setosa' is clearly apart from the other two species as it has the smallest petal lengths and widths. 'Iris Setosa' also has the smallest sepal 
lengths but wider sepal widths than the other two species.

<b>Potential Limitations</b>
Although the pair plots work well for a data set of this size (150), it's clear that they might not work so well for very large data set sizes for rows that number in the thousands or tens of thousands.


## References

**[Maths is fun](https://www.mathsisfun.com/data/standard-deviation.html)**  
**[Statistics and Standard Deviation](https://www.statisticshowto.com/probability-and-statistics/standard-deviation/)**  
**[Choosing the right visualisation techniques for extracting data insights](https://medium.com/analytics-vidhya/choosing-the-right-visualization-techniques-for-extracting-data-insights-34466c9f26e4)**  
**[Pandas describe() method](https://www.w3schools.com/python/pandas/ref_df_describe.asp#:~:text=The%20describe()%20method%20returns,The%20average%20(mean)%20value.)**  
