# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:36:47 2015

@author: Alex
"""
#TOOLS FOR READING, WRITING, AND UPDATING CSV FILES


import csv
import os

#LOADS CSV FILE WHEN PASSED THE FILENAME AND PATH RETURNING A LIST OF LISTS
def load_data(path, filename):
    os.chdir(path)    
    data = []
    with open(filename, 'r') as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row) 
    return data