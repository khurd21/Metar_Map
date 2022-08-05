from os import getcwd
from urllib3 import HTTPResponse, PoolManager
import logging

BASE_DIR = getcwd()
logging.basicConfig(
    filename=f'{BASE_DIR}/logs/metar.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    )

MOST_RECENT_FOR_EACH_STATION: bool = True

BASE_URL: str = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars' \
    '&requestType=retrieve' \
    '&format=xml' \
    '&hoursBeforeNow=5' \
    '&mostRecentForEachStation=true' \
    '&stationString=kshn'

logging.info(f'Set the BASE_URL to:\n{BASE_URL}')

http: PoolManager = PoolManager()

response: HTTPResponse = http.request('GET', BASE_URL)

print(type(response))
print(response.status)

value: str = response.data.decode('utf-8')
print(type(value))
print(value)

val = True
print(f'VALUE TRUE: {str(val).lower()}')