---- Finding the shortest route between two stations in Singapore MRT Lines ----

----A) Installing Dependencies and Running the program----
1) Install dependency virtualenv using pip
	MACOS: python3 -m pip install --user virtualenv
	WINDOWS: py -m pip install --user virtualenv
2) Create a virtual environment 
	MACOS: python3 -m venv env
	WINDOWS: py -m venv env
3) Activate virtual environment
	MACOS: source env/bin/activate
	WINDOWS: .\env\Scripts\activate
4) Download dependencies from requirements.txt file
	pip install -r requirements.txt
5) Run the server
	MACOS: python -m flask run
	WINDOWS: python app.py
6) Deactivating the virtual environment 
	deactivate

----B) Running tests----
1) Go to the root directory of the folder and run 
	pytest test.py

----C) Assumptions----
1) The user is expected to enter the start and end stations as query parameters (GET Request)
	e.g. http://127.0.0.1:5000/path?start=Bugis&end=Yew+Tee
2) The station names with spaces in between are expected to be seperated by a '+' sign (as shown above)
3) If the user does not enter the date in the url, today's date and time is set by default (GMT time)
4) The shortest path with least time has been calculates using Dijkstra's algorithm with time as the weights in the graph
5) URL with time as the parameter looks like below, 
	e.g. http://127.0.0.1:5000/path?date=2019-01-31T04:00&start=Bugis&end=Yew+Tee 
6) The data of the station names is stored in the Data folder with the name "StationMap.csv"
7) Trains are assumed to run in both directions

NOTE: Both the original as well as the bonus tasks have been implemented
