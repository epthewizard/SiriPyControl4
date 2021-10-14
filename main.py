import json
from logging import debug
from typing_extensions import ParamSpecArgs
from dotenv.main import load_dotenv
from flask import Flask, request, jsonify
from c4_auth import director, FLASKPASS
from lights import check_lights, toggle_lights 
from garage import toggle_garage
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return 'IT WORKS IT RELOADED'

@app.route('/light/status', methods=['POST'])
def light_status():
	try:
		password = request.form['pw']
		if password == FLASKPASS:
			return check_lights()
		return "Incorrect Password"
	except:
		return "Incorrect Password"

@app.route('/light/toggle', methods=['POST'])
def toggle_light():
        password = request.form['pw']
        if password == FLASKPASS:
                return toggle_lights()

@app.route('/garage/toggle', methods=['POST'])
def openclose_garage():
	try:
		password = request.form['pw']
		if password == FLASKPASS:
			return toggle_garage()
		return 'Incorrect Password'
	except:
		return "Incorrect Password"	
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
