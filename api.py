# import flask and jsonify (convert python dict into JSON for API routes)
from flask import Flask, jsonify
import subprocess
import os

# this is a rebase test.

# create a instance of app to use 
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_home():
    return "Welcome to the API! Use /date, /cal, /docker, or /cls."

# at '/date' endpoint, run this function
@app.route("/date", methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})

# at '/cal' endpoint, run this function
@app.route("/cal", methods=['GET'])
def get_cal():
    result = subprocess.check_output(['cal']).decode('utf-8')
    return jsonify({'calendar': result.strip()})

# at '/docker' endpoint, run this function
@app.route("/docker", methods=['GET'])
def get_docker():
    result = subprocess.check_output(['docker', 'ps']).decode('utf-8')
    return jsonify({'docker': result.strip()})

# at '/cls' endpoint, run this function- non-windows OS specific 
@app.route("/cls", methods=['GET'])
def get_cls():
    platform = os.name
    if platform == 'nt':
        message = "Screen cleared (Windows)"
    else:
        message = "Screen cleared (Linux/macOS)"
    return jsonify({'message': message})

# Check if the script is being run directly
if __name__ == '__main__':
    app.run(debug=True)