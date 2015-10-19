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
    

from dictionary_conversion import recode_data

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
    
if __name__=='__main__':
    unittest.main()