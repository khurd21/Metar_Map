

#####################################
# Name: Kyle Hurd
# Date: 01/21/2021
# Project: Metar / Aviation Data
# File: globals.py
# Tested: Python 3.7+
####################################

import datetime as dt
import board
import neopixel


# LED Brightness Info
LOCATION = 'Seattle'
USE_DEFAULT_BRIGHT_DIM = False      # Use default sunrise sunset or use location based
BEGIN_BRIGHTNESS = dt.time(7,0)     # Default dimming time
BEGIN_DIMMING = dt.time(18,0)       # Default dimming time
BRIGHTNESS_LEVEL_DEF = 0.5          # Default brightness level between 0-1
BRIGHTNESS_LEVEL_DIM = 0.1          # Brightness level for night, between 0-1


# Blinking Info
BLINK_DURATION_SECONDS = 60         # Script will be run every minute (60 seconds)
BLINK_FREQUENCY = 1.0               # Frequency in which light will blind (seconds)
GUST_THRESHOLD = 10                 # LED will blind when gust exceeds this value
USE_LIGHTNING_ANIMATION = True      # LED will blink color assigned to lightning RGB
USE_GUST_ANIMATION = True           # LED will blink color assigned to gusts RGB

_FLIP_FLOP = True                   # Don't touch me, I toggle the LED on and off


# Locations of Needed Files
FILE_LOCATION = './files/airports'
URL_FOR_WEATHER = 'https://www.aviationweather.gov/adds/dataserver_current/' \
        'httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow' \
        '=5&mostRecentForEachStation=true&stationString='


# Led Configs 
LED_COUNT = 50
LED_PIN = board.D18
LED_ORDER = neopixel.GRB


# Colors
RGB_VFR         = (255,0,0)
RGB_MVFR        = (0,0,255)
RGB_IFR         = (0,255,0)
RGB_LIFR        = (0,125,125)
RGB_EMPTY       = (0,0,0)
RGB_LIGHTING    = (255,255,255)
