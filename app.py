# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:08:59 2022

@author: Edward

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
df["min"]= new[0].astype(int)
  
# making separate last name column from new data frame
df["secmic"]= new[1]
  
# data  with .
new = df["secmic"].str.split(".", n = 1, expand = True)
df["sec"]= new[0].astype(int)
df["mic"]= new[1].astype(int)

df = df.assign(mic1 = lambda x: (x['min'] * 60 * 1000))
df = df.assign(mic2 = lambda x: (x['sec'] * 1000))
df['fin_time_mic'] = df['mic1'] + df['mic2'] + df['mic']

#cleanup
df.drop(columns=['secmic','mic','mic1','mic2','sec','min'], inplace = True)

#df['mean_fintime'] = df.groupby('horse_name')['fin_time_mic'].mean()
df['mean_tmp']=df.groupby('horse_name')['fin_time_mic'].transform(lambda x: x.ewm(alpha=0.30).mean())
df['std_tmp']=df.groupby('horse_name')['fin_time_mic'].transform(lambda x: x.ewm(alpha=0.30).std())
print(df)

