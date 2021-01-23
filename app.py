# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np
import requests
import jsonify
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
standard_scaler = StandardScaler()

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    diesel = 0
    petrol = 0
    seller_type = 0
    transmission = 0
    
    if request.method == 'POST':
        
        curr_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        owner = int(request.form['Owner'])
        
        petrol_val = request.form['Fuel']
        if(petrol_val == 'Petrol'):
            petrol = 1
        else:
            diesel = 1
            
        year = int(request.form['Year'])
        age = 2020 - year
        
        seller_type_val = request.form['Seller_Type']
        if(seller_type_val == 'Individual'):
            seller_type = 1
        else:
            seller_type = 0
 
        transmission_val = request.form['Transmission']
        if(transmission_val == 'Manual'):
            transmission = 1
        else:
            transmission = 0
            
        prediction = model.predict([[curr_price, kms_driven, owner, age, diesel, petrol, seller_type, transmission]])
        output = round(prediction[0],2)        
        
        if(output < 0):
            return render_template('index.html', prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You can sell at {}".format(output))
        
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
        
        
        