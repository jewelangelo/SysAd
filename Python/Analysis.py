import numpy as np
import pandas as pd
import matplotlib
import plotly


xls = pd.ExcelFile ('pathtofile.xlsx') #to read the specific Sheet in the excel file
cols = [0, 2, 3, 7] #define columns needed for analysis column A is 0
df = pd.read_excel (xls, 'Clean', usecols=cols) #to read the specific Sheet in the excel file
long_df = df.groupby('Name')['Shift'].value_counts().reset_index(name="count")
