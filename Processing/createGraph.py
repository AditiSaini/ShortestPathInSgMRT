#This file has functions used to create a graph structure for all the stations
from Structure import graph
import itertools

#Helper functions for creating the graph
#Weight between two stations
def weightBetweenTwoStations(station1, station2, stationTime):
    if station1[:2] == station2[:2]:
        return stationTime[station1[:2]]
    else:
        return stationTime['Change']

def addIntersectionForTwoStations(station1, station2, g, stationTime):
    weight = weightBetweenTwoStations(station1, station2, stationTime)
    g.addEdge(station1, station2, weight)
    return g

#Graph representation and connection of stations
#Step 1. Add edge in graph for adjacent stations
def createGraphForAdjacentStations(stations, maps, stationTime):
    g = graph.Graph()
    #Iterates through every station name
    for station in stations:
        df = maps[maps['Station Code'].str.match(station)]
        if len(df)>0:
            min_index = df['Station Code'].index[0]
            max_index = df['Station Code'].index[-1]
            #Adds adjacent station to current stations (prev and next)
            for index in range(len(df['Station Code'])):
                row = df['Station Code'][df['Station Code'].index[index]]
                if (index-1>=0):
                    prev_index = df['Station Code'].index[index-1]
                    if (prev_index >= min_index) and df['Station Code'][prev_index] not in g.graph_dict[row]:
                        weight = weightBetweenTwoStations(row, df['Station Code'][prev_index], stationTime)
                        g.addEdge(row, df['Station Code'][prev_index], weight)
                if (index+1< len(df)):
                    next_index = df['Station Code'].index[index+1]
                    if (next_index < max_index) and df['Station Code'][next_index] not in g.graph_dict[row]:
                        weight = weightBetweenTwoStations(row, df['Station Code'][next_index], stationTime)
                        g.addEdge(row, df['Station Code'][next_index], weight)
    return g

#Step 2. Add edge in graph for common stations between lines
def addAllIntersectedStations(intersectedStations, graph, stationTime):
    # For each intersected stations with more than one line, add edge to graph for both names
    for station in intersectedStations:
        combos = list(itertools.combinations(range(len(intersectedStations[station])), 2))
        for chance in combos:
            graph = addIntersectionForTwoStations(intersectedStations[station][chance[0]], intersectedStations[station][chance[1]], graph, stationTime)
    return graph

