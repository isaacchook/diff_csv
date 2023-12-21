#load module
import pandas as pd

#load the file 
file1 = 'Oct.csv'
file2 = 'Nov.csv'

#declare datafames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

#compare them
compare_csv = df1.compare(df2)
compare_csv.rename(columns={'self': 'Oct', 'other': 'Nov'}, inplace=True)
print(compare_csv)