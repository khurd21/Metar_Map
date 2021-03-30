# Metar Weather Map

Welcome to the METAR Weather map.

This program pulls weather data from the aviationweather.gov website and displays the weather information to LEDs for a personal METAR weather map. 

# Requirements

- You will need Python3.7+
- You will need VirtualEnv already installed (pip3 install virtualenv)

# Setup

Desgined for Raspberry Pi. You may need 'sudo' permission to properly access the LEDs. I am still trying to find a workaround to avoid this issue.

- Type 'make install' in the base directory of project. This will install all needed modules for project inside of a virtual environment.
- Type 'make run' in the base directory of project. This will execute the code.
