# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np
import requests
import jsonify
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

model = pickle.load(open('models/car_price_prediction.pkl', 'rb'))
standard_scaler = StandardScaler()

@app.route('/', methods=['GET'])
def load_home_page():
    return render_template('index.html')

@app.route('/index.html', methods=['GET'])
def load_index_page():
    return render_template('index.html')

@app.route('/portfolio.html', methods=['GET'])
def load_portfolio():
    return render_template('portfolio.html')

@app.route('/blog.html', methods=['GET'])
def load_blog_page():
    return render_template('blog.html')

@app.route('/about.html', methods=['GET'])
def load_about_page():
    return render_template('about.html')

@app.route('/contact.html', methods=['GET'])
def load_contact_page():
    return render_template('contact.html')

@app.route('/demos.html', methods=['GET'])
def load_demo_page():
    return render_template('demos.html')

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
            return render_template('index.html')
        else:
            return render_template('index.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
