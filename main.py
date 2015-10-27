# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:24:18 2015

@author: Alex
"""
import pprint
import csv_tools
import diagnostic_suite
import cleaning_tools
import clustering_module
#import graphics


data_path = "C:\Clustering Project\Data"
data_path_2 = "C:\users\Alexander\clustering_project\Data"
data_file = 'GSS_comma.csv'

#Sets up pretty printer for later use
pp = pprint.PrettyPrinter()

#Loads data from CSV into list of lists
data = csv_tools.load_data(data_path_2, data_file )

#Converts CSV data to dictionary
data = diagnostic_suite.run_diagnostics_and_transformations(data)
#runs the diagnostic and conversion suite which gets data ready for analysis
finalized_respondent_data=diagnostic_suite.run_dict_diagnostics(data)
#pp.pprint(final_data)

#creates a dictionary of variables where fewer than 10% of observations are missing
filtered_dict=cleaning_tools.filter_missing_value_questions(finalized_respondent_data, 0.10,1)
#pp.pprint(filtered_dict)

#Removes dictionary entries for features that are not in filtred_dict
data_dict_questions_filterd=cleaning_tools.filter_respondent_questions(filtered_dict.keys(), finalized_respondent_data)

#Removes respondents where, after filtering questions, more than 10% of questions are not answered
final_data_dict = cleaning_tools.filter_respondents(data_dict_questions_filterd, 0.1, 1)

final_data_list= clustering_module.convert_to_list(final_data_dict) 
feature_names = final_data_dict.values()[0].keys()

pp.pprint(final_data_list)
#pp.pprint(feature_names)

