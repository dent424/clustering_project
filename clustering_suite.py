# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:07:03 2015

@author: Alex
"""

import clustering_module
import dictionary_conversion
import numpy as np
from diagnostic_tools import compare_respondent_dicts
from sklearn.preprocessing import MinMaxScaler
#This file combines the functions of clustering module to create a single function call in main.py

def cluster(final_data_dict, cluster_range, list_or_dict):
    final_data_list= clustering_module.convert_to_list(final_data_dict) 
    respondent_IDs = np.array(map(int, final_data_dict.keys()))
    feature_names = final_data_dict.values()[0].keys()
    final_data_list_imputed = clustering_module.preprocess(final_data_list)
    Scaler = MinMaxScaler()    
    final_data_list_scaled = Scaler.fit_transform(final_data_list_imputed)
    #Transformed is distance of each respondent from each cluster center
    #Predicted is the cluster membership of each respondent
    merging_list = clustering_module.convert_to_list(final_data_dict,remove_NaN=0 )
    data = list(merging_list)
    ignore_set_added = set(['ids'])
    for num_clusters in cluster_range:    
        transformed, predicted, score = clustering_module.clustering(final_data_list_scaled, num_clusters)
        cluster_name = "%s_clusters" % num_clusters
        ignore_set_added.add(cluster_name)    
        data, feature_names = clustering_module.add_new_data_to_rows(predicted, data, feature_names, [cluster_name])
    data, feature_names = clustering_module.add_new_data_to_rows(respondent_IDs, data, feature_names, ["ids"], "before")
    if list_or_dict == "dict":        
        temp = dictionary_conversion.create_dictionary(data, feature_names)    
        num_converted = dictionary_conversion.convert_values_to_int(temp)    
        #Set of features that should be different due to being categorical
        ignore_set_changed = set(['busgrn', 'peopgrn', 'sex', 'race', 'topprob1', 'topprob2'])    
        verdict = compare_respondent_dicts(respondent_IDs, num_converted, final_data_dict, ignore_set_changed, ignore_set_added)
        return num_converted, verdict
    elif list_or_dict == "list":
        return data, feature_names
    