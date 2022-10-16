import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from urllib.parse import unquote

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("sgunderscore/hatescore-korean-hate-speech")
model = AutoModelForSequenceClassification.from_pretrained("sgunderscore/hatescore-korean-hate-speech")

app = flask.Flask(__name__) 
cors = CORS(app)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_context():
    article = request.form.get('analyze')
    print(article)
    result = infer(article)
    return jsonify(result)

def infer(x):
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
    result = classifier(x)
    result = result[0]['label']
    print(result)
    return result

#APP RUNSERVER
app.run()