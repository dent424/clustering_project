# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:45:26 2015

@author: Alexander
"""

from sklearn import cluster
from sklearn.preprocessing import Imputer
import numpy as np

#Converts non_numeric values in a list to NaN
def convert_to_NaN(data_list):
    for i, response in enumerate(data_list):
        try:
            float(response)
        except:
            data_list[i]='NaN'
    return data_list
    
#Converts dictionary form data to an array
def convert_to_list(data_dict):
    data_array = np.array([])    
    for entry in data_dict:
        respondent = np.array([v for _,v in data_dict[entry].items()])        
        respondent = convert_to_NaN(respondent)        
        if data_array.size == 0:        
            data_array = np.array([respondent])            
        else:
            data_array = np.vstack((data_array, respondent))
    return data_array

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
    if np.array_equal(cluster_data.transpose(),cluster_data):    
        cluster_data = np.array([cluster_data]).transpose()       
    data_with_clusters = np.append(data, cluster_data, axis=1)
    new_feature_names = feature_names + new_features
    return data_with_clusters, new_feature_names
