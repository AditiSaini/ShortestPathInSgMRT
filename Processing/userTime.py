#This file has functions to compute the time taken between each stop depending on the user entered time
from datetimerange import DateTimeRange
import pandas as pd

def defineStationTime(date):
    time = date[1]
    date_new = date[0]
    day = pd.to_datetime(date_new).day_name() 
    week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    formatted = date_new+'T'+time+':00'
    night_range1 = DateTimeRange(date_new+"T"+"22:00:00", date_new+"T"+"23:59:59")
    night_range2 = DateTimeRange(date_new+"T"+"00:00:00", date_new+"T"+"05:59:59")
    peak_range1 = DateTimeRange(date_new+"T"+"06:00:00", date_new+"T"+"09:00:00")
    peak_range2 = DateTimeRange(date_new+"T"+"18:00:00", date_new+"T"+"20:00:00")
    if (formatted in night_range1) or (formatted in night_range2):
        return "NIGHT"
    elif (day in week_day) and ((formatted in peak_range1) or (formatted in peak_range2)):
        return "PEAK"
    return "NON-PEAK and DAY"

def mapToTime(timeType):
    if (timeType=="PEAK"):
        return {'NS': 12, 'NE': 12, 'EW': 10, 'CG': 10, 'CC': 10, 'DT': 10, 'TE': 10, 'CE': 10, 'Change': 15}
    elif (timeType=="NIGHT"):
        return {'NS': 10, 'NE': 10, 'EW': 10, 'CC': 10, 'TE': 8, 'Change': 10}
    else:
        return {'NS': 10, 'NE': 10, 'EW': 10, 'CG': 10, 'CC': 10, 'DT': 8, 'TE': 8, 'CE': 10, 'Change': 10}