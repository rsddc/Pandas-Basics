# Store Brics countries information:-
# (Name,Capital,Area,population)
# Dataset in tabular form
# 1.Multidimensional Array but very complex to handle
# 2.Numpy but it store only sing type of data etc.only ints etc.
# 3.For small volume of data store it in dictionary use Pandas.
# 4.Pandas are used to store the data in tabular form,called DataFrame

dict={}

dict={
	 'country': ['Brazil', 'Russia', 'India', 'Chaina', 'SA'],
     'capital': ['Brasilia', 'Moscow', 'Delhi', 'Beijing', 'Pretoria'],
     'area': [8.516, 17.1, 3.286, 9.597, 1.221],
     'population': [200.4, 143.5, 1252.0, 1357.0, 52.98]
	 
	 }
	 
import pandas as pd
brics=pd.DataFrame(dict)
print(brics)

# output:-

  # country   capital    area  population
# 0  Brazil  Brasilia   8.516      200.40
# 1  Russia    Moscow  17.100      143.50
# 2   India     Delhi   3.286     1252.00
# 3  Chaina   Beijing   9.597     1357.00
# 4      SA  Pretoria   1.221       52.98

#Pandas module assign each row mathematically we can it short name

brics.index=['BR','RU','IN','CH','SA']
print('========================================')
print(brics)


#output:-

  # country   capital    area  population
# BR  Brazil  Brasilia   8.516      200.40
# RU  Russia    Moscow  17.100      143.50
# IN   India     Delhi   3.286     1252.00
# CH  Chaina   Beijing   9.597     1357.00
# SA      SA  Pretoria   1.221       52.98





