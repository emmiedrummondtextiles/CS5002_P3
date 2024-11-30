#matplot lib visulisaitons

import pandas as pd
import matplotlib.pylot as plt

csv_path = "data/refined_Scotland_teaching_file_1PCT.csv"
df = pd.read_csv(csv_path)




# perform the descriptive analysis of the dataset:– determine the total number of records in the dataset;– determine the type of each variable in the dataset;– for each variable except “Record_Number” and “Region”, find all different values that
 #it takes, and the number of occurrences for each value,


#build the following plots:– bar chart for the number of records for each age group;– bar chart for the number of records for each occupation,