import pandas as pd
import numpy as np
import csv
import json
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

#https://www.geeksforgeeks.org/how-to-plot-bar-graph-in-python-using-csv-file
#https://blog.finxter.com/5-effective-ways-to-visualize-csv-data-with-matplotlib-in-python/
#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
#https://www.slingacademy.com/article/pandas-understanding-dataframe-map-method-5-examples/

csv_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\refined_Scotland_teaching_file_1PCT.csv" 
df = pd.read_csv(csv_path)

print("Column names in CSV:", df.columns) #checking if the columns have succesfully loaded

json_path = r"C:\Users\Emmie\OneDrive - University of St Andrews\CS5002_P3\data\data_dictionary.json"
with open(json_path, 'r') as file:
    data_dict = json.load(file)

if "age" not in df.columns:
    print("Error: 'Age' column not found in the dataset.")

if "Occupation" not in df.columns:
    print("Error: 'Occupation' column not found in CSV")

if "age" in df.columns and "Occupation" in df.columns:
    age_mapping = {int(k): v for k, v in data_dict["Age"].items()} #https://stackoverflow.com/questions/44390818/how-to-insert-key-value-pair-into-dictionary-at-a-specified-position
    df["Age_Group"] = df["age"].map(age_mapping)  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    df["Occupation_Group"] = df["Occupation"].map(data_dict["Occupation"])
    
    if "health" in df.columns:
        health_mapping = {int(k): v for k, v in data_dict["Health(General Health)"].items()}
        df["Health_Status"] = df["health"].map(health_mapping)
    else:
        print("Error: 'health' column not found in the dataset.")
    
    if "Ethnic_Group" in df.columns:
        ethnic_mapping = {str(k): v for k, v in data_dict.get("Ethnic_Group", {}).items()}
        if not df["Ethnic_Group"].isna().all():
            df["Ethnic_Group_Label"] = df["Ethnic_Group"].map(ethnic_mapping)
        else:
            print("Error: No valid ethnic group mappings found.")
    else:
        print("Error: 'Ethnic_Group' column not found in the dataset.")
else:
    print("Error: 'Age' or 'Occupation' column not found in the dataset.")

    #ethnicity was not working because i didnt put it in the data_dict

# https://note.nkmk.me/en/python-pandas-value-counts/

def print_bar_age():  # Using https://www.geeksforgeeks.org/how-to-plot-bar-graph-in-python-using-csv-file tutorial
    age_counts = df["Age_Group"].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.bar(age_counts.index, age_counts.values, color='skyblue')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Records')
    plt.title('Number of Records for Each Age Group')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def print_bar_occupation():
    occupation_counts = df["Occupation_Group"].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.bar(occupation_counts.index, occupation_counts.values, color='salmon')
    plt.xlabel('Occupation')
    plt.ylabel('Number of Records')
    plt.title('Number of Records for Each Occupation')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def print_pie_health():
    if "Health_Status" in df.columns:
        health_counts = df["Health_Status"].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(health_counts.values, labels=health_counts.index, autopct='%1.1f%%')
        plt.title('Percentage of Records for Each General Health Descriptor')
        plt.tight_layout()
        plt.show()
    else:
        print("Error: 'Health_Status' column not found in the dataset.")

def print_pie_ethnic_group(): #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
    if "Ethnic_Group_Label" in df.columns:
        ethnic_counts = df["Ethnic_Group_Label"].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(ethnic_counts.values, labels=ethnic_counts.index, autopct='%1.1f%%')
        plt.title('Percentage of Records for Each Ethnic Group')
        plt.tight_layout()
        plt.show()
    else:
        print("Error: 'Ethnic_Group_Label' column not found in the dataset.")

def generate_graphs():
    if "Age_Group" in df.columns and "Occupation_Group" in df.columns:
        print_bar_age()
        print_bar_occupation()
        print_pie_health()
        print_pie_ethnic_group()
    else:
        print("Error: Unable to generate graphs due to missing data")


    #easy requirement 2, based on https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

hours_industry_group = df.groupby(['Hours_Worked_Per_Week', 'industry']).size().reset_index(name='Record_Count')
print("Number of records by hours worked per week and industry:")
print(hours_industry_group)

occupation_social_grade_group = df.groupby(['Occupation', 'Approximate_Social_Grade']).size().reset_index(name='Record_Count')
print("\nnumber of records by occupation/approximate social grade:")
print(occupation_social_grade_group)

if __name__ == "__main__":
    generate_graphs()
