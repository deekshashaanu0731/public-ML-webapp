# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:43:57 2022

@author: miadmin
"""


import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
 
 # loading the saved models
 
diabetes_model = pickle.load(open('C:/Users/miadmin/Desktop/multiplediseae prediction/models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/miadmin/Desktop/multiplediseae prediction/models/heart_disease_model.sav', 'rb'))  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# sidebar for navigate

with st.sidebar:
    
 selected = option_menu('multiplediseae prediction',
                        ['Diabetes Prediction',
                         'Heart Disease Prediction'],
                        default_index = 0)
 
 #diabetes prediction page
 if (selected == 'Diabetes Prediction'):
     
     #page title
     st.title('Diabetes Prediction using ML')
     
if (selected == 'Heart Disease Prediction'):
    
    #page title 
    st.title('Heart Disease Prediction using ML') 


 
 




                                                        
    