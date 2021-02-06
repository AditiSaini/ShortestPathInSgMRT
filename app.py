#This file implements the endpoint using flask
from flask import Flask, request
from main import *
import json
import time

# create the Flask app
app = Flask(__name__)

#Helper function to package response to the client
def packageResponse(isValid, dateEntered, startStation, endStation):
    if (isValid==True):
        logs = getFinalPath(dateEntered, startStation, endStation)
        response = app.response_class(
        response=json.dumps(logs),
        status=200,
        mimetype='application/json')
        return response
    response = app.response_class(
    response=isValid['response'],
    status=isValid['status'],
    mimetype='application/json')
    return response

#Add space to query param using + e.g. start=Boon+Lay
@app.route('/path')
def get_path():
    #Get inputs from query params
    dateToday = time.strftime("%Y-%m-%dT%H:%M", time.gmtime())
    #Format: 2019-01-31T13:00
    dateEntered = dateToday if request.args.get('date') is None else request.args.get('date')
    startStation = ' '.join(request.args.get('start').split('+')) 
    endStation = ' '.join(request.args.get('end').split('+')) 
    isValid = isInputValid(dateEntered, startStation, endStation)
    return packageResponse(isValid, dateEntered, startStation, endStation)
    
if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)