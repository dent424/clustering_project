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
data_path_2 = "C:\users\Alexander\clustering_project\Data"
data_file = 'GSS_comma.csv'

#Loads data from CSV into list of lists
data = csv_tools.load_data(data_path_2, data_file )

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
data_dict = cleaning_tools.remove_single_answers(del_keys, data_dict)
#Also removes variables that will not be used in the analysis
data_dict = cleaning_tools.remove_single_answers(['numemps'], data_dict)

#Finds the answer sets for each question
possible_answers = diagnostic_tools.get_answers(data_dict)

#Counts the occurence of answer types and prints out an ordered list of them
diagnostic_tools.count_answer_types(possible_answers)
#This analysis points out that there are three common answer types that correspond to no data.
#THese are  "No answer", "Not applicable", "Don't know", and "Dont know"

#In this case note that often more than one of these answer types will appear as responses to a given question
#As a result, it will appear that the number of Nan responses is lower than it ought to be
nan_replace = ["No answer","Not applicable", "Don't know", "Dont know", "Not available","Cant choose","Can t choose","No car, dont drive"]
for answer in nan_replace:
    data_dict = cleaning_tools.replace_with_nan(answer, data_dict)

#Prints new list of answers
possible_answers=diagnostic_tools.get_answers(data_dict)
#diagnostic_tools.count_answer_types(possible_answers)
   
#Answer types removes doubles from possible_answers 
answer_types = diagnostic_tools.get_answer_types(possible_answers)

#Creates an id number for each dictionary type and places it in a dictionary with the id as the key 
#and the list of responses as a value and returns answers_dict. Also creates answer_type_vars
#which makes a dictionary with the answer type id as key and a list of vars with that 
#answer type as values
answers_dict, answer_type_vars = diagnostic_tools.get_var_answer_types(answer_types, possible_answers)
print answer_type_vars

#Creates a dictionary where the key is the variable name and the value is the id number of the answer type 
#Takes in a dictionary where the keys are the id numbers and the values are lists containing questions with that question format

question_answer_map = diagnostic_tools.generate_question_answer_map(answer_type_vars)

pp = pprint.PrettyPrinter()
pp.pprint(answers_dict)

#Recodes all data values with their numerical alternatives
unmatched_dict, data_dict = dictionary_conversion.recode_data(question_answer_map, data_dict)