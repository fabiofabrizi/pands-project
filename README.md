# pands-project



<div align="center">
    <h3 align="center">pands-project</h3>
    <p align="center">This is the repo for the programming and scripting module project - The Iris Dataset</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li>
        <a href="#getting-started">Getting Started</a></li>
      </ul>
    </li>
    <li>
      <a href="#Why">Why</a>
      <ul>
        <li><a href="#Background">Background</a></li>
        <li><a href="#installation">Research</a></li>
      </ul>
    </li>
    <li><a href="#Preliminary Findings">Preliminary Findings</a></li>
    <li><a href="#Files">Files</a></li>
    <li><a href="#Conclusions">Conclusions</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

This is the project for the Programming and Scripting module - Higher Diploma in Data Analytics.
Fisher's Iris Data set is to be researched, and documentation (my opinions) and code (Python) must be produced.


## Getting Started

I started by creating the Github repository 'pands-project' and added the data set to it converted from a data file.
The script for conversion is included. As I've delved deeper into the project, the repository has increased in size.

## Why

The task, as I understand it, is to take some data - in this case, about Irises
and interpret it in such a way that:
1) I learn why the data is collected in the first place
2) I can then explain to others, whether they have an interest (or not) how to 
identify what type of Iris they have.

## Background
I have no background in horticulture - the furthest my expertise extends to is mowing the grass and a small herb garden.
However, from looking at the many blogs/articles written on Fisher's Iris data set, the common theme amongst all of them is:
[1] A dataset
[2] Python script(s) to analyse that dataset in order to make sense of the data and/or identify any patterns.

## Research

The various sources/sites/etc that I found and used are listed below.

[1] The Mother
I have no background in horticulture - the furthest my expertise extends to is mowing the grass and a small herb garden.
However, my mother is a keen gardener, she told me about a scenario that occurs fairly often with her.
1) She wants to find out what type of plant/tree/flower/etc she's come across
2) She takes a picture and some measurements and any other relevant information (acidity of soil, type of shade, etc.)
3) She then emails RHS (Royal Horticultural Society - she lives in the UK)
4) Within a few days, someone has responded with the answer. 

So there's a concrete example of a data set point being checked against the data set (or many) in order to produce an answer.

## Preliminary Findings

From all the various articles (aimed at beginners in this field) that I've come across on this topic, there seems to be a common pattern.
i) Get the dataset
ii) Check the dataset for null values and remove them
iii) Get a 'feeling' for the dataset and associated data - ie How many rows/columns, mean/max/min values etc
iv) Apply some statistical analysis to get a visual representation of the data
v) Examine the visual representation - Does it show a pattern or something unique that we can use to understand the data set.

From the process above, one can take a data set in csv format and apply the above steps to look for any unique patterns in the data.

## Files

There's lots of files - here's an explanation of them
converter2.py
This pulls directly from the main archive at UCI and converts it to a CSV format with headers
The call to the function is commented out because analysis.py calls it.
The file does the task of i) from Preliminary Findings

EDA.py
This is the Exploratory Data Analysis of the Iris Data set. We check for missing values, duplicates, etc
The function is called from analysis.py
This file does the task of ii) and iii) from Preliminary Findings.

analysis.py
This calls the functions from the other files so that only one file needs to be run. I've done it in this way
because I tried to split it up into parts and thought if the project scope changed it would be better for maintenance


dataVis.py
This file performs iv) and v) from Preliminary Findings
We're examining: 
- Sepal length and width of the species and looking for patterns,
- Petal lengtha and width and looking for patterns,


## Conclusions

dataVis.py generates all the visualisations and saves them.
<b>Sepal Relationship</b>
From looking at the scatterplot in the 'Data Visualisation' folder (sepal_length_width.png) we can determine
the following:
'Iris Setosa' has larger sepal widths but smaller sepal lengths
'Iris Virginica' has larger sepal lengths but smaller sepal widths
'Iris Versicolor' is somewhere inbetween the two species in terms of sepal length and width.

<b>Petal Relationship</b>
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
I believe that so far, meaning has been extracted from a file, that when opened, just shows numbers and text (iris2.csv)

<b>Pair Plots</b>
'pair_plots.png' is a scatter plot of all pairs of attributes.
If I could only present one plot to my audience, it would be this one, as we can see that petal length and width are highly correlated. In addition, it's clear that no matter what variable is examined, 'Iris Setosa' is clearly apart from the other two species as it has the smallest petal lengths and widths. 'Iris Setosa' also has the smallest sepal 
lengths but wider sepal widths than the other two species.

<b>Potential Limitations</b>
Although the pair plots work well for a data set of this size (150), it's clear that they might not work so well for very large data set sizes. 