# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:24:18 2015

@author: Alex
"""
import pprint
import csv_tools
import diagnostic_tools
import cleaning_tools
import dictionary_conversion

data_path = "C:\Clustering Project\Data"
data_file = 'GSS_comma.csv'

#Loads data from CSV into list of lists
data = csv_tools.load_data(data_path, data_file )

#This looks for any mostly empty rows
#print diagnostic_tools.count_empty(data)
#Looking at this data it is clear that the last two rows ought to be removed
#This code removes the 2 empty rows and returns the data
data = cleaning_tools.remove_empties(data)
#This data confirms that the data was removed
#print diagnostic_tools.count_empty(data)

#Converts the list data into dictionary data for easier analysis
data_dict = dictionary_conversion.create_dictionary(data)

#Analyzes possible answers for each field
possible_answers = diagnostic_tools.get_answers(data_dict)

#This analysis shows 4 dictionary keys associated with only 1 type of response
del_keys = diagnostic_tools.find_delete_keys(possible_answers)
#And removes these dictionary entries
cleaning_tools.remove_single_answers(del_keys, data_dict)

possible_answers = diagnostic_tools.get_answers(data_dict)
