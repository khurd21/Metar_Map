

#####################################
# Name: Kyle Hurd
# Date: 02/30/2021
# Project: Metar / Aviation Data
# File: display.py
# Tested: Python 3.7+
#####################################
import globals
import neopixel
import board as b
import time
from datetime import datetime


def _init_neopixel():
    '''Returns a NeoPixel object with LED info based on global variables'''
    is_bright:bool = globals.BEGIN_BRIGHTNESS < datetime.now().time() < globals.BEGIN_DIMMING
    return neopixel.NeoPixel(
            globals.LED_PIN, 
            globals.LED_COUNT, 
            brightness = (globals.BRIGHTNESS_LEVEL_DIM 
                if not is_bright
                else globals.BRIGHTNESS_LEVEL_DEF
                ),
            pixel_order = globals.LED_ORDER,
            auto_write = False
            )


def _init_iterations()->int:
    '''Returns number of iterations to occur based on global variables'''
    return (1
            if globals.USE_GUST_ANIMATION or globals.USE_LIGHTNING_ANIMATION
            else int(globals.BLINK_DURATION_SECONDS // globals.BLINK_FREQUENCY)
            )


def _toggle_flip_flop()->None:
    '''Inverts the flip flop which controls the blinking LEDs'''
    globals._FLIP_FLOP = not globals._FLIP_FLOP
    return


def _get_rgb_vfr(weather_conditions):
    '''Returns the rgb color based on vfr conditions'''
    return (globals.RGB_VFR
            if not (weather_conditions['is_lightning'] or weather_conditions['is_gusting'])
            else globals.RGB_LIGHTING if (weather_conditions['is_lightning'] and globals._FLIP_FLOP)
            else globals.RGB_VFR if (weather_conditions['is_gusting'] and globals._FLIP_FLOP)
            else globals.RGB_EMPTY
            )


def _get_rgb_mvfr(weather_conditions):
    '''Returns the rgb color based on mvfr conditions'''
    return (globals.RGB_MVFR
            if not (weather_conditions['is_lightning'] or weather_conditions['is_gusting'])
            else globals.RGB_LIGHTING if (weather_conditions['is_lightning'] and globals._FLIP_FLOP)
            else globals.RGB_MVFR if (weather_conditions['is_gusting'] and globals._FLIP_FLOP)
            else globals.RGB_EMPTY
            )


def _get_rgb_ifr(weather_conditions):
    '''Returns the rgb color based on ifr conditions'''
    return (globals.RGB_IFR
            if not (weather_conditions['is_lightning'] or weather_conditions['is_gusting'])
            else globals.RGB_LIGHTING if (weather_conditions['is_lightning'] and globals._FLIP_FLOP)
            else globals.RGB_IFR if (weather_conditions['is_gusting'] and globals._FLIP_FLOP)
            else globals.RGB_EMPTY
            )


def _get_rgb_lifr(weather_conditions):
    '''Returns the rgb color based on lifr conditions'''
    return (globals.RGB_LIFR
            if not (weather_conditions['is_lightning'] or weather_conditions['is_gusting'])
            else globals.RGB_LIGHTING if (weather_conditions['is_lightning'] and globals._FLIP_FLOP)
            else globals.RGB_LIFR if (weather_conditions['is_gusting'] and globals._FLIP_FLOP)
            else globals.RGB_EMPTY
            )


def get_led_color(weather_conditions):
    '''Determines flight category and returns rgb color based on given category'''
    if weather_conditions is None:
        return globals.RGB_EMPTY
    if weather_conditions['flight_category'] == 'VFR':
        return _get_rgb_vfr(weather_conditions)
    if weather_conditions['flight_category'] == 'MVFR':
        return _get_rgb_mvfr(weather_conditions) 
    if weather_conditions['flight_category'] == 'IFR':
        return _get_rgb_ifr(weather_conditions)
    if weather_conditions['flight_category'] == 'LIFR':
        return _get_rgb_lifr(weather_conditions)
    return globals.RGB_EMPTY


def drive_leds(conditions:dict, stations:list)->None:
    '''Cycles through each station ID and determines the color of rgb based on weather conditions.
    
    The stations and the rgbs are assigned incrementally, which means the first item in the
    stations list will be assigned to the first rgb in the string. If the station is titled
    NONE then the rgb assigned for that station will be left off. 
    '''
    pixel_list:list = _init_neopixel()
    num_iterations:int = _init_iterations()

    while num_iterations > 0:
        itr:int = 0
        for station in stations:
            if station == 'NONE':
                pixel_list[i] = globals.RGB_EMPTY
                itr += 1
                continue

            weather_conditions = conditions.get(station, None)

            color = get_led_color(weather_conditions)
            pixel_list[itr] = color
            itr += 1

        pixel_list.show()
        num_iterations -= 1
        _toggle_flip_flop()
        print('I made it')
        time.sleep(globals.BLINK_DURATION_SECONDS)
    return
