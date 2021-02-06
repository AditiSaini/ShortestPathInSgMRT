import pytest
import requests

#Test 1) Tests for status codes
def test_statusCode_successRequest():
    "GET request to url returns a 200"
    url = 'http://127.0.0.1:5000/path?start=Bugis&end=Yew+Tee'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_statusCode_failedRequest():
    "GET request to url returns a 404 because of inavlid station name"
    url = 'http://127.0.0.1:5000/path?start=Bugis&end=Yew+Teee'
    resp = requests.get(url)
    assert resp.status_code == 404

#Test 2) Test for content type in header
def test_contentType_successRequest():
    url = 'http://127.0.0.1:5000/path?start=Bugis&end=Yew+Tee'
    response = requests.get(url)
    assert response.headers['Content-Type'] == "application/json"

#Test 3) Tests for invalid user input
def test_userInput_invalidStationName():
    url = 'http://127.0.0.1:5000/path?start=Bugis&end=Yew+Teee'
    resp = requests.get(url)
    response_body = resp.json()
    assert response_body == "Invalid Station Names"

def test_userInput_invalidTime():
    url = 'http://127.0.0.1:5000/path?date=2019-01-31T004:00&start=Bugis&end=Yew+Tee'
    resp = requests.get(url)
    response_body = resp.json()
    assert response_body == "Invalid Time"

def test_userInput_invalidDate():
    url = 'http://127.0.0.1:5000/path?date=20019-01-31T04:00&start=Bugis&end=Yew+Tee'
    resp = requests.get(url)
    response_body = resp.json()
    assert response_body == "Invalid Date"

#Test 4) Tests for valid user input
def test_userInput_validInputWithoutTime():
    url = 'http://127.0.0.1:5000/path?start=Holland+Village&end=Bugis'
    resp = requests.get(url)
    response_body = resp.json()
    assert response_body == [
    "Take CC line from Holland Village to Farrer Road",
    "Take CC line from Farrer Road to Botanic Gardens",
    "Change from CC line to DT line",
    "Take DT line from Botanic Gardens to Stevens",
    "Take DT line from Stevens to Newton",
    "Take DT line from Newton to Little India",
    "Take DT line from Little India to Rochor",
    "Take DT line from Rochor to Bugis",
    "In total it will take approximately 70 minutes during NON-PEAK and DAY hours"
]

def test_userInput_validInputPeakHour():
    url = 'http://127.0.0.1:5000/path?date=2019-01-31T06:00&start=Holland+Village&end=Bugis'
    resp = requests.get(url)
    response_body = resp.json()
    assert response_body == [
    "Take CC line from Holland Village to Farrer Road",
    "Take CC line from Farrer Road to Botanic Gardens",
    "Change from CC line to DT line",
    "Take DT line from Botanic Gardens to Stevens",
    "Take DT line from Stevens to Newton",
    "Take DT line from Newton to Little India",
    "Take DT line from Little India to Rochor",
    "Take DT line from Rochor to Bugis",
    "In total it will take approximately 85 minutes during PEAK hours"
]

def test_userInput_validInputNightHour():
    url = 'http://127.0.0.1:5000/path?date=2019-01-31T04:00&start=Holland+Village&end=Bugis'
    resp = requests.get(url)
    response_body = resp.json()
    #DT line stops working at night, hence the change in route
    assert response_body == [
    "Take CC line from Holland Village to Buona Vista",
    "Change from CC line to EW line",
    "Take EW line from Buona Vista to Commonwealth",
    "Take EW line from Commonwealth to Queenstown",
    "Take EW line from Queenstown to Redhill",
    "Take EW line from Redhill to Tiong Bahru",
    "Take EW line from Tiong Bahru to Outram Park",
    "Take EW line from Outram Park to Tanjong Pagar",
    "Take EW line from Tanjong Pagar to Raffles Place",
    "Take EW line from Raffles Place to City Hall",
    "Take EW line from City Hall to Bugis",
    "In total it will take approximately 110 minutes during NIGHT hours"
]

def test_userInput_validInputDayHour():
    url = 'http://127.0.0.1:5000/path?date=2019-01-31T13:00&start=Holland+Village&end=Bugis'
    resp = requests.get(url)
    response_body = resp.json()
    #DT line stops working at night, hence the change in route
    assert response_body == [
    "Take CC line from Holland Village to Farrer Road",
    "Take CC line from Farrer Road to Botanic Gardens",
    "Change from CC line to DT line",
    "Take DT line from Botanic Gardens to Stevens",
    "Take DT line from Stevens to Newton",
    "Take DT line from Newton to Little India",
    "Take DT line from Little India to Rochor",
    "Take DT line from Rochor to Bugis",
    "In total it will take approximately 70 minutes during NON-PEAK and DAY hours"
]