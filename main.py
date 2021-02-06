#This file merges all the functions to compute the shortest path with least time taken
import pandas as pd
from Processing import helper, createGraph, shortestDistance, userTime, validateInput
import json

def getFilteredDataForTrain(dateProcess):
    #Inputs and result 
    #Reading csv file
    maps = pd.read_csv('Data/StationMap.csv')
    date = pd.to_datetime(dateProcess[0], format='%Y-%m-%d')
    #Convert date to datetime type 
    maps['Opening Date'] = maps.apply(lambda row : helper.converToDatetime(row['Opening Date']), axis = 1) 
    maps = maps[maps['Opening Date'] <= date]
    return maps

def getTimingsAndStation(dateProcess):
    #Weight for each edge 
    timeType = userTime.defineStationTime(dateProcess)
    stationTime = userTime.mapToTime(timeType)
    stations = helper.getOperatingStations(timeType)
    return stations, stationTime, timeType

def stationMappedToCode(maps):
    #Mapping of station name to station code
    stationToCodeMap = dict(maps.groupby('Station Name')['Station Code'].apply(list))
    #Maps the station code to station
    codeToStation = maps[['Station Code', 'Station Name']].set_index('Station Code')['Station Name'].to_dict()
    return stationToCodeMap, codeToStation

def createGraphOfStations(stations, stationToCodeMap, stationTime, maps):
    #Getting all intersected stations
    intersectedStations = helper.getStationsWithLineExchange(stationToCodeMap)
    #Adding adjacent stations in the map
    graph = createGraph.createGraphForAdjacentStations(stations, maps, stationTime)
    #Adding intersected stations in the map
    graph = createGraph.addAllIntersectedStations(intersectedStations, graph, stationTime)
    return graph

def getPathAndTotalTimeWithLogs(startStation, endStation, graph, stationToCodeMap, stationTime, codeToStation, timeType):
    finalPath = shortestDistance.shortestDistanceBetweenTwoStations(graph, startStation, endStation, stationToCodeMap, stationTime)
    totalTime = helper.totalTimeTaken(finalPath, stationTime)
    logs = helper.stationLogs(finalPath, totalTime, codeToStation, timeType)
    return logs

def getFinalPath(dateEntered, startStation, endStation):
    #Process data to get final path
    dateProcessed = dateEntered.split('T')
    maps = getFilteredDataForTrain(dateProcessed)
    stations, stationTime,  timeType = getTimingsAndStation(dateProcessed)
    stationToCodeMap, codeToStation = stationMappedToCode(maps)
    graph = createGraphOfStations(stations, stationToCodeMap, stationTime, maps)
    logs = getPathAndTotalTimeWithLogs(startStation, endStation, graph, stationToCodeMap, stationTime, codeToStation, timeType)
    return logs

def isInputValid(dateEntered, startStation, endStation):
    if (dateEntered is None) or (startStation is None) or (endStation is None):
        return {'status': 404, 'response': json.dumps('Please Enter All Inputs Correctly')}
    elif (validateInput.validateDate(dateEntered)== False):
        return {'status': 404, 'response': json.dumps('Invalid Date')}
    elif (validateInput.validateTime(dateEntered)== False):
        return {'status': 404, 'response': json.dumps('Invalid Time')}
    elif (validateInput.validateStations(startStation, endStation)== False):
        return {'status': 404, 'response': json.dumps('Invalid Station Names')}
    elif (startStation==endStation):
        return {'status': 200, 'response': json.dumps('Your start station is same as your destination')}
    else:
        return True