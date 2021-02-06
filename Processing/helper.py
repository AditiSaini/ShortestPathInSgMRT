#This file has helper functions used to make the calculations in other files convenient
import pandas as pd

#Get stations with intersected lines
def getStationsWithLineExchange(stationToCodeMap):
    newDict = {}
    for station in stationToCodeMap:
        if len(stationToCodeMap[station])>1:
            newDict[station] = stationToCodeMap[station]
    return newDict

#Weight between two stations
def weightBetweenTwoStations(station1, station2, stationTime):
    if station1[:2] == station2[:2]:
        return stationTime[station1[:2]]
    else:
        return stationTime['Change']

#Total time taken for the journey
def totalTimeTaken(path, stationTime):
    totalTime = 0
    for p in range(1, len(path)):
        totalTime += weightBetweenTwoStations(path[p], path[p-1], stationTime)
    return totalTime

#Logs to show path for the journey
def stationLogs(finalPath, totalTime, codeToStation, timeType):
    logs = []
    for p in range(1, len(finalPath)):
        stationCode1 = finalPath[p-1]
        stationCode2 = finalPath[p]
        if stationCode1[:2]==stationCode2[:2]:
            logs.append("Take %s line from %s to %s" % (stationCode1[:2], codeToStation[stationCode1], codeToStation[stationCode2]))
        else:
            logs.append("Change from %s line to %s line" % (stationCode1[:2], stationCode2[:2]))
    logs.append("In total it will take approximately %s minutes during %s hours" % (totalTime, timeType))
    return logs

#Convert str date to datetime data structure in the dataframe
def converToDatetime(date): 
    monthDict={'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    processDate = date.split(' ')
    if len(processDate)==2:
        formattedDate = '01'+monthDict[processDate[0]]+processDate[1]
    else:
        formattedDate = processDate[0]+monthDict[processDate[1]]+processDate[2]
    return pd.to_datetime(formattedDate, format='%d%m%Y')

#Operating stations based on time
def getOperatingStations(timeType):
    if (timeType == "NIGHT"):
        return ['(NS.*)', '(EW.*)', '(NE.*)', '(CC.*)', '(TE.*)']
    else:
        return ['(NS.*)', '(EW.*)', '(CG.*)', '(NE.*)', '(CC.*)', '(DT.*)', '(TE.*)', '(CE.*)']