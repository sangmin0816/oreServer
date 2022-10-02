import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from urllib.parse import unquote

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("./hatescore-korean-hate-speech")
model = AutoModelForSequenceClassification.from_pretrained("./hatescore-korean-hate-speech")

app = flask.Flask(__name__) 
cors = CORS(app)

@app.route("/")
def home():
    return "Flask API get endpoint running"

@app.route('/analyze', methods=['POST'])
def analyze_context():
    article = request.get_json()
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
if __name__ == "__main__":
    app.run()