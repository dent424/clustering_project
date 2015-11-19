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
#Note that del_keys is a list
def remove_single_answers(del_keys, data_dict):
    for row in data_dict:
        for key in del_keys:    
            if key in data_dict[row]:
                del data_dict[row][key]    
    return data_dict

#takes in a dictionary and replaces value in replace_value with nan
def replace_with_nan(replace_value, d):    
    for row in d:
        for cell in d[row]:
            if d[row][cell] == replace_value:
                d[row][cell] = 'NaN'
    return d

#filters answers based on the id provided in answer_pattern_id
def filter_data_dict(dataDict, answer_pattern_id, tolerance, answer_patterns_id_dict):
    filtered_dict = {}    
    basis_answer_pattern = answer_patterns_id_dict[answer_pattern_id]
    for respondent in dataDict:        
        comparison_pattern = diagnostic_tools.get_single_answer_pattern(dataDict[respondent])
        difference = diagnostic_tools.compare_answer_patterns(basis_answer_pattern, comparison_pattern)
        if difference <= tolerance:
            filtered_dict[respondent] = dataDict[respondent] 
    return filtered_dict
    
#Filters dictionary of question names and the percent of respondents not answering those questions keeping only
#Those less than tolerance
def filter_missing_value_questions(data_dict, tolerance, reporting=0):
    question_answered_dict = diagnostic_tools.get_question_NaN_ratio(data_dict)  
    new_questions_dict = {k:v for k, v in question_answered_dict.iteritems() if v < tolerance }    
    if reporting !=0:
        print "Number of questions reduced from ", len(question_answered_dict.keys()), " to ", len(new_questions_dict.keys())
    return new_questions_dict

#Takes in the data and removes all key,value pairs where the key is not a key in output
def filter_respondent_questions(keep_vars, dataDict):
    final_dict = {}    
    for respondent in dataDict:    
        temp_dict={k:v for k,v in dataDict[respondent].iteritems() if k in keep_vars}
        final_dict[respondent]=temp_dict
    return final_dict

#Filters out respondents that have more than tolerance missing values
def filter_respondents(data_dict, tolerance, reporting=0):
    NaN_dict = diagnostic_tools.get_NaN_ratio(data_dict)
    final_dict = {k: v for k, v in data_dict.items() if NaN_dict[k] <= tolerance}
    if reporting != 0:
        print "Number of respondents reduced from ", len(data_dict), " to ", len(final_dict)
    return final_dict
            