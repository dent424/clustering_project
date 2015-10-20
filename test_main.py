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

    def test_get_NaN_ratio(self):
        test = get_NaN_ratio(self.dataDict)
        self.assertDictEqual(self.outputDict, test)
    
    def test_get_question_NaN_ratio(self):
        test = get_question_NaN_ratio(self.dataDict)
        self.assertDictEqual(self.questionOutputDict, test)
    
from diagnostic_tools import answer_patterns

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
                           
    def test_answer_patterns(self):
        test = answer_patterns(self.dataDict)
        self.assertEqual(sorted(self.outputList),sorted(test))

if __name__=='__main__':
    unittest.main()