# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:13:16 2015

@author: Alexander
"""

import unittest
from diagnostic_tools import count_empty


class TestC_E(unittest.TestCase):
    def setUp(self):
        self.l = [['a','a','a'],[1,1,1],['','',''],['','a',2]]
    
    def test_empty_rows(self):
        self.assertEqual(count_empty(self.l),[0,0,3,1])
    

from dictionary_conversion import recode_data, recode_to_int

class TestRecodeData(unittest.TestCase):
    def setUp(self):
        self.QAMap = {'grncon':8,
                      'natspac': 1,
                      'watergen':21,
                      'priven' :16}
        self.dataDict = {'10000':{'grncon':'2',
                                  'natspac':'NaN',
                                  'watergen':'Extremely dangerous',
                                  'priven':'Agree'},
                         '10001':{'grncon':'NaN',
                                  'natspac':'Oppose',
                                  'watergen':'NaN',
                                  'priven':''},
                         '10002':{'grncon':'Plonky',
                                  'natspac':'Too little',
                                  'watergen':'Somewhat dangerous',
                                  'priven':'Disagree'},
                         '10003':{'grncon':'',
                                  'natspac':'',
                                  'watergen':'Somewhat dangerous',
                                  'priven':'Strongly agree'},
                         '10004':{'grncon':'Very concerned',
                                  'natspac':'About right',
                                  'watergen':'Not dangerous',
                                  'priven':'Strongly disagree'}}
        self.recodedDict = {'10000':{'grncon':2,
                                  'natspac':'NaN',
                                  'watergen':1,
                                  'priven':4},
                         '10001':{'grncon':'NaN',
                                  'natspac':'Oppose',
                                  'watergen':'NaN',
                                  'priven':''},
                         '10002':{'grncon':'Plonky',
                                  'natspac':1,
                                  'watergen':3,
                                  'priven':2},
                         '10003':{'grncon':'',
                                  'natspac':'',
                                  'watergen':3,
                                  'priven':5},
                         '10004':{'grncon':5,
                                  'natspac':2,
                                  'watergen':5,
                                  'priven':1}}
        self.outputDict = {'10001':['natspac','priven'],
                           '10002':['grncon'],
                           '10003':['natspac','grncon']}
       
        self.ignore = ['natspac','grncon']
        
        self.outputWithIgnoreDict = {'10001':['priven']} 
        
        self.string_int_dict = {'10000':{'grncon':'2',
                                         'natspac':'1',
                                         'watergen':'5',
                                         'priven':'3'},
                                    '10001':{'grncon':'NaN',
                                         'natspac':'Oppose',
                                         'watergen':'NaN',
                                         'priven':'2'},
                                    '10002':{'grncon':'Plonky',
                                        'natspac':'2',
                                        'watergen':'5',
                                        'priven':'1'},
                                    '10003':{'grncon':'',
                                        'natspac':'3',
                                        'watergen':'2',
                                        'priven':'1'},
                                    '10004':{'grncon':'1',
                                        'natspac':'5',
                                        'watergen':'3',
                                        'priven':'Strongly disagree'}}
        
        self.string_int_dict_recoded1 = {'10000':{'grncon':2,
                                         'natspac':'1',
                                         'watergen':'5',
                                         'priven':'3'},
                                    '10001':{'grncon':'NaN',
                                         'natspac':'Oppose',
                                         'watergen':'NaN',
                                         'priven':'2'},
                                    '10002':{'grncon':'Plonky',
                                        'natspac':'2',
                                        'watergen':'5',
                                        'priven':'1'},
                                    '10003':{'grncon':'',
                                        'natspac':'3',
                                        'watergen':'2',
                                        'priven':'1'},
                                    '10004':{'grncon':1,
                                        'natspac':'5',
                                        'watergen':'3',
                                        'priven':'Strongly disagree'}}
        
       
    #Tests to see whether the data recodes under normal circumstances   
    def test_recode_data(self):
        output, updated_dict =  recode_data(self.QAMap, self.dataDict)        
        print output        
        self.assertEqual(updated_dict, self.recodedDict)
        self.assertEqual(output, self.outputDict)
        
   #Tests to see whether the ignore functionality works
    def test_recode_with_ignore(self):
        output, updated_dict =  recode_data(self.QAMap, self.dataDict, self.ignore) 
        self.assertEqual(output, self.outputWithIgnoreDict)
    
    #Tests to make sure that strings of numbers are recoded as int in the specified variables    
    def test_recode_string_to_int(self):
        updated_dict = recode_to_int(self.string_int_dict, 'grncon')
        self.assertEqual(updated_dict, self.string_int_dict_recoded1)

from dictionary_conversion import create_NaN_list

#Tests the data that will be the input for the NaN graph
class TestGraphData(unittest.TestCase):
    def setUp(self):
        self.dataDict = {'10000':{'grncon':'2',
                                  'natspac':'NaN',
                                  'watergen':'Extremely dangerous',
                                  'priven':'Agree'},
                         '10001':{'grncon':'NaN',
                                  'natspac':'Oppose',
                                  'watergen':'NaN',
                                  'priven':'Strongly disagree'},
                         '10002':{'grncon':'Plonky',
                                  'natspac':'Too little',
                                  'watergen':'Somewhat dangerous',
                                  'priven':'Disagree'},
                         '10003':{'grncon':'1',
                                  'natspac':'Strongly disagree',
                                  'watergen':'Somewhat dangerous',
                                  'priven':'Strongly agree'},
                         '10004':{'grncon':'NaN',
                                  'natspac':'NaN',
                                  'watergen':'NaN',
                                  'priven':'Strongly disagree'}}
        self.outputList = [[0,0,1,1,1],[0,1,0,1,1],[0,1,0,1,1],[1,1,1,1,1]]

    #Tests to see whether a binary dictionary of NaN, Not-NaN is created
    def test_recode_into_binary_list(self):
        binary_output = create_NaN_list(self.dataDict)        
        self.assertEqual(self.outputList, binary_output)

from diagnostic_tools import get_NaN_ratio, get_question_NaN_ratio

class TestNaNCounter(unittest.TestCase):
    def setUp(self):
        self.dataDict = {'10000':{'grncon':'2',
                          'natspac':'NaN',
                          'watergen':'Extremely dangerous',
                          'priven':'Agree'},
                 '10001':{'grncon':'NaN',
                          'natspac':'Oppose',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'},
                 '10002':{'grncon':'Plonky',
                          'natspac':'Too little',
                          'watergen':'Somewhat dangerous',
                          'priven':'Disagree'},
                 '10003':{'grncon':'1',
                          'natspac':'Strongly disagree',
                          'watergen':'Somewhat dangerous',
                          'priven':'Strongly agree'},
                 '10004':{'grncon':'NaN',
                          'natspac':'NaN',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'}}

        self.outputDict = {'10000':0.25,
                           '10001':0.5,
                           '10002':0,
                           '10003':0,
                           '10004':0.75}
        self.questionOutputDict = {'grncon':0.4,
                                   'natspac':0.4,
                                   'watergen':0.4,
                                   'priven':0}

    #test the percent of a person's responses that are NaN    
    def test_get_NaN_ratio(self):
        test = get_NaN_ratio(self.dataDict)
        self.assertDictEqual(self.outputDict, test)
    
    #tests the percent of responses to a given question that are NaN
    def test_get_question_NaN_ratio(self):
        test = get_question_NaN_ratio(self.dataDict)
        self.assertDictEqual(self.questionOutputDict, test)
    
from diagnostic_tools import get_weights, answer_patterns, count_answer_patterns, get_single_answer_pattern, compare_answer_patterns, answer_pattern_crosstab, get_tolerance_matrix, collapse_tolerance_matrix
#This section tests the discovery and counting of answer patterns
class TestAnswerPatterns(unittest.TestCase):
    def setUp(self):
        self.dataDict={'10000':{'grncon':'2',
                          'natspac':'NaN',
                          'watergen':'Extremely dangerous',
                          'priven':'Agree'},
                 '10001':{'grncon':'NaN',
                          'natspac':'Oppose',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'},
                 '10002':{'grncon':'Plonky',
                          'natspac':'Too little',
                          'watergen':'Somewhat dangerous',
                          'priven':'Disagree'},
                 '10003':{'grncon':'1',
                          'natspac':'NaN',
                          'watergen':'Somewhat dangerous',
                          'priven':'Strongly agree'},
                 '10004':{'grncon':'NaN',
                          'natspac':'NaN',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'}}
        self.outputList = [sorted(['grncon','watergen','priven']), 
                           sorted(['natspac','priven']),
                           sorted(['grncon','natspac','watergen','priven']), 
                           sorted(['priven'])] 
        self.answer_pattern_id = {0:['priven'],
                                  1:['grncon', 'priven', 'watergen'],
                                  2:['natspac', 'priven'],
                                  3:['grncon', 'natspac', 'priven', 'watergen']}
        self.answer_pattern_count = {0:1,1:2,2:1,3:1}
        self.answer_pattern_crosstabs = [[0,2,1,3],[2,0,2,1],[1,2,0,2],[3,1,2,0]] 
        self.tolerance_matrix = [[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]]
        self.weights = [1,2,1,1]
        self.weighted_tolerance_matrix = [[1,0,1,0],[0,2,0,1],[1,0,1,0],[0,2,0,1]]
        self.collapsed_tolerance_matrix= {0:2,1:3,2:2,3:3}
    
    def test_get_single_answer_pattern(self):
        test = get_single_answer_pattern(self.dataDict['10000'])
        self.assertEqual(test, self.answer_pattern_id[1])

    #Finds answer patterns and returns a list of them 
    def test_answer_patterns(self):
        test = answer_patterns(self.dataDict)
        self.assertEqual(sorted(self.outputList),sorted(test))
        
    #Counts answer patterns in the data and returns two dicionaries, one with counts and one with ids.
    def test_count_answer_patterns(self):
        test, ids = count_answer_patterns(answer_patterns(self.dataDict), self.dataDict)
        self.assertDictEqual(self.answer_pattern_id, ids)        
        self.assertEqual(self.answer_pattern_count,test)
    #A simple test to see if the proper number of differences between lists comes back
    def test_compare_answer_patterns(self):
        difference = compare_answer_patterns(self.answer_pattern_id[0],self.answer_pattern_id[3])
        self.assertEqual(difference, 3)
    #Creates a matrix comparing all answer patterns to all other answer patterns
    def test_answer_pattern_crosstab(self):
        crosstab = answer_pattern_crosstab(self.answer_pattern_id) 
        self.assertEqual(crosstab, self.answer_pattern_crosstabs)

    #Tests whether a tolerance indicator matrix can be produced
    def test_tolerable_difference(self):
        tolerance = 1        
        tolerance_matrix = get_tolerance_matrix(self.answer_pattern_crosstabs, tolerance)
        self.assertEqual(tolerance_matrix, self.tolerance_matrix)
    
    #Tests the creation of weights for the tolerable_difference function    
    def test_weights(self):
        weights = get_weights(self.answer_pattern_count)
        self.assertEqual(weights, self.weights)
    
    #Tests the tolerable difference function with weights applied
    def test_tolerable_difference_weighted(self):
        tolerance = 1
        weights = get_weights(self.answer_pattern_count)
        weighted_tolerance_matrix = get_tolerance_matrix(self.answer_pattern_crosstabs, tolerance, weights)
        self.assertEqual(weighted_tolerance_matrix, self.weighted_tolerance_matrix)

    #Test to make sure that the tolerable_difference collapsing function works properly
    def test_collapse_tolerance_matrix(self):
        collapsed_matrix = collapse_tolerance_matrix(self.weighted_tolerance_matrix)        
        self.assertEqual(collapsed_matrix, self.collapsed_tolerance_matrix)

from cleaning_tools import filter_data_dict

class FilterAnswerPatterns(unittest.TestCase):
    def setUp(self):    
        self.collapsed_tolerance_matrix= {0:2,1:3,2:2,3:3}
        self.answer_pattern_id = {0:['priven'],
                                      1:['grncon', 'priven', 'watergen'],
                                      2:['natspac', 'priven'],
                                      3:['grncon', 'natspac', 'priven', 'watergen']}
        self.dataDict = {'10000':{'grncon':'2',
                              'natspac':'NaN',
                              'watergen':'Extremely dangerous',
                              'priven':'Agree'},
                     '10001':{'grncon':'NaN',
                              'natspac':'Oppose',
                              'watergen':'NaN',
                              'priven':'Strongly disagree'},
                     '10002':{'grncon':'Plonky',
                              'natspac':'Too little',
                              'watergen':'Somewhat dangerous',
                              'priven':'Disagree'},
                     '10003':{'grncon':'1',
                              'natspac':'Strongly disagree',
                              'watergen':'Somewhat dangerous',
                              'priven':'Strongly agree'},
                     '10004':{'grncon':'NaN',
                              'natspac':'NaN',
                              'watergen':'NaN',
                              'priven':'Strongly disagree'}}
        self.filtered_dict = {'10001':{'grncon':'NaN',
                              'natspac':'Oppose',
                              'watergen':'NaN',
                              'priven':'Strongly disagree'},
                               '10004':{'grncon':'NaN',
                              'natspac':'NaN',
                              'watergen':'NaN',
                              'priven':'Strongly disagree'}} 
        self.answer_pattern_id = {0:['priven'],
                          1:['grncon', 'priven', 'watergen'],
                          2:['natspac', 'priven'],
                          3:['grncon', 'natspac', 'priven', 'watergen']}
    
    def test_filter_data_dict(self):
        answer_pattern_id = 0
        tolerance = 1  
        filtered_dict = filter_data_dict(self.dataDict, answer_pattern_id, tolerance, self.answer_pattern_id)
        self.assertDictEqual(filtered_dict, self.filtered_dict)

from cleaning_tools import filter_missing_value_questions, filter_respondent_questions, filter_respondents

class FilterList(unittest.TestCase):

    def setUp(self):
        self.dataDict = {'10000':{'grncon':'NaN',
                          'natspac':'NaN',
                          'watergen':'Extremely dangerous',
                          'priven':'Agree'},
                 '10001':{'grncon':'NaN',
                          'natspac':'Oppose',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'},
                 '10002':{'grncon':'Plonky',
                          'natspac':'Too little',
                          'watergen':'Somewhat dangerous',
                          'priven':'Disagree'},
                 '10003':{'grncon':'1',
                          'natspac':'Strongly disagree',
                          'watergen':'Somewhat dangerous',
                          'priven':'Strongly agree'},
                 '10004':{'grncon':'NaN',
                          'natspac':'NaN',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'}}
        self.output_case_dict = {'natspac' :.40,
                                'watergen': .40,
                                'priven': 0}

        self.respondent_dict = {'10000':{'natspac':'NaN',
                          'watergen':'Extremely dangerous',
                          'priven':'Agree'},
                 '10001':{'natspac':'Oppose',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'},
                 '10002':{'natspac':'Too little',
                          'watergen':'Somewhat dangerous',
                          'priven':'Disagree'},
                 '10003':{'natspac':'Strongly disagree',
                          'watergen':'Somewhat dangerous',
                          'priven':'Strongly agree'},
                 '10004':{'natspac':'NaN',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'}}
        self.final_dict = {'10000':{'natspac':'NaN',
                          'watergen':'Extremely dangerous',
                          'priven':'Agree'},
                 '10001':{'natspac':'Oppose',
                          'watergen':'NaN',
                          'priven':'Strongly disagree'},
                 '10002':{'natspac':'Too little',
                          'watergen':'Somewhat dangerous',
                          'priven':'Disagree'},
                 '10003':{'natspac':'Strongly disagree',
                          'watergen':'Somewhat dangerous',
                          'priven':'Strongly agree'}}

    def test_filter_missing_value_questions(self):
        tolerance = 0.5                    
        tolerance2 = 0.5       
        output = filter_missing_value_questions(self.dataDict, tolerance)
        self.assertDictEqual(output, self.output_case_dict)
        output2 = filter_respondent_questions(output, self.dataDict)
        self.assertDictEqual(output2, self.respondent_dict)                
        output3 = filter_respondents(self.respondent_dict, tolerance2)
        print output3        
        self.assertDictEqual(output3, self.final_dict)

        

if __name__=='__main__':
    unittest.main()