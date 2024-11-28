import sys 
import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pandas import DataFrame, Series 

print("Hello World!")

#first step:  the values of variables are of the expected format (numbers, strings, etc.)
# the values of variables are admissible (e.g. are within a given range or are from the list of admissible values)
#in case of any inconsistencies and/or duplicates found, produce new file with refined data to be used in the subsequent analysis;

def load_df(file_path):
    return pd.read_csv("data/Scotland_teaching_file_1PCT.csv")  

#check data types before duplicates

def check_data_types(df, expected_types):
    for column, expected_type in expected_types.items():
        try:
            df[column] = df[column].astype(expected_type)
            print(f"Column '{column} converted to {expected_type}.")
        except ValueError as error:
            print(f"Error converting column to expected tyoe")
            return df

#
# 
# df_duplicates= df.drop_duplicates(inplace=True) 


#with open(r"data\data_dictionary.json", "r") as jsonfile: #forgot r
    #data_dictionary = json.load(jsonfile)

#https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf

#print("Missing values:\n", data.isnull().sum())

#to_keep = df[df.groupby(['a', 'b', 'c'])['result'].transform('nunique') == 1] #duplicates
#duplicate_rows = df[df.duplicated()]
#print(duplicate_rows)
#df.drop_duplicates(inplace=True)

#https://www.w3schools.com/python/pandas/pandas_cleaning.asp


#associate directly to data dictionary?, 

#assert data_cleaned["Age"].between(0,120).all(),"out of range" #object is not scriptable, Age

#for columns in  df:  #convert csv to string? 



#def columns

#def rows


#df = pd.DataFrame(np.array([[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, 0], [4, 5, 6, 1], [1, 2, 3, 1]]),
                      #columns=['a', 'b', 'c', 'result'])
             #https://stackoverflow.com/questions/61909261/how-can-we-detect-inconsistency-in-pandas-dataframe
             #https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf



#print(to_keep)

#print(sys.argv) # this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);