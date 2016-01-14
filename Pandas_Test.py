#
#Pandas Test:

#Part 1)
 #*  Make a new DataFrame with the data below:

#rng = date_range('1/1/2011', periods=72, freq='H')
#ts = Series(randn(len(rng)), index=rng)



# importing required packages
import numpy as np
import pandas as pd
from numpy import random 
from pandas import Series, DataFrame

rng = pd.date_range('1/1/2011', periods=72, freq='H')
ts = Series(random.randn(len(rng)), index=rng)

# Return a series where the absolute difference between a number and the next number in the series is less than .5
#****asumption**** the abs diff in ts series numbers is verifies to build a new series, 
#the numbers in resultant series may not have the difference between sub sequest values less than 0.5
myarray = Series() #new series
myframe= pd.DataFrame(ts,columns=['value']) #creating data frame from series
for i in range(len(myframe)-1):
    if abs(myframe['value'][i] - myframe['value'][i+1]) < 0.5: # condition
        myarray.set_value(myframe.index.values[i],myframe['value'][i]) # set value and indexx to new series
print myarray

# Plot and show a Histogram of the Series
import matplotlib.pyplot as plt
plt.hist(myarray)

#Give me the rolling average of the series over the last 5 hours in a new column on a DataFrame

rolling=pd.rolling_mean(myarray.values, 5) # using rolling function with 5 hours gap
print rolling
myrolling=Series(rolling,index=myarray.index) # crating new series for rolling to include index
print myrolling
myframe['rolling_avg']=myrolling # appending rolling values to data frame
print myframe

#Change any negative numbers in the new rolling average column to 0
    
myframe['rolling_avg']= myframe['rolling_avg'].apply(lambda x : 0 if x< 0 else x) # using lambda to apply condition to all rows
 print myframe['rolling_avg']  
 
 #Part 2)

 #Take your DataFrame and put it into Excel.
        # Make the width of the columns 20
        # Hide the gridlines on the excel sheet
        
#***  CHANGE EXCEL PATH BEFORE EXECUTION ***
writer = pd.ExcelWriter('C:\\Users\\POOJA\\Dropbox\\Resume\\full time\\Notes\\Avant\\output.xlsx', engine='xlsxwriter')
myframe.to_excel(writer,'Sheet1')
worksheet = writer.sheets['Sheet1']
worksheet.set_column(0,3,20)   # Trying to set column width as 20

worksheet.hide_gridlines(2) #hiding the gridlines

writer.save() 
writer.close()
