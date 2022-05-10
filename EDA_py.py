import pandas as pd 
from pandas_profiling import ProfileReport

df = pd.read_csv('Excel for Analytics Project Series Source File - Copy.csv')
profile = ProfileReport(df,title='EDA')
profile.to_file('EDA.html')
