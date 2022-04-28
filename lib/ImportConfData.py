# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:06:37 2022

@author: Edward


pip install PyYAML
conda install -c conda-forge -y pyyaml

to use
pip install PyYAML
conda install -c conda-forge -y pyyaml

this lib is to import variables from yaml or json files used from ./config 
"""
import json
import yaml

class ImportConfData:
   
   def import_config_json(source_data):
     with open("./config/config.json","r") as data:
       conf_var = json.load(data, Loader=json.FullLoader)
     return(conf_var[source_data])
 
   def import_config_yaml(source_data):
     with open("./config/config.yaml", "r") as data:
       conf_var = yaml.load(data, Loader=yaml.FullLoader)
     return(conf_var[source_data])
 
    

        
 


  


        




