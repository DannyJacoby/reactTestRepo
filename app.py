from flask import Flask, request, redirect, url_for, session, send_from_directory
from flask_cors import CORS, cross_origin
from flask_session import Session

# Non Flask/DB imports
from datetime import date
import os
import time

flaskApp = Flask(__name__, static_folder="frontend/", static_url_path="")
CORS(flaskApp)
Session(flaskApp)


@flaskApp.route("/time")
@cross_origin()
def get_current_time():
    return {"time" : time.time()}

@flaskApp.route("/date")
@cross_origin()
def get_current_date():
    return {"date" : date.today()}

@flaskApp.route("/")
@flaskApp.route("/index")
@cross_origin()
def index():
    return send_from_directory(flaskApp.static_folder, "index.html")

@flaskApp.errorhandler(404)
def not_found(e):
    return flaskApp.send_static_file('error.html')