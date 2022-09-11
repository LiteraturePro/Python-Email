from flask import Flask
from flask import Flask, jsonify, request
from flask import render_template



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def time():
    return str(datetime.now())
