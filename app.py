# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np
import requests
import jsonify
from sklearn.preprocessing import StandardScaler
import nltk

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/demos', methods=['GET'])
def demos():
    return render_template('demos.html')

@app.route('/demos/preprocessing', methods=['GET'])
def preprocessing():
    return render_template('/demos/preprocessing/preprocessing.html')

@app.route('/demos/preprocessing/tokenization', methods=['GET', 'POST'])
def tokenization():
    if request.method == 'POST':
        input = request.form['tokenize_input']
        words = nltk.word_tokenize(input)
        return render_template('/demos/preprocessing/tokenization.html', output=str(words), input=input)
    return render_template('/demos/preprocessing/tokenization.html')


@app.route('/demos/preprocessing/normalization', methods=['GET'])
def normalization():
    return render_template('/demos/preprocessing/normalization.html')

@app.route('/demos/preprocessing/noise-removal', methods=['GET'])
def noise_removal():
    return render_template('/demos/preprocessing/noise-removal.html')

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
