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

#load the data
source_data = lib.DataConfig.datafile("5ycsvM")
#create dataframe from import data 
df = lib.ImportData.import_csv(source_data)

#filter on dist = 3600 and select only column data horsename fin_time and dist.m
df = df.loc[df['dist.m.'] == 3600].filter(['date','horse_name','fin_time','dist.m.'], axis=1)
df['date'] = pd.to_datetime(df.date)

#drop the nan spaces to block errors
df.dropna(inplace = True)

#split fin_time in to 2 colums min (converted to int) sec+microsecnd
new = df["fin_time"].str.split(":", n = 1, expand = True)
df["min"]= new[0].astype(int)
df["secmic"]= new[1]
  
# convert secmic in to 2 columns of int type (sec and microsecond)
new = df["secmic"].str.split(".", n = 1, expand = True)
df["sec"]= new[0].astype(int)
df["mic"]= new[1].astype(int)

#make the min and sec into micro second and make 1 new column with only micsecond
df = df.assign(mic1 = lambda x: (x['min'] * 60 * 1000))
df = df.assign(mic2 = lambda x: (x['sec'] * 1000))
df['fin_time_mic'] = df['mic1'] + df['mic2'] + df['mic']

#cleanup and drop not neeted columns
df.drop(columns=['secmic','mic','mic1','mic2','sec','min'], inplace = True)

#make fin_time a time dtype so its clean
df['fin_time']= pd.to_datetime(df['fin_time'], format='%M:%S.%f')

#check dtype of fin_time_mic, is it  int?
df.info()

#trying to make average in new column mean_time
df['fin_time'].ewm().mean()
#df['mean_tmp']=df.groupby('horse_name')['fin_time_mic'].transform(lambda x: x.ewm(alpha=0.30).mean())
#df['std_tmp']=df.groupby('horse_name')['fin_time_mic'].transform(lambda x: x.ewm(alpha=0.30).std())

print(df)

