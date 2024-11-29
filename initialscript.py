import sys 
import csv
import json
import pandas as pd
import numpy as np
from pandas import DataFrame, Series 

#doing data visualisation in seperate .py file, this is datat cleaning file, 

#data frame is becoming none?, think it is reading data_dictionary, or there is somereason why it isnt loading, im not going to load externally until i understand why

print("Hello World!")

df = pd.read_csv(r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\Scotland_teaching_file_1PCT.csv")
#instead of load i should just use df?

##missing_values = ["n/a", "na", "--"]
#df = pd.read_csv("property data.csv", na_values = missing_values) put this up here?

data_dictionary = {
    "RESIDENCE_TYPE": {
        "C": "Resident in a Communal Establishment",
        "P": "Not resident in a Communal Establishment"
    },
    "Family_Composition": {
        "0": "Not in a family",
        "1": "Married/same-sex civil partnership couple family",
        "2": "Cohabiting couple family",
        "3": "Lone parent family (male head)",
        "4": "Lone parent family (female lead)",
        "5": "Other related family",
        "X": "No code required (residents of a communal establishment)"
    },
    "Sex": {
        "1": "Male",
        "2": "Female"
    },

    "Age": {
        "1":"0 to 15",
        "2":"16 to 24",
        "3":"25 to 34",
        "4":"35 to 44",
        "5":"45 to 54",
        "6":"55 to 64",
        "7":"65 to 74",
        "8":"75 and over"
    },
    "Marital_Status":{
        "1":"Single(Never married or never registered a same-sex civil partnership)",
        "2":" Married or in a same sex-civil partnership",
        "3":"Separated, but still legally married or still legally in a same-sex civil partnership",
        "4":"Divorced or formerly in a same-sex civil partnership which is now legally dissolved",
        "5":"Widowed or surviving partner from a same-sex civil partnership"
    },
    "Student (Schoolchild or full-time student)":{
        "1":"Yes",
        "2":"No"
    },
    "Country_Of_Birth":{
        "1":"UK",
        "2":"Non UK"
    },
    "Health(General Health)":{
        "1":"Very Good Health",
        "2":"Good Health",
        "3":"Fair Health",
        "4":"Bad Health",
        "5":"Very Bad Health"
    },
    "Religion":{
        "1":"No Religeon",
        "2":"Christian",
        "3":"Buddhist",
        "4":"Hindu",
        "5":"Jewish",
        "6":"Muslim",
        "7":"Sihk",
        "8":"Other Religeon",
        "9":"Not Stated"
    },
    "Economic_Activity": {
    "1": "Economically active: Employed",
    "2": "Economically active: Self-Employed",
    "3": "Economically active: Unemployed",
    "4": "Economically active: Full-time student",
    "5": "Economically inactive: Retired",
    "6": "Economically inactive: Student",
    "7": "Economically inactive: Looking after home or family",
    "8": "Economically inactive: Long-term sick or disabled",
    "9": "Economically inactive: Other",
    "X": "No code required (Aged under 16)"
},
"Occupation": {
    "1": "Managers, Directors and Senior Officials",
    "2": "Professional Occupations",
    "3": "Associate Professional and Technical Occupations",
    "4": "Administrative and Secretarial Occupations",
    "5": "Skilled Trades Occupations",
    "6": "Caring, Leisure and Other Service Occupations",
    "7": "Sales and Customer Service Occupations",
    "8": "Process, Plant and Machine Operatives",
    "9": "Elementary Occupations",
    "X": "No code required (People aged under 16 and people who have never worked)"
},
"Industry": {
    "1": "Agriculture, forestry and fishing",
    "2": "Mining and quarrying; Manufacturing; Electricity, gas, steam and air conditioning system; Water supply",
    "3": "Construction",
    "4": "Wholesale and retail trade; Repair of motor vehicles and motorcycles",
    "5": "Accommodation and food service activities",
    "6": "Transport and storage; Information and communication",
    "7": "Financial and insurance activities",
    "8": "Real estate activities; Professional scientific and technical activities; Administrative and support service activities",
    "9": "Public administration and defence",
    "10": "Education",
    "11": "Human health and social work activities",
    "12": "Arts; entertainment and recreation",
    "13": "Other",
    "X": "No code required (People aged under 16 and people who have never worked)"
},
"Hours_Worked_Per_Week": {
    "1": "Part-time: 15 or less hours worked",
    "2": "Part-time: 16 to 30 hours worked",
    "3": "Full-time: 31 to 48 hours worked",
    "4": "Full-time 49 or more hours worked",
    "X": "No code required (People aged under 16 and people not working)"
},
"Approximate_Social_Grade": {
    "1": "AB",
    "2": "C1",
    "3": "C2",
    "4": "DE",
    "X": "No code required (People aged under 16 and people resident in communal establishments)"
}

}


#forgot to map between the csv and the data set,



def mapping_values(df, data_dict):
    for column, mapping in data_dict.items():
        if column in df.columns:
            valid_values = list(mapping.keys())
            df[column] = df[column].apply(lambda x: x if str(x) in valid_values else np.nan)
            print(f"Validated values in column '{column}'.")
    return df

#https://stackoverflow.com/questions/20199126/reading-json-from-a-file

#def get_expected_types_from_data_dictionary(df): #refer to df instead
    #df = df.infer_objects()
    #return df.dtypes.to_dict() # found inbuilt to automatically concert data types #https://www.analyticsvidhya.com/blog/2024/05/automate-data-cleaning-in-python/

    #https://www.analyticsvidhya.com/blog/2024/05/automate-data-cleaning-in-python/

#check data types before duplicates

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
        # checked the data types based off of these tutorials, by column for each population segment

#do we want to print or append?
#check if variables are admissable (e.g. are within a given range or are from the list of admissible values)

#def range_or_list(df, range_or_list_values):
   # for column, admissable in range_or_list_values.items():
      #  try:
        #   if isinstance(admissable):
          #     min_val, max_val = admissable
          #     df[column]=df[column].apply(lambda row: min_val<= row <= max_val) 
           #    print(f"Column  {column} values to be checked within range")

         #  elif isinstance(admissable, list):   #put list aswell as range

         #   df[column]=df[column].apply()

     #   except ValueError as error:
      #     print(f"error checking columns for admissable values") #do list as a value error?
       #    return df

#https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dataframe/
#https://www.slingacademy.com/article/exploring-pandas-dataframe-isin-method/
#https://blog.finxter.com/5-best-ways-to-check-if-values-fall-within-intervals-using-pythons-pandas/
#https://stackoverflow.com/questions/40156469/how-to-check-if-any-value-of-a-column-is-in-a-range-in-between-two-values-in-p
#https://stackoverflow.com/questions/13921707/check-if-numbers-are-in-a-certain-range-in-python-with-a-loop
#https://www.w3resource.com/python-exercises/python-functions-exercise-6.php

#handling duplicates


def duplicate_check(df):
    duplicate_rows = df[df.duplicated()]
    df = df.drop_duplicates()
    print(f"Removed {len(duplicate_rows)} duplicate rows.") # print so i can see if it works in terminal
    return df, duplicate_rows

    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
    #https://stackoverflow.com/questions/14657241/how-do-i-get-a-list-of-all-the-duplicate-items-using-pandas-in-python


def missing_value_check(df): # error, load_Df
    df.replace('', np.nan) #from #https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
    nan_values = df[df.isna().any(axis=1)]
    missing_summary = df.isna().sum()
    columns_with_missing_value = []
    for column, missing_count in missing_summary.items():
        if missing_count  > 0: 
            columns_with_missing_value.append((column, missing_count))
    return df, columns_with_missing_value, nan_values
    
#https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
#https://stackoverflow.com/questions/27159189/find-empty-or-nan-entry-in-pandas-dataframe


#call everything into one funciton to convert, I will do admissable later as Im stuck

def clean_data(file_path, output_file):
    df = df
    df = mapping_values(df, data_dictionary)
    df, columns_with_missing_value, nan_values = missing_value_check(df)
    expected_types = get_expected_types_from_data_dictionary(df)
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