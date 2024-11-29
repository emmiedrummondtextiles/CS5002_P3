import sys 
import csv
import json
import pandas as pd
import numpy as np
from pandas import DataFrame, Series 

#doing data visualisation in seperate .py file, this is datat cleaning file

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
        
        #https://realpython.com/python-data-cleaning-numpy-pandas/
        #https://blog.finxter.com/5-best-ways-to-convert-data-types-in-a-pandas-dataframe-with-python/
        # checked the data types based off of these tutorials, by column for each population segment

#do we want to print or append?
#check if variables are admissable (e.g. are within a given range or are from the list of admissible values)

def range_or_list(df, range_or_list_values):
    for column, admissable in range_or_list_values.items():
        try:
           if isinstance(admissable):
               min_val, max_val = admissable
               df[column]=df[column].apply(lambda row: min_val<= row <= max_val) 
               print(f"Column  {column} values to be checked within range")

           elif isinstance(admissable, list):   #put list aswell as range

            df[column]=df[column].apply()

        except ValueError as error:
            print(f"error checking columns for admissable values") #do list as a value error?
            return df

#https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dataframe/

#myfun = lambda row: row['b']<=row['a']<=row['c'], between max val and minimum val

    #df = df[column].apply(lambda row: min_val<= row[] max_val) #axis? 
    
#df1['Result'] = df1.apply(myfun, axis=1)
#display(df1)

    #elifisinstance
#https://www.slingacademy.com/article/exploring-pandas-dataframe-isin-method/
#https://blog.finxter.com/5-best-ways-to-check-if-values-fall-within-intervals-using-pythons-pandas/
#https://stackoverflow.com/questions/40156469/how-to-check-if-any-value-of-a-column-is-in-a-range-in-between-two-values-in-p
#https://stackoverflow.com/questions/13921707/check-if-numbers-are-in-a-certain-range-in-python-with-a-loop
#https://www.w3resource.com/python-exercises/python-functions-exercise-6.php

#handling duplicates

def duplicate_check(df):
    duplicate_rows= df[df.duplicated()]
    if not duplicate_rows.empty:
        df.drop_duplicates()
        return df, duplicate_rows

    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
    #https://stackoverflow.com/questions/14657241/how-do-i-get-a-list-of-all-the-duplicate-items-using-pandas-in-python


#print cleaned file, to convert back into a csv
#df.to_csv(output_file, index=False)
    #print(f"Cleaned data saved to '{output_file}'.")


#https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf



#https://www.w3schools.com/python/pandas/pandas_cleaning.asp





#def columns

#def rows


#df = pd.DataFrame(np.array([[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, 0], [4, 5, 6, 1], [1, 2, 3, 1]]),
                      #columns=['a', 'b', 'c', 'result'])
             #https://stackoverflow.com/questions/61909261/how-can-we-detect-inconsistency-in-pandas-dataframe
             #https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf



#print(to_keep)

#print(sys.argv)
# 
#  # this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);