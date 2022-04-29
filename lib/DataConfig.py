# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:55:06 2022

@author: Edward
"""
class DataConfig:

 def datafile(filename):    
   if "5ycsvM":
     output =  r'./../data/all_races05_19.csv'
     return output
   elif "5ycsvW":  
     output = r'.\..\data\all_races05_19.csv'
     return output
   else:
     return "default thing"
