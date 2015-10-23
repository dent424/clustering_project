# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:24:18 2015

@author: Alex
"""
import pprint
import csv_tools
import diagnostic_suite
#import graphics


data_path = "C:\Clustering Project\Data"
data_path_2 = "C:\users\Alexander\clustering_project\Data"
data_file = 'GSS_comma.csv'

#Sets up pretty printer for later use
pp = pprint.PrettyPrinter()

#Loads data from CSV into list of lists
data = csv_tools.load_data(data_path, data_file )

#Converts CSV data to dictionary
data = diagnostic_suite.run_diagnostics_and_transformations(data)
#runs the diagnostic and conversion suite which gets data ready for analysis
final_data=diagnostic_suite.run_dict_diagnostics(data)
#pp.pprint(final_data)








