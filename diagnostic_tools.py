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
def find_delete_keys(possible_answers):
    del_keys = []    
    for question in possible_answers:
        if len(possible_answers[question])<2:
            print question, " ",possible_answers[question]
            del_keys.append(question)
    return del_keys