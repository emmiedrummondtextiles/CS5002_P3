# CS5002_P3

READ ME FILE_Next, create a new directory containing a plain
 text file called README.txt or README.md where you will later add basic details about your project



CS5002_P3 - "Teaching in Scotland" Pandas Data Analysis Project

This project uses pandas and matplotlib to analyse and visualise a teaching scotland file. This is meant to analyse the population by demographic. The requirements are to clean the dataset, produce descriptive statistics, and create visual representations of various demographics, specificaly age, occupation, health status, and ethnic groups. 

Features

This project involves loading and processing data from a data CSV file and a JSON dictionary, mapping numerical codes to demographhic types, and identifying/removing duplicate records from the dataset. It also performs descriptive analysis to summarise dataset features and creates bargraph/piechart visualisations, which are adjustable based on your type list.

Project Structure- Directory
Folders.

CODE:

data_cleaning.py: Handles data cleaning tasks, including loading the dataset, mapping categorical attributes, and removing duplicates.

visualisations.py: visualiSES the dataset USING MATPLOTLIB.

NOTEBOOKS:

data_analysis_notebook.ipynb: A Jupyter Notebook used for interactive analysis of the dataset, showing functionality of the programmes.

DATA:

Scotland_teaching_file_1PCT.csv: Contains raw data on teaching in Scotland.

data_dictionary.json: Provides mappings of numerical values to categorical labels for different attributes.

refined_Scotland_teaching_file_1PCT.csv: The cleaned and processed version of the raw dataset.

Requirements:

Must installl pandas, sys, matplotlib, numpy, OS and json

Run pip install pandas sys matplotlib numpy OS json

How to Run

First clean the required CSV using sata_cleaning.py, then use visualisations by inputting the refined version from the data folder.

The viusalisation folder produces two bar graphs and two pie graphs, which the user can alter based on the type names based in your own csv file manually.


