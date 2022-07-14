# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:12:07 2022

@author: DC
"""

import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded = pickle.load(open('C:/Users/DC/OneDrive/Desktop/vihar_project_final/trained_model.sav','rb'))

# Creating a function for prediction

def diabetes_prediction(input_data):
    
    input_data= (5,166,72,19,8,0,587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
       return 'The Person is not diabetec'
    else:
       return 'The person is diabetec'
   



def main():
       
       #giving a title
       st.title('Diabetes Prediction Web App')
       
       #getting the input data from the user
       #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
       Pregnancies= st.text_input('Number of Pregnancies')
       Glucose= st.text_input('Glucose Level')
       BloodPressure = st.text_input('Blood Pressure Value')
       SkinThickness = st.text_input('Skin Thickness Value')
       Insulin = st.text_input('Insulin Level')
       BMI = st.text_input('BMI Value')
       DiabetesPedigreeFunction = st.text_input('Diabetes Predigree Function Value')
       Age = st.text_input('Age of the Person')
       
       #Code for Prediction
       diag = ""
       
       #creating a button for prediction
       
       if st.button('Diabetes Test Result'):
           diag = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
       
       st.success(diag)
        
if __name__== '__main__':
    main()