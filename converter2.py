# The purpose of this file is to convert the .data files to csv format so that they can be 
# worked on. 
# source: https://stackoverflow.com/questions/31797013/how-to-open-a-data-file-extension
# source: https://datascience.stackexchange.com/questions/97633/convert-data-file-to-csv
# Author: Fabio Fabrizi

# Import pandas so that we can convert file
import pandas as pd


# Read the data file from the website itself
# NB The headers (attributes) are specified on the web page itself
# https://archive.ics.uci.edu/ml/datasets/Iris

def convert_data():

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    iris=pd.read_csv(url, header=None,names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
    #iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None,names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
    # This is where the conversion happens
    #iris.to_csv('iris2.csv', index = None)
    conversion = iris.to_csv('iris2.csv', index=None)
    #iris.to_csv('pands-project/iris2.csv', index = None)
    #type(iris)
    print("Data set converted from data to csv format")
    return conversion