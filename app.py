from flask import Flask, render_template,render_template,send_from_directory,request,jsonify,make_response
from flask_cors import CORS, cross_origin
import boto3
import os
import time

app = Flask(__name__
    ,static_folder='frontend/build',static_url_path='')
cors = CORS(app)

@app.route('/api')
@cross_origin()
def Welcome():
    return "Welcome to the API!!"

@app.route('/time')
@cross_origin()
def get_current_time():
    return {'time': time.time()}

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder,'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')