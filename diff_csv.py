#load module
import pandas as pd

#load the file 
file1 = 'file1.csv'
file2 = 'file2.csv'

#declare datafames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

#compare them
compare_csv = df1.equals(df2)

#conditional statements
if compare_csv:
    print('They are identical') #expected because file1=file2
else:
    print('They are different')
