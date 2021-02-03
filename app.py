# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
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


if __name__ == "__main__":
    app.run(debug=True)
