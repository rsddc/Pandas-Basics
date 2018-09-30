#Using Brics_csv.py to get csv DataFrame for selective analysis

import pandas as pd

# Read entire Dataframe as tabular format with the help of pandas
brics = pd.read_csv("C:\\pycode\\Pandas_module\\brics.csv",index_col=0)

#show only country
print(brics['country'])
# =============================================================================
# output:-
# 
# BR           Brazil
# RU           Russia
# IN            India
# CH            China
# SA     South Africa
# Name: country, dtype: object
# 
# Here we print type(brics['country']), will get <class 'pandas.core.series.Series'>.
# 
# Meaning pandas series is a 1D Array that we can label as Data FrameFrame. 
# =============================================================================
print(type(brics['country']))

#Toget data frame use [[]] Double square bracket.

print(brics[['country']])
print(type(brics[['country']]))#<class 'pandas.core.frame.DataFrame'>
# =============================================================================
# output:-
#           country
# BR         Brazil
# RU         Russia
# IN          India
# CH          China
# SA   South Africa
# <class 'pandas.core.frame.DataFrame'>
# =============================================================================

#To get Data from 2 data frames
print(brics[['country','capital','area']])

# =============================================================================
# output:-
#           country    capital    area
# BR         Brazil   Brasilia   8.516
# RU         Russia     Moscow  17.100
# IN          India  New Delhi   3.286
# CH          China    Beijing   9.597
# SA   South Africa   Pretoria   1.221
# =============================================================================
print(brics[1:3])# for rows use same slicing lower included and upper excluded