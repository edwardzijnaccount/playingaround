# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:08:59 2022

@author: RodenburgE1

pd.Timedelta(np.timedelta64(1, "ms"))
#df['fin_time']= pd.to_datetime(df['fin_time'], format='%H:%M:%S.%f')
this is the main program, the one you see live
"""
import lib.ImportData 
import lib.DataConfig
import lib.ImportConfData
import pandas as pd
import numpy as np

source_data = lib.DataConfig.datafile("5ycsv")
df = lib.ImportData.import_csv(source_data)
df = df.loc[df['dist.m.'] == 3600].filter(['date','horse_name','fin_time','dist.m.'], axis=1)
df['date'] = pd.to_datetime(df.date)
df.dropna(inplace = True)

new = df["fin_time"].str.split(":", n = 1, expand = True)
  
# making separate first name column from new data frame
df["min"]= new[0]
  
# making separate last name column from new data frame
df["secmic"]= new[1]
  
# data  with .
new = df["secmic"].str.split(".", n = 1, expand = True)
df["sec"]= new[0]
df["mic"]= new[1]

#cleanup
df.drop(columns =["secmic"], inplace = True)

# df display
print(df)






#df.convert_string(df["fin_time"])
#df.info()
#pd.Series(['fin_time'], dtype="string")
#df = df.astype(str)
#df['fin_time'].str.split('.', expand=True)
#df['inbetween'] = df.groupby('horse_name")["fin_time"].transform('mean')
#df['inbetween'] = df.groupby('horse_name')["fin_time"].mean()
#x = np.mean(df['fin_time'])                             
#(df.groupby(['horse_name', 'fin_time'], as_index=False).mean()
#            .groupby('horse_name')['fin_time'].mean())
#df['mean_tmp']=df.groupby('horse_name')['fin_time'].transform(lambda x: x.ewm(alpha=0.30).mean())
#df['std_tmp']=df.groupby('horse_name')['fin_time'].transform(lambda x: x.ewm(alpha=0.30).std())
#df.dropna(subset=['std_tmp'], inplace=True)









