#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports and such
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mp
import numpy as np
import math as m


# In[2]:


#create a blank data frame which will take our final analysis for the [ɑ] vowel
data = {'year':[], 'vowel':[], 'F1/F2 dif':[], 'F3 dif':[]}
ar_data_frame = pd.DataFrame(data)

#create an excel sheet variable and grab the amount of sheets in it
xl = pd.ExcelFile("/Users/derekchase/Desktop/capstone files/Excel books/ar data workbook.xlsx")
sheet_len = len(xl.sheet_names)

#we're going to interate through each sheet of the workbook and do some analysis
for i in range(sheet_len-1):
    
    #create a (shortlived) dataframe to get the year variable
    df = pd.read_excel(xl, sheet_name=i+1,)
#     print(df.columns.tolist())
    yr = int(df.loc[0, "Year"])
    vl = df.loc[0, "Vowel"]
    
    #re-create the frame without the year column to get pure data, and grab the number of rows
    df = pd.read_excel(xl, sheet_name=i+1, usecols="A:E")
    data_len = len(df["F1_Hz"])
    
    #create blank lists
    f1 = []
    f2 = []
    f3 = []
    
    #add the data
    for j in range(data_len):
        f1.append(df.loc[j, "F1_Hz"])
        f2.append(df.loc[j, "F2_Hz"])
        f3.append(df.loc[j, "F3_Hz"])
    
    #grab the top and bottom halves of the data
    btm_hlf = m.floor(data_len/2)
    top_hlf = data_len - btm_hlf  
    
    #loop through the top and bottom halves of the formant lists (f1 and f2 specifically) 
    #to check for glide vowels
    f1bsum = 0
    f1tsum = 0
    f2bsum = 0
    f2tsum = 0
    f3bsum = 0
    f3tsum = 0
    for j in range(btm_hlf):
        f1bsum += f1[j]
        f2bsum += f2[j]
        f3bsum += f3[j]
    f1bavg = f1bsum/btm_hlf
    f2bavg = f2bsum/btm_hlf
    f3bavg = f3bsum/btm_hlf
    for j in range(top_hlf):
        f1tsum += f1[btm_hlf + j]
        f2tsum += f2[btm_hlf + j]
        f3tsum += f3[btm_hlf + j]
    f1tavg = f1tsum/top_hlf
    f2tavg = f2tsum/top_hlf
    f3tavg = f3tsum/top_hlf
    
    #find the difference
    f1dif = abs(f1tavg - f1bavg)
    f2dif = abs(f2tavg - f2bavg)
    f3dif = abs(f3tavg - f3bavg)
    
    #when the difference is too large, consider the [ɑ] a glide, else, keep the averages
    if f1dif <= 200:
        f1avg = (f1bavg+f1tavg)/2
    else:
        f1avg = ''
    
    if f2dif <= 400:
        f2avg = (f2bavg+f2tavg)/2
    else:
        f2avg = ''
        
    #finally, create a new dataframe row and add it to the blank to append new data
    if f1avg and f2avg != '':
        f1_2_dif = f2avg - f1avg
        f3_dif = abs(f3tavg - f3bavg)
        newline = {'year': yr, 'vowel': vl, 'F1/F2 dif': f1_2_dif, 'F3 dif': f3_dif}
        ar_data_frame.loc[len(ar_data_frame)] = newline
    pd.set_option('display.max_rows', 20)
        
    ar_data_frame.to_excel('AR ANALYSIS.xlsx', sheet_name='AR data frame')

    
print(ar_data_frame)


# In[3]:


#create a blank data frame which will take our final analysis for the [ɑ] vowel
data = {'year':[], 'vowel':[], 'F1/F2 dif':[], 'F3 dif':[]}
ar_data_frame = pd.DataFrame(data)

#create an excel sheet variable and grab the amount of sheets in it
xl = pd.ExcelFile("/Users/derekchase/Desktop/capstone files/Excel books/modern ar book.xlsx")
sheet_len = len(xl.sheet_names)

#we're going to interate through each sheet of the workbook and do some analysis
for i in range(sheet_len):
    
    #create a (shortlived) dataframe to get the year variable
    df = pd.read_excel(xl, sheet_name=i,)
#     print(df.columns.tolist())
    yr = int(df.loc[0, "Year"])
    vl = df.loc[0, "Vowel"]
    
    #re-create the frame without the year column to get pure data, and grab the number of rows
    df = pd.read_excel(xl, sheet_name=i, usecols="A:E")
    data_len = len(df["F1_Hz"])
    
    #create blank lists
    f1 = []
    f2 = []
    f3 = []
    
    #add the data
    for j in range(data_len):
        f1.append(df.loc[j, "F1_Hz"])
        f2.append(df.loc[j, "F2_Hz"])
        f3.append(df.loc[j, "F3_Hz"])
    
    #grab the top and bottom halves of the data
    btm_hlf = m.floor(data_len/2)
    top_hlf = data_len - btm_hlf  
    
    #loop through the top and bottom halves of the formant lists (f1 and f2 specifically) 
    #to check for glide vowels
    f1bsum = 0
    f1tsum = 0
    f2bsum = 0
    f2tsum = 0
    f3bsum = 0
    f3tsum = 0
    for j in range(btm_hlf):
        f1bsum += f1[j]
        f2bsum += f2[j]
        f3bsum += f3[j]
    f1bavg = f1bsum/btm_hlf
    f2bavg = f2bsum/btm_hlf
    f3bavg = f3bsum/btm_hlf
    for j in range(top_hlf):
        f1tsum += f1[btm_hlf + j]
        f2tsum += f2[btm_hlf + j]
        f3tsum += f3[btm_hlf + j]
    f1tavg = f1tsum/top_hlf
    f2tavg = f2tsum/top_hlf
    f3tavg = f3tsum/top_hlf
    
    #find the difference
    f1dif = abs(f1tavg - f1bavg)
    f2dif = abs(f2tavg - f2bavg)
    f3dif = abs(f3tavg - f3bavg)
    
    #when the difference is too large, consider the [ɑ] a glide, else, keep the averages
    if f1dif <= 300:
        f1avg = (f1bavg+f1tavg)/2
    else:
        f1avg = ''
    
    if f2dif <= 600:
        f2avg = (f2bavg+f2tavg)/2
    else:
        f2avg = ''
        
    #finally, create a new dataframe row and add it to the blank to append new data
    if f1avg and f2avg != '':
        f1_2_dif = f2avg - f1avg
        f3_dif = abs(f3tavg - f3bavg)
        newline = {'year': yr, 'vowel': vl, 'F1/F2 dif': f1_2_dif, 'F3 dif': f3_dif}
        ar_data_frame.loc[len(ar_data_frame)] = newline
        
    ar_data_frame.to_excel('MODERN AR ANALYSIS.xlsx', sheet_name='AR data frame')

    
print(ar_data_frame)


# In[ ]:




