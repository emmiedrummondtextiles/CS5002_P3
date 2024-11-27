
import pandas as pd
import numpy as np
import matplotlib
print("Hello World!")

#https://blog.devgenius.io/5-essential-data-quality-checks-you-can-perform-with-python-18fc87655950

df = pd.read_csv('Scotland_teaching_file_1PCT.csv')
#missing_values = df.isnull().sum()
print(df)

#duplicate_rows = df[df.duplicated()]
#print(duplicate_rows)

#df.drop_duplicates(inplace=True)


#df = pd.DataFrame(np.array([[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, 0], [4, 5, 6, 1], [1, 2, 3, 1]]),
                      #columns=['a', 'b', 'c', 'result'])
             #https://stackoverflow.com/questions/61909261/how-can-we-detect-inconsistency-in-pandas-dataframe
             #https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf

#to_keep = df[df.groupby(['a', 'b', 'c'])['result'].transform('nunique') == 1] #duplicates

#print(to_keep)
