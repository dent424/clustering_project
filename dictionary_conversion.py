# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:30:25 2015

@author: Alex
"""

#This file converts a list of lists with a header list into a dictionary making the id number the dictionary key
def create_dictionary(data):
    var_names = data.pop(0)
    data_dict = {}
    for j, row in enumerate(data):
        temp_dict = {}
        for i, element in enumerate(row):
            if i != 1:        
                temp_dict[var_names[i]] = element
            else: 
                pass
            data_dict[data[j][1]] = temp_dict
    return data_dict