# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:46:32 2015

@author: Alex
"""

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