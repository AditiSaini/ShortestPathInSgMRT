
#This file has functions to validate the user entered inputs
import datetime
import pandas as pd
import time
 
def validateDate(dateEntered):
    date_string = dateProcessed = dateEntered.split('T')[0]
    format = "%Y-%m-%d"
    try:
      datetime.datetime.strptime(date_string, format)
      return True
    except ValueError:
      return False

def validateTime(dateEntered):
    processed = dateProcessed = dateEntered.split('T')
    if len(processed)<= 1:
        return False
    time_string = processed[1]
    try:
        time.strptime(time_string, '%H:%M')
        return True
    except ValueError:
        return False

def validateStations(startStation, endStation):
    maps = pd.read_csv('Data/StationMap.csv')
    if (startStation not in set(maps['Station Name'])) or (endStation not in set(maps['Station Name'])):
        return False
    return True
    