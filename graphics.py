# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:33:44 2015

@author: Alex
"""


import matplotlib.pyplot as plt
from dictionary_conversion import create_NaN_list

#Creates a chart with questions on the y-axis, respondent on the x-axis to show NaN vs. Non-NaN values
#Each question, respondent combination would be assigned an x-y coordinate and would be 
#Red for NaN and Green for any other value.

    
def plot_NaNs(data_dict):
    NaN_list = create_NaN_list(data_dict)
    plt.plot(NaN_list)