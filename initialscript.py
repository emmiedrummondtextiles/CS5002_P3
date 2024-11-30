import sys 
import csv
import json
import pandas as pd
import numpy as np
from pandas import DataFrame, Series 

#doing data visualisation in seperate .py file, this is datat cleaning file, 

#data frame is becoming none?, think it is reading data_dictionary, or there is somereason why it isnt loading, im not going to load externally until i understand why

print("Hello World!")

#putting this in one function to call later on, instead of calling files at the start which was causing issues/ regognising file as empty

def load_data(csv_path, json_path):
    df = pd.read_csv(csv_path)
    with open(json_path, 'r') as file:
        data_dict = json.load(file)
    df = df.infer_objects()
    return df, data_dict #https://www.analyticsvidhya.com/blog/2024/05/automate-data-cleaning-in-python/ 
#infer objects already checks data types so data_types_check is not neccesary, i will use that to load the json types

#https://stackoverflow.com/questions/20199126/reading-json-from-a-file
#https://www.analyticsvidhya.com/blog/2024/05/automate-data-cleaning-in-python/

#Combining duplicates, admissable and missing values into one function as I was having issues with calling them all at the end, duplicates was turning the data set into null.

def duplicate_admissable__missing_check(df, data_dict):
    df = df.drop_duplicates() 
    print(f"Removed {len(df)} duplicate rows.") # print so i can see if it works in terminal

#check if variables are admissable (e.g. are within a given range or are from the list of admissible values)

#find a simpler, or inbuild way to do this, not runnning; use nan?

   for column, admissable in data_dict.items(): # Changes range_or_list to just refer to data_dict, to directly load what is admissible
        if column in df.columns:
            try:
                if isinstance(admissable, tuple):
                    min_val, max_val = admissable
                    df[column] = df[column].between(min_val, max_val, inclusive='both').replace({False: np.nan}) #https://stackoverflow.com/questions/29247712/how-to-replace-a-value-in-pandas-with-nan
                    print(f"Column '{column}' values checked within range ({min_val}, {max_val})")
                elif isinstance(admissable, list):
                    df[column] = df[column].where(df[column].isin(admissable), np.nan)
                    print(f"Column '{column}' values checked against admissible list.")
            except ValueError as error:
                print(f"Error checking columns for admissible values: {error}")
#missing values, replace with nan

    df.replace('', np.nan) #from #https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
    nan_values = df[df.isna().any(axis=1)]
    missing_summary = df.isna().sum()
    columns_with_missing_value = [] #null, caused issues with converting data set to none, will have to revamp
    for column, missing_count in missing_summary.items():
        if missing_count  > 0: 
            columns_with_missing_value.append((column, missing_count))

    return df

#https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dataframe/
#https://www.slingacademy.com/article/exploring-pandas-dataframe-isin-method/
#https://blog.finxter.com/5-best-ways-to-check-if-values-fall-within-intervals-using-pythons-pandas/
#https://stackoverflow.com/questions/40156469/how-to-check-if-any-value-of-a-column-is-in-a-range-in-between-two-values-in-p
#https://stackoverflow.com/questions/13921707/check-if-numbers-are-in-a-certain-range-in-python-with-a-loop
#https://www.w3resource.com/python-exercises/python-functions-exercise-6.php
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
 #https://stackoverflow.com/questions/14657241/how-do-i-get-a-list-of-all-the-duplicate-items-using-pandas-in-python
 #https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
#https://stackoverflow.com/questions/27159189/find-empty-or-nan-entry-in-pandas-dataframe

 #save the refined data to then check data types after the duplicates, admissable and missing values have been dealt with 


#check  the expected types from the json before checking data types in the csvs

def check_data_types(df):
    data_types = df.dtypes
    print("Data types of each variable:")
    print(data_types)
    return df

#using infer.objects inbuild instead, more automated as said in brief

        #https://realpython.com/python-data-cleaning-numpy-pandas/
        #https://blog.finxter.com/5-best-ways-to-convert-data-types-in-a-pandas-dataframe-with-python/

# took away lambda as it wasnt running/ used nan instead
def mapping_values(df, data_dict):
    for column, mapping in data_dict.items():
        if column in df.columns:
            df[column] = df[column].map(mapping).fillna(np.nan)
            print(f"Validated values in column '{column}'.")
    return df

#https://datagy.io/pandas-map-apply/
#https://www.geeksforgeeks.org/using-dictionary-to-remap-values-in-pandas-dataframe-columns

#call everything into one funciton to convert, I will do admissable later as Im stuck

def clean_data(): #instead of calling I  will fulfil the paths here, made it simpler by handling fewer functions
    csv_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\Scotland_teaching_file_1PCT.csv"
    json_path = "data/data_dictionary.json"
    output_path = "data/refined_Scotland_teaching_file_1PCT.csv"

#replace data_dictionary with json path for printing

    df, data_dict = load_data(csv_path, json_path)
    df = duplicate_admissable__missing_check(df, data_dict)
    df = mapping_values(df, data_dict)
    df = check_data_types(df)


    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to '{output_path}'.")


if __name__ == "__main__":
    clean_data()



#print cleaned file, to convert back into a csv, debating on using sys but will see


#df.to_csv(output_file, index=False)
    #print(f"Cleaned data saved to '{output_file}'.")

    #print(to_keep)

#print(sys.argv)


#https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf



#https://www.w3schools.com/python/pandas/pandas_cleaning.asp





#def columns

#def rows


#df = pd.DataFrame(np.array([[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, 0], [4, 5, 6, 1], [1, 2, 3, 1]]),
                      #columns=['a', 'b', 'c', 'result'])
             #https://stackoverflow.com/questions/61909261/how-can-we-detect-inconsistency-in-pandas-dataframe
             #https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf



# 
#  # this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);