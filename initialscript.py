import sys 
import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pandas import DataFrame, Series 

print("Hello World!")

#four loop on pandas mapping
#pin thing in sys 

#https://blog.devgenius.io/5-essential-data-quality-checks-you-can-perform-with-python-18fc87655950
#https://medium.com/@swaratvaghela30112003/working-with-csv-and-json-in-python-fc88e49c1c1d


#df = pd.read_csv('data\Scotland_teaching_file_1PCT.csv')

df = "data/Scotland_teaching_file_1PCT.csv"
data = pd.read_csv(df)
with open("data\data_dictionary.json", "r") as jsonfile:
    data_dictionary = json.load(jsonfile)

#df = pd.DataFrame(np.array(data_dictionary)),

print("Missing values:\n", data.isnull().sum())

data_cleaned= data.drop_duplicates(inplace=True)
#for columns in  df:  #convert csv to string? 


#def columns

#def rows


#df = pd.DataFrame(np.array([[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, 0], [4, 5, 6, 1], [1, 2, 3, 1]]),
                      #columns=['a', 'b', 'c', 'result'])
             #https://stackoverflow.com/questions/61909261/how-can-we-detect-inconsistency-in-pandas-dataframe
             #https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf

#to_keep = df[df.groupby(['a', 'b', 'c'])['result'].transform('nunique') == 1] #duplicates

#print(to_keep)


#read cvs file
# use data_dictionary as 

#first step:  the values of variables are of the expected format (numbers, strings, etc.)
# the values of variables are admissible (e.g. are within a given range or are from the list of admissible values)

#in case of any inconsistencies and/or duplicates found, produce new file with refined data to be used in the subsequent analysis;

#duplicate_rows = df[df.duplicated()]
#print(duplicate_rows)
#df.drop_duplicates(inplace=True)

#print(sys.argv) # this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);