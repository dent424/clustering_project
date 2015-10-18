# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:13:16 2015

@author: Alexander
"""

import unittest
from diagnostic_tools import count_empty

class TestC_E(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_empty_dict(self):
        testSet=[['a','a','a'],[1,1,1],['','',''],['','a',2]]        
        self.assertEqual(count_empty(testSet),[0,0,3,1])
        
if __name__=='__main__':
    unittest.main()