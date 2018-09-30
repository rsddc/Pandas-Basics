#The DataFrame is one of Pandas' most important data structures. 
#It's basically a way to store tabular data where you can label the rows 
#and the columns. One way to build a DataFrame is from a dictionary.
#Data volume will be huge so in real time use CSV files to read data 
#with the help of pandas. Same tabular information inBrics_country.py
#Now read through CSV.


#import csv
#with open('C:\\pycode\\Pandas_module\\Brics.csv') as f:
#    r = csv.reader(f)
#    for row in r:
#        print(row)

# 2. Best is to use Pandas.No need to import CSV. pandas inbuilt data-structures
#internally deals with csv by read_csv function. Use either above code or this one:-

import pandas as pd
#read = pd.read_csv('C:\\pycode\\Pandas_module\\Brics.csv') #Here
#Just a minor modification:- It gives one addtional unmaned column heading remove it by
read=pd.read_csv('C:\\pycode\\Pandas_module\\Brics.csv',index_col=0)

print(read)

#Just a minor modification:- It gives one addtional unmaned column heading remove it by
#read=pd.read_csv('C:\\pycode\\Pandas_module\\Brics.csv',index_col=0)

		