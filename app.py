from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import requests
import datetime

pApi = Flask(__name__)
CORS(pApi)  # Initialize CORS

@pApi.route('/')
def code_name():
    try:
        # Preparing the additional information
        email = "akinrogundecodenamemomi@gmail.com" 
        current_datetime = datetime.datetime.now(datetime.timezone.utc).isoformat()
        github_url = "https://github.com/codenamemomi/pApi"  
        # Create the response
        return jsonify({
            'email': email,
            'current_datetime': current_datetime,
            'github_url': github_url
        }), 200  # it returns 200 ok status code for success
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500  # Returning a 500 status code for server errors
