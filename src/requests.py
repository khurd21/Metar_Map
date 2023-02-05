from dataclasses import dataclass
from datetime import datetime
import xml.etree.ElementTree as ElementTree
import requests
from urllib3 import HTTPResponse

_url = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars' \
    '&requestType=retrieve' \
    '&format=xml' \
    '&hoursBeforeNow=5' \
    '&mostRecentForEachStation=true' \
    '&stationString='

_metar_weather_tag = 'METAR'
_flight_category = 'flight_category'
_observation_time = 'observation_time'
_temp_c = 'temp_c'
_dewpoint_c = 'dewpoint_c'
_lightning = 'LTG'


@dataclass
class MetarWeatherStation:

    raw_text: str
    station_id: str
    observation_time: datetime

    temp_celsius: float
    dewpoint_celsius: float
    precipitation_inches: float
    elevation_meters: float
    visibility_statute_miles: float
    altimeter_in_hg: float

    wind_direction_degrees: int
    wind_speed_knots: int
    wind_gust_knots: int

    _lightning: int
    _gust_threshold: int = 10

    def __init__(self):
        pass

    def is_gusting(self) -> bool:
        return (self.wind_gust_knots - self.wind_speed_knots) > self._gust_threshold

    def is_lightning(self) -> bool:
        return self._lightning != -1


def get_metar_weather(stations: list[str]) -> list[MetarWeatherStation]:
    station_string = ','.join(stations)
    response: HTTPResponse = requests.get(f'{_url}{station_string}')
    reports = ElementTree \
        .fromstring(response.data.decode('utf-8')) \
        .iter(_metar_weather_tag)

    for report in reports:
        pass
