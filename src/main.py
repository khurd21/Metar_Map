#!/usr/bin/env python3

#####################################
# Name: Kyle Hurd
# Date: 01/21/2021
# Project: Metar / Aviation Data
# File: main.py
# Tested: Python 3.7+
####################################
import globals
import metar
import xml.etree.ElementTree as element_tree
import leds


def main():
    metar.get_sunrise_sunset()
    airports:list[str] = metar.get_airports(globals.FILE_LOCATION)
    content = metar.get_web_data(airports)

    # conditions (dict), stations (list[str])
    conditions, stations = metar.get_weather_condition(element_tree.fromstring(content))
    print(f'{conditions}\n')
    print(f'{stations}\n\n')

    for station in stations:
        for x in conditions[station]['sky_conditions']:
            print(f'Cover: {x["cover"]} @ {x["cloud_base_ft_agl"]} ft')
        print(f'Flight Category: {conditions[station]["flight_category"]}')

    leds.drive_leds(conditions, stations)
    return

if __name__ == '__main__':
    main()
