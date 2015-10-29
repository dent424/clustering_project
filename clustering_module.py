# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:45:26 2015

@author: Alexander
"""

from sklearn import cluster
from sklearn.preprocessing import Imputer
import numpy as np

#Converts dictionary form data to an array
def convert_to_list(data_dict):
    data_array = np.array([])    
    for entry in data_dict:
        respondent = [v for _,v in data_dict[entry].items()]        
        if data_array.size == 0:        
            #print "YA"
            data_array = np.array([respondent])            
        else:
            #print data_array
            #print respondent
            data_array = np.vstack((data_array, respondent))
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
    #print transformed
    predicted = clf.predict(data)
    #print predicted
    score = clf.score(data)
    return transformed, predicted, score

#cluster_data - list of cluster memberships
#data - response data
#feature names - list of feature names
#cluster name - what the cluster membership column should be called. Must be as a list
def add_new_data_to_rows(cluster_data, data, feature_names, new_features):
    data_with_clusters = [row + [cluster_data[i]] for i, row in enumerate(data)]      
    new_feature_names = feature_names + new_features
    return data_with_clusters, new_feature_names
        