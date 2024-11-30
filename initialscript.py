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

#https://stackoverflow.com/questions/20199126/reading-json-from-a-file
#https://www.analyticsvidhya.com/blog/2024/05/automate-data-cleaning-in-python/

#Combining duplicates, admissable and missing values into one function as I was having issues with calling them all at the end, duplicates was turning the data set into null.

def duplicate_admissable__missing_check(df, data_dict):
    df = df.drop_duplicates() 
    print(f"Removed {len(df)} duplicate rows.") # print so i can see if it works in terminal

#check if variables are admissable (e.g. are within a given range or are from the list of admissible values)


    for column, admissable in data_dict.items(): #changes range_or_list to just refer to data_dict, to directly load what is admissable
        if column in df.columns:
            try:
                if isinstance(admissable):
                    min_val, max_val = admissable
                df[column]=df[column].apply(lambda row: min_val<= row <= max_val)
                print(f"Column  {column} values to be checked within range") #remove admissable aswell as duplicates?, find source
                elif isinstance(admissable, list):   #put list aswell as range
                df[column]=df[column].apply()
                except ValueError as error:
            print(f"error checking columns for admissable values") #do list as a value error?

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



#check  the expected types from the json before checking data types in the csv?





def check_data_types(df, expected_types): # figure out if you still need this
    for column, expected_type in expected_types.items():
        try:
            df[column] = df[column].astype(expected_type)
            print(f"Column '{column} converted to {expected_type}.") #check if need to define integer and list, before or after?
        except ValueError as error:
            print(f"Error converting column to expected type")
        return df
        
        #https://realpython.com/python-data-cleaning-numpy-pandas/
        #https://blog.finxter.com/5-best-ways-to-convert-data-types-in-a-pandas-dataframe-with-python/

#mapping values using loop, come first or after data cleaning?

def mapping_values(df, data_dict):
    for column, mapping in data_dict.items():
        if column in df.columns:
            valid_values = list(mapping.keys())
            df[column] = df[column].apply(lambda x: x if str(x) in valid_values else np.nan) #https://stackoverflow.com/questions/44061607/pandas-lambda-function-with-nan-support
            print(f"Validated values in column '{column}'.")
    return df #put this in duplicates?

#https://datagy.io/pandas-map-apply/
#https://www.geeksforgeeks.org/using-dictionary-to-remap-values-in-pandas-dataframe-columns

#call everything into one funciton to convert, I will do admissable later as Im stuck

def clean_data(): #instead of calling I  will fulfil the paths here
    csv_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\Scotland_teaching_file_1PCT.csv"
    json_path = "data/data_dictionary.json"
    output_path = "data/refined_Scotland_teaching_file_1PCT.csv"

#replace data_dictionary with json path for printing


    df = df
    df = mapping_values(df, data_dictionary)
    df, columns_with_missing_value, nan_values = missing_value_check(df)
    expected_types = get_expected_types_from_data_dictionary(df) #define this
    df = check_data_types(df, expected_types)
    df, duplicate_rows = duplicate_check(df)
    return {
        "corrected_columns": expected_types.keys(),
        "duplicate_rows": duplicate_rows,
        "columns_with_missing": columns_with_missing_value,
        "nan_values": nan_values,
        "output_file": output_file
    }
if __name__ == "__main__":
    input_file = 'data/Scotland_teaching_file_1PCT.csv'
    output_file = 'data/Scotland_teaching_file_1PCT_cleaned.csv'
    result_summary = clean_data(input_file, output_file)
    print(result_summary)


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