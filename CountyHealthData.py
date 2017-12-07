# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:30:13 2017

@author: leblanckh
"""

import pandas as pd
import numpy as np
from scipy import stats
import os
import sys
dataFolder = "/Users/leblanckh/Documents/CountyHealthData"
os.chdir(dataFolder)
FileList = os.listdir(dataFolder)

sheet_names = []

for File in FileList:
    if not File.endswith('.xls'):
        print ("skipping file named", File)
        continue
    currentFile = pd.ExcelFile(File, skiprows = 1, index_col = 0)
    RankedDF = currentFile.parse('Ranked Measure Data')
    AddMsrDF = currentFile.parse('Additional Measure Data')
    
    #I'm trying to do something very similar to the dataIncubator project, but for some reason\
    #the first few rows and columns aren't functioning normally.  I got hung up on trying to \
    #get the merge to work because it couldn't find the 'FIPS' column label with the AddMsrDF.
    print (RankedDF.iloc[1,1])
    print (AddMsrDF.iloc[3,3])
    #MasterDF = pd.merge(RankedDF,AddMsrDF,on = 'FIPS', how = 'outer')
    
#        ColumnNames = df.iloc[1,:].values.tolist()
#        sheet_names.append(ColumnNames)
#         pd.to_csv('./ColumnNames_%s.csv' % (sheet,))
#        print (ColumnNames)
#        YPLLFilters = ['Years of Potential Life Lost Rate', 'YPLL Rate']
#        YPLL =  Header[Header[0].isin(SubjectFilters)].iloc[0,1]
        
    Premature_death = MasterDF.loc[:,'Years of Potential Life Lost Rate']
    Physical_inactivity = MasterDF.loc[:,'% Physically Inactive']
    STD_rate = MasterDF.loc[:,'Chlamydia Rate']
    MH_ratio = MasterDF.loc[:,'MHP Ratio']
    percent_college = MasterDF.loc[:,'% Some College']
    income_inequal = MasterDF.loc[:,'Income Ratio']
    social_assoc = MasterDF.loc[:,'Association Rate']
    HIV = MasterDF.loc[:,'HIV Prevalence Rate']
    percent_LA_healthy_food = MasterDF.loc[:,'% Limited Access']
    health_costs = MasterDF.loc[:,'Costs']
    median_income = MasterDF.loc[:,'Household Income']
    percent_free_lunch = MasterDF.loc[:,'% Free or Reduced Lunch']
    percent_kids = MasterDF.loc[:,'% < 18']
    percent_elderly = MasterDF.loc[:,'% 65 and over']
    percent_AA = MasterDF.loc[:,'% African American']
    percent_AI = MasterDF.loc[:,'% American Indian/Alaskan Native']
    percent_AS = MasterDF.loc[:,'% Asian']
    percent_HAW = MasterDF.loc[:,'% Native Hawaiian/Other Pacific Islander']
    percent_HIS = MasterDF.loc[:,'% Hispanic']
    percent_white = MasterDF.loc[:,'% Non-Hispanic White']
    percent_no_english = MasterDF.loc[:,'% Not Proficient in English']
    percent_female = MasterDF.loc[:,'% Female']
    percent_rural = MasterDF.loc[:,'% Rural']
    
    ResultsList = [Premature_death,Physical_inactivity,STD_rate,MH_ratio,percent_college,\
    income_inequal,social_assoc,HIV,percent_LA_healthy_food,health_costs,median_income,\
    percent_free_lunch,percent_kids,percent_elderly,percent_AA,percent_AI,percent_AS,percent_HAW,\
    percent_HIS,percent_white,percent_no_english,percent_female,percent_rural]

ResultsDF = pd.concat(ResultsList, axis = 1)
#print ('ResultsDF', ResultsDF)
    
    
    
    

#df2 = pd.DataFrame(data=sheet_names)
#df2.to_csv('./ColumnNames2.csv')


#HealthDF = DF.parse('HEALTH')
#StoresDF = DF.parse('STORES')
#RestDF = DF.parse('RESTAURANTS')
#InsecureDF = DF.parse('INSECURITY')
#LocalDF = DF.parse('LOCAL')
#AssistDF = DF.parse('ASSISTANCE')
#VariablesDF = DF.parse('Variable List')
#SheetList = [RestDF,InsecureDF,LocalDF,AssistDF]


    