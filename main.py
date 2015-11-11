# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:24:18 2015

@author: Alex
"""
import pprint
import csv_tools
import diagnostic_suite
import cleaning_tools
import csv
import numpy as np
from clustering_suite import cluster

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

#Conducts clustering for data, outputting as either a dict or a list 
#data_dict, _=cluster(final_data_dict, range(2, 10), "dict")
data_list, features = cluster(final_data_dict, range(2, 10), "list")

#Writes data to csv file
with open('clusterData.csv', 'wb') as f:
    wr = csv.writer(f)
    wr.writerows([features])
    np.savetxt(f, data_list, delimiter=',', fmt="%s")
 



    



