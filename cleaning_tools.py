# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:49:31 2015

@author: Alex
"""
import diagnostic_tools

#Remove rows with no data
def remove_empties(data):
    counter = 0
    delete_rows = []    
    for row in data:      
        if diagnostic_tools.count_one_empty(row) != 0:
            delete_rows.append(row)            
            counter += 1
    for row in delete_rows:
        data.remove(row)
    print counter, " ROWS REMOVED"
    return data
    
#Removes fields from dictionaries that have no useful data
def remove_single_answers(del_keys, data_dict):
    for row in data_dict:
        for key in del_keys:    
            if key in data_dict[row]:
                del data_dict[row][key]    
    return data_dict