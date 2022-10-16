import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from urllib.parse import unquote

app = flask.Flask(__name__) 
cors = CORS(app)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_context():
    article = request.get_json()
    print(article)
    res = requests.post("http://43.155.168.76:5000/analyze", data=article)
    return res.text

#APP RUNSERVER
app.run()