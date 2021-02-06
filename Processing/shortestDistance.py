#This file has function to calculate the shortest distance between 2 stations and gets the shortest path with least time taken
import sys
from Algorithm import shortestPath
from Processing import helper

def shortestDistanceBetweenTwoStations(graph, stationName1, stationName2, stationToCodeMap, stationTime):
    if (stationName1 not in stationToCodeMap.keys()) or (stationName2 not in stationToCodeMap.keys()):
        return []
    possibleStartStations = stationToCodeMap[stationName1]
    possibleEndStations = stationToCodeMap[stationName2]
    leastTimeTaken = sys.maxsize
    bestPath = None
    for start in possibleStartStations:
        for end in possibleEndStations:
            path = shortestPath.dijsktra(graph, start, end)
            time = helper.totalTimeTaken(path, stationTime)
            if time<leastTimeTaken:
                leastTimeTaken = time
                bestPath = path
    return bestPath