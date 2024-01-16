from django.http import HttpResponse
from django.shortcuts import render, redirect
import pickle
import os
from pathlib import Path



def index(requests):
    return render(requests, "index.html")

def calculator(requests):
    
    result = {'result': 'Click to Predict!'}
    
    try:
        attributes= {"total_sqft": None, 
                    "bath": 0.0, 
                    "balcony": 0.0,
                    "bhk": 0.0,
                    "area_type_le": 0.0,
                    "location_le": 0.0
                }
    
        if requests.method== 'POST':
            
            for col, val in attributes.items():
                attributes[col]= float(requests.POST.get(col))
        
        if attributes['total_sqft'] is None:
            return render(requests, 'calculator.html', result)
        
        file_path = 'model\hechPredictor_model'
        print(f"Attempting to open file at: {file_path}")

        with open(file_path, 'rb') as model:
            mdl = pickle.load(model)
    
        prediction= mdl.predict([[val for key, val in attributes.items()]])

        result['result']= prediction

    except:
        return HttpResponse('Error 404')

    
    return render(requests, 'calculator.html', result)
