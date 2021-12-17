import requests
import os
import json
import pandas as pd
from requests.exceptions import HTTPError
import time

url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
r = requests.get(url)

##Function 1##

def get_search_result(objectID1, objectID2):
    """
    get_search_results function gives museum collections dataframe within a specific ID range
    
    Parameters Setup
    ----------
    objectID1, objectID2: the searching spectrum (can be adjusted by user, within the database limit)
    i.e.: "1", "300"

    Returns
    -------
    A dataframe with the desired artwork information of non-public-domain (can be changed to other parameter)
    grabbed from metmuseum database.
    The results include about all artworks meeting input parameter values.
    """
    
    url2 = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
    object_data = []
    for i in range(objectID1,objectID2):
        url_i = f'{url2}{i}'
        r = requests.get(url_i)
        object_data.append(r.json())
                
    object_data_df = pd.DataFrame(object_data)
    
    return object_data_df

##Function 2##

def search_department(objectID1, objectID2, object_name, department_name):
    """
    objectID1, objectID2: the searching spectrum (can be adjusted by user, within the database limit)
    i.e.: "1", "300"

    search_department function gives specific museum collections in a department,
    that satisfy a certain set of query parameters, for the given dataframe extracted from get_search_result before
    It collects artwork information data from the met museum database
    
    Parameters Setup
    ----------
    object_name: Search term set by the user, can be a string of words, or a single word
    i.e.: "Coin" 
    
    department_name: objects that fall within the query search results,
    which belongs to a particular department in the mustum 
    i.e.: "The American Wing"
    
      
    Returns
    -------
    A dataframe with the desired artwork information grabbed from metmuseum database.
    The results include all artworks meeting input parameter values.
    """
    url2 = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
    object_data = []
    for i in range(objectID1,objectID2):
        url_i = f'{url2}{i}'
        r = requests.get(url_i)
        object_data.append(r.json())
                
    object_data_df = pd.DataFrame(object_data)
    type_data_df = object_data_df[object_data_df['objectName']==object_name]
    department_type_df = type_data_df[type_data_df['department']==department_name]
    
    return department_type_df

##Function 3##

def accession_distribution(objectID1, objectID2):
    """
    accession_distribution function gives the accession year distribution of
    all museum collections within a specific ID range.
    It collects artwork information data from the met museum database.
    
    Parameters Setup
    ----------
    objectID1, objectID2: the searching spectrum (can be adjusted by user, within the database limit)
    i.e.: "1", "300"

      
    Returns
    -------
    A dataframe with the desired artwork information grabbed from metmuseum database.
    The results include all artworks meeting input parameter values.
    """
    
    url2 = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
    object_data = []
    for i in range(objectID1,objectID2):
        url_i = f'{url2}{i}'
        r = requests.get(url_i)
        object_data.append(r.json())
                
    object_data_df = pd.DataFrame(object_data)
    accessionYear_df = object_data_df['accessionYear']
    
    print(object_data_df.accessionYear.value_counts().plot())
    
    return accessionYear_df
