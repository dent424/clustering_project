# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:45:26 2015

@author: Alexander
"""

from sklearn import cluster
from sklearn.preprocessing import Imputer

#Converts dictionary form data to an array
def convert_to_list(data_dict):
    data_array = []    
    for entry in data_dict:
        respondent = [v for _,v in data_dict[entry].items()]
        data_array.append(respondent)        
    return data_array

#Converts non_numeric values to NaN
def convert_to_NaN(data_list):
    for i, respondent in enumerate(data_list):
        for j, response in enumerate(respondent):
            try:
                float(response)
            except:
                data_list[i][j]='NaN'
    return data_list

#Preprocesses the data to prepare for clustering
def preprocess(data_list):    
    imp = Imputer()
    imputed_data = imp.fit_transform(data_list)
    return imputed_data
    
#Clusters the data
def clustering(data, num_clusters):
    clf = cluster.KMeans(n_clusters=num_clusters)
    clf.fit(data)
    transformed = clf.transform(data)
    print transformed[:3]
    predicted = clf.predict(data)
    print predicted[:3]

