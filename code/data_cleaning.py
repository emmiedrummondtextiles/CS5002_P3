import sys 
import csv
import json
import pandas as pd
import numpy as np
from pandas import DataFrame, Series 

print("Hello World!") 

#json file = data_dict
#

def load_data(csv_path, json_path):
    df = pd.read_csv(csv_path) #creating the initial dataframe
    with open(json_path, 'r') as file:
        data_dict = json.load(file)
    df = df.infer_objects()
    return df, data_dict 


def remove_duplicates_and_check_missing(df):

    df.replace('', np.nan, inplace=True) ##https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
#replacing missing values with NAN

    df = df.drop_duplicates()  #https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/
    print(f"Removed {len(df)} duplicate rows.") 

#missing values

    missing_summary = df.isna().sum()  #https://stackoverflow.com/questions/26266362/how-do-i-count-the-nan-values-in-a-column-in-pandas-dataframe
    for column, missing_count in missing_summary.items():
        if missing_count > 0:
            print(f"Column '{column}' has {missing_count} missing values.")
    
    return df


#must check if  the values of variables are of the expected format (numbers, strings, etc.);, check if infer.objects does this properly, need print statement
#infer doesnt check if the values coallign with the json dictionary, edit admissable to directly corralate this

#pandas merge funciton, use loops, create data frame with merge funciton, 
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

#I forgot to directly link the data_dictionary and the csv file together, merging them would be the best approach as i researched previously

#putting mapping and invalid types in the same funciton.


def admissable_invalid_merge(df, data_dict):
     value_nan = [] #finding the number of invalid entries, that were replaced by nan.

     for column, admissable in data_dict.items():
        if column in df.columns: #loop over data_dict (mappings to the json file)
        
            admissable_df = pd.DataFrame({column: list(admissable.keys())})  #list of valid keys from the cvs file, new data_frame

#https://stackoverflow.com/questions/23940181/pandas-merging-with-missing-values
#https://stackoverflow.com/questions/46386402/how-to-properly-understand-pandas-dataframe-merge-how-left-on-right-on

            merged_df = df[[column]].merge(admissable_df, on=column, how='left', indicator=True) #merging to find invalid values
            invalid_rows = merged_df[merged_df['_merge'] == 'left_only'].index

#https://dnmtechs.com/replacing-invalid-values-with-none-in-pandas-dataframe-in-python-3/
            
            if len(invalid_rows) > 0: #relacing the invalid rows with nan
                df.loc[invalid_rows, column] = np.nan
                value_nan.append(f"Column '{column}' has {len(invalid_rows)} invalid entries replaced with NAN")

                #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

            for issue in value_nan:
                print(issue) 

            return df
        
#took out keys, mapping the numbers to labels

#https://datagy.io/pandas-map-apply/
#https://www.geeksforgeeks.org/using-dictionary-to-remap-values-in-pandas-dataframe-columns

#call everything into one funciton to convert, I will do admissable later as Im stuck

# perform the descriptive analysis of the dataset:– determine the total number of records in the dataset;– determine the type of each variable in the dataset;– for each variable except “Record_Number” and “Region”, find all different values that
 #it takes, and the number of occurrences for each value,

# was oriinally going to put decriptive analyis in the visualisation file, but decided to keep analysis in one file.



def clean_data():
    # Specified paths for the dataset and data dictionary
    csv_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\Scotland_teaching_file_1PCT.csv"
    json_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\data_dictionary.json"
    output_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\refined_Scotland_teaching_file_1PCT.csv"

    df, data_dict = load_data(csv_path, json_path)


    df = admissable_invalid_merge(df, data_dict)
    df = remove_duplicates_and_check_missing(df)

    df.to_csv(output_path)
    print(f"\nc2`leaned data saved to '{output_path}'.")




if __name__ == "__main__":
    clean_data()

#def clean_data(): #instead of calling I  will fulfil the paths here, made it simpler by handling fewer functions
 #   csv_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\Scotland_teaching_file_1PCT.csv"
  #  json_path = "data/data_dictionary.json"
   # output_path = "data/refined_Scotland_teaching_file_1PCT.csv"

#replace data_dictionary with json path for printing , removed the check as it was regognising it as an unbound local error
    #df, data_dict = load_data(csv_path, json_path)
    #df = duplicate_admissable__missing_check(df, data_dict)
    #df = mapping_values(df, data_dict)


    #df.to_csv(output_path, index=False)
    #print(f"Cleaned data saved to '{output_path}'.")


#if __name__ == "__main__":
 #   clean_data()


#print cleaned file, to convert back into a csv, debating on using sys but will see


#df.to_csv(output_file, index=False)
    #print(f"Cleaned data saved to '{output_file}'.")

    #print(to_keep)

#print(sys.argv)


#https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf



#https://www.w3schools.com/python/pandas/pandas_cleaning.asp

