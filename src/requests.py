import requests

_url = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars' \
    '&requestType=retrieve' \
    '&format=xml' \
    '&hoursBeforeNow=5' \
    '&mostRecentForEachStation=true' \
    '&stationString='

def get(stations: list[str]):
    station_string = ','.join(stations)