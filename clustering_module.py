# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:45:26 2015

@author: Alexander
"""

import sklearn.cluster

def convert_to_list(data_dict):
    data_array = []    
    for entry in data_dict:
        respondent = [v for _,v in data_dict[entry].items()]
        data_array.append(respondent)
    print data_array
    return_data = sorted(data_array)        
    return return_data

