# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:46:32 2015

@author: Alex
"""
import math
#Takes a dataset and sees how many cells in each row are empty
def count_empty(data):
    empty_num = []    
    for row in data:
        counter = count_one_empty(row)    
        empty_num.append(counter)
    return empty_num

#Takes one rows and sees how many cells are empty
def count_one_empty(row):
    counter = 0    
    for element in row:
        if element == '':
            counter += 1
    return counter

#Takes in a dictionary with fields as key names and returns all of the different types of answers presented    
def get_answers(data_dict):
    keys = data_dict["1"].keys()
    possible_answers={}
    for key in keys:
        possible_answers[key]=[]
    for respondent in data_dict:   
        for key in keys:
            if data_dict[respondent][key] not in possible_answers[key]:
                possible_answers[key].append(data_dict[respondent][key])
            else:
                pass
    return possible_answers

#Takes in the dictionary of possible answers and prints keys that have no meaningful variation in responses
def find_delete_keys(possible_answers, printer=0):
    del_keys = []    
    for question in possible_answers:
        if len(possible_answers[question])<2:
            if printer == 1:            
                print question, " ",possible_answers[question]
            else:
                pass
            del_keys.append(question)
    return del_keys

#Counts number of answers of a given type
def count_answer_types(answer_dict):
    answer_types = {}
    for answer_type in answer_dict:
        for answer in answer_dict[answer_type]:
            if answer in answer_types.keys():
                answer_types[answer] += 1
            else:
                answer_types[answer] = 1

    for w in sorted(answer_types, key=answer_types.get, reverse=True):
        print w, answer_types[w]

#Returns a non-repeating list of answer types when provided with a list like 
#the one outputted by get_answers())
def get_answer_types(possible_answers):
    answer_types = []
    for answer_set in possible_answers:
        if sorted(possible_answers[answer_set]) not in answer_types:
            answer_types.append(sorted(possible_answers[answer_set]))
    return answer_types

def get_var_answer_types(answer_types, possible_answers):
    answers_dict = {}
    for i, answer_type in enumerate(answer_types):    
        answers_dict[i]=answer_type

    answer_type_vars = {}
    for answer_type in answers_dict:
        answer_type_vars[answer_type] = []    
        for var in possible_answers:
            if sorted(answers_dict[answer_type]) == sorted(possible_answers[var]):
                answer_type_vars[answer_type].append(var)
    return answers_dict, answer_type_vars

#Maps questions to the id numbers of the question types
def generate_question_answer_map(answer_type_vars):
    question_answer_map = {}
    for answers in answer_type_vars:
        for question in answer_type_vars[answers]:
            question_answer_map[question] = answers
    return question_answer_map

#Finds the proportion of questions that every individual has a missing value for
def get_NaN_ratio(data_dict):
    NaN_dict = {}
    for respondent in data_dict:
        if respondent not in NaN_dict.keys():
            response_count = len(data_dict[respondent].keys())            
            NaN_dict[respondent]=0
            counter = 0
        for response in data_dict[respondent]:
            try:            
                if math.isnan(float(data_dict[respondent][response])):
                    counter += 1
            except:
                pass
        NaN_dict[respondent]=float(counter)/float(response_count)
    return NaN_dict
            
#Finds the proportion of respondents that have missing values for every question
def get_question_NaN_ratio(data_dict):
    NaN_dict = {}
    denominator = len(data_dict)    
    for respondent in data_dict:
        for question in data_dict[respondent]:
            if question not in NaN_dict.keys():
                NaN_dict[question]=0
            try:
                if math.isnan(float(data_dict[respondent][question])):
                    NaN_dict[question]+=1
            except:
                pass
    for item in NaN_dict:
        NaN_dict[item]=NaN_dict[item]/float(denominator)
    return NaN_dict

#This module finds the answer pattern for an individual respondent
def get_single_answer_pattern(respondent):
    temp_list = []
    for question in respondent:                 
        try:
            if math.isnan(float(respondent[question])):
                pass
            else:
                temp_list.append(question)
        except:
            temp_list.append(question)
    temp_list.sort()
    return temp_list

#Finds the different types of answer patterns that respondents provide
def answer_patterns(data_dict):
    full_list=[]    
    for respondent in data_dict:
        temp_list = get_single_answer_pattern(data_dict[respondent])
        if temp_list not in full_list:
            full_list.append(temp_list)                
    return full_list

#Counts the number of times each answer pattern occurs.
#Assigns ID numbers to each answer pattern
#Puts them into two dictionaries
#Requires the output of answer_patterns() as input along with the data in dictionary form   
def count_answer_patterns(answer_patterns, data_dict):
    answer_pattern_dict = {}
    answer_patterns_id = {}    
    for respondent in data_dict:
        temp_list = get_single_answer_pattern(data_dict[respondent])        
        for i, answer_pattern in enumerate(answer_patterns):
            if answer_pattern == temp_list:
                if i in answer_pattern_dict.keys():
                    answer_pattern_dict[i]+=1
                else:
                    answer_pattern_dict[i]=1
                    answer_patterns_id[i]=answer_pattern
    return answer_pattern_dict, answer_patterns_id

#compares two answer patterns and returns the number of differences between them
def compare_answer_patterns(answer_pattern1, answer_pattern2):
    if len(answer_pattern1)>len(answer_pattern2):  
        set1 = set(answer_pattern1)
        set2 = set(answer_pattern2)
    else:
        set1 = set(answer_pattern2)
        set2 = set(answer_pattern1)
    
    x = len(list(set1-set2))       
    return x 

#Takes the id dict reated by count_answer_patterns and creates a matrix showing the coloseness of answer patterns to each other    
def answer_pattern_crosstab(answer_pattern_id_dict):
    total_list=[]    
    for answer_pattern_id in answer_pattern_id_dict:
        temp_list=[]        
        for answer_pattern_comparison_id in answer_pattern_id_dict:        
            temp = compare_answer_patterns(answer_pattern_id_dict[answer_pattern_id],answer_pattern_id_dict[answer_pattern_comparison_id])
            temp_list.append(temp)
        total_list.append(temp_list)
    return total_list


#Gets the weights list to be used in the get_tolerance_matrix function from the get_pattern_dict output of count answer patterns
def get_weights(answer_pattern_count):
    return [answer_pattern_count[answer] for answer in answer_pattern_count]

#Creates a matrix that shows how many answer patterns are within tolerance distance to evey other answwer pattern.
#The input is the output of answer_pattern_crosstab 
def get_tolerance_matrix(answer_pattern_crosstab, tolerance, weights=[]):
    tolerance_matrix = []    
    for count_list in answer_pattern_crosstab:
        temp = []        
        for count in count_list:
            if count <= tolerance:
                temp.append(1)
            else:
                temp.append(0)
        if weights != []:
            try:
                temp = [a*b for a,b in zip(temp,weights)]
            except:
                print "Weights not applied due to different length lists"
        tolerance_matrix.append(temp)
    return tolerance_matrix            

#Collapses the tolerance matrix from above to get a measure of how similar an answer_pattern is to the whole
def collapse_tolerance_matrix(tolerance_matrix, printer=0):
    tolerance_metric_dict={}    
    for i, tolerance_list in enumerate(tolerance_matrix):        
        tolerance_metric_dict[i]=sum(tolerance_list)
    if printer != 0:
        tuples = []
        for pattern_id in tolerance_metric_dict:
            tuples.append((tolerance_metric_dict[pattern_id], pattern_id))
        tuples.sort(reverse=False)
        for pattern in tuples:
            print "answer_pattern ID: ", pattern[1], "number: ", pattern[0]
    return tolerance_metric_dict