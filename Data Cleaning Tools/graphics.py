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
    y_axis = range(len(NaN_list)) #The respondents
    x_axis = range(len(NaN_list[0])) #The variables
    
    
    plt.figure(figsize=(20,10))    
    for i, y in enumerate(y_axis):
        ys = len(x_axis)*[y]
        y_vals = NaN_list[i]        
        yscolors = ['r' if y == 0 else 'g' for y in y_vals]        
        plt.scatter(x_axis,ys,c=yscolors,alpha=0.5, marker='s',lw=0,s=2)        
    plt.savefig('foo.png')