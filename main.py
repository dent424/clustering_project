# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:24:18 2015

@author: Alex
"""
import pprint
import csv_tools
import diagnostic_suite
from diagnostic_tools import compare_respondent_dicts
import cleaning_tools
import clustering_module
import dictionary_conversion
import numpy as np
#import graphics


data_path = "C:\Clustering Project\Data"
data_path_2 = "C:\users\Alexander\clustering_project\Data"
data_file = 'GSS_comma.csv'

#Sets up pretty printer for later use
pp = pprint.PrettyPrinter()

#Loads data from CSV into list of lists
data_list_form = csv_tools.load_data(data_path, data_file )

#Converts CSV data to dictionary
data = diagnostic_suite.run_diagnostics_and_transformations(data_list_form)
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
respondent_IDs = np.array(map(int, final_data_dict.keys()))
feature_names = final_data_dict.values()[0].keys()
final_data_list_imputed = clustering_module.preprocess(final_data_list)
#Transformed is distance of each respondent from each cluster center
#Predicted is the cluster membership of each respondent
transformed, predicted, score = clustering_module.clustering(final_data_list_imputed, 5)
merging_list = clustering_module.convert_to_list(final_data_dict)
data, var_names = clustering_module.add_new_data_to_rows(predicted, merging_list, feature_names, ["5_Cluster"])
data, var_names = clustering_module.add_new_data_to_rows(respondent_IDs, data, var_names, ["ids"], "before")
temp = dictionary_conversion.create_dictionary(data, var_names)
num_converted = dictionary_conversion.convert_values_to_int(temp)

#Set of features that should be different due to being categorical
ignore_set_changed = set(['busgrn', 'peopgrn', 'sex', 'race', 'topprob1', 'topprob2'])    
ignore_set_added = set(['5_Cluster'])    
compare_respondent_dicts(respondent_IDs, num_converted, final_data_dict, ignore_set_changed, ignore_set_added)
   

    



