# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:30:25 2015

@author: Alex
"""


#This file relates to the recoding and creation of dictionaries
import translation_dictionary

#This function converts a list of lists with a header list into a dictionary making the id number the dictionary key
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

#Takes in the data dictionary and the question answer map
#The question answer map is a dictionary where key is the variable name and the value is the id number of the answer type 
#Thequeswtion answer map is created in diagnostic_tools.generate_question_answer_map()

def recode_data(question_answer_map, data_dict):
    for question in question_answer_map:
        #Generates the recoding dictionary used to convert strings to numerical values in the data dictionary                
        translate = translation_dictionary.recode_dict()        
        for entry in translate:
            answer_set_id = question_answer_map[question]
            if answer_set_id == entry:
                recode_dict = translate[entry]
                for respondent in data_dict:
                    for response in recode_dict:
                        answer = data_dict[respondent][question]
                        if answer==response:
                            data_dict[respondent][question]=recode_dict[response]
                        else:
                            pass
    return data_dict