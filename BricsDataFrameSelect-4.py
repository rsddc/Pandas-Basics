#Some advance data select from DataFrame are loc and iloc.loc is based upon
#labled location.means Russia information etc.using the same csv and converting in dataframe

import pandas as pd
brics = pd.read_csv('C:\\pycode\\Pandas_module\\brics.csv',index_col=0)
#need information of russia.So label is Russia and use loc function.
russia_info = brics.loc[["RU"]]#[[]] same like basic select part-3
print(russia_info)
#output:-
#   country capital  area  population
#RU  Russia  Moscow  17.1       143.5
print('==========================================')
combined=brics.loc[["RU","IN"]]
print(combined)
print('==========================================')
combined=brics.loc[["RU","IN"],['country','capital']]#intersection of 2 countries with 2 labels
print(combined)
print('==========================================')
combined=brics.loc[:,['country','capital']]#intersection of all rows with 2 labels
print(combined)
print('==========================================')
#for iloc use index instead of label. iloc and loc are the same. difference is of
#index and lable using all above example for iloc

iloc_russia_info=brics.iloc[[1]]
print(iloc_russia_info)

print('==========================================')
iloc_combined=brics.iloc[[1,2],[0,1]]
print(iloc_combined)

print('==========================================')
iloc_combined=brics.iloc[:,[0,1]]
print(iloc_combined)