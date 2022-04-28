# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:06:37 2022

@author: Edward

this lib is to switch to different data input.
"""
import pandas as pd

class ImportData:
    
  def import_csv(sourcedata):
    return(pd.read_csv(sourcedata))
  def import_json(sourcedata):
    return(pd.read_json(sourcedata))



        
 


  


        




