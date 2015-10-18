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
    unmatched_count={}    
    #Generates the recoding dictionary used to convert strings to numerical values in the data dictionary                
    translate = translation_dictionary.recode_dict()
    #pulls out a question, answer-type ID combination   
    for question in question_answer_map:
        #Pulls up a recoded question answer-set combination                     
        for entry in translate:
            #pulls out the answer-set ID number              
            answer_set_id = question_answer_map[question]            
            if answer_set_id == entry:
                #if the answer-set-ID # is equal to the translation dict
                #Pulls out the dictionary with the answer-set
                recode_dict = translate[entry]
                #pulls out a row from the data_dictionary
                for respondent in data_dict:
                    #iterates individual responses for the row
                    zero  = 0                    
                    for response in recode_dict:
                        #pulls out the un recoded answer
                        answer = data_dict[respondent][question]
                        #If the answer is equal to the response... 
                        if answer==response:
                            #replace the dictionary entry
                            data_dict[respondent][question]=recode_dict[response]
                            zero = 1
                        else:
                            pass
                    #If recoder finds non-recodable value, creates a dictionary entry for that row with the count
                    if zero == 0:
                        if respondent in unmatched_count.keys(): 
                            unmatched_count[respondent]+=1
                        else:
                            unmatched_count[respondent]=1
                                           
    return unmatched_count, data_dict