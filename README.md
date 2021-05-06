# Metar Weather Map

Welcome to the METAR Weather map.

This program pulls weather data from the aviationweather.gov website and displays the weather information to LEDs for a personal METAR weather map. 

# Requirements

- You will need Python3.7+
- You will need VirtualEnv already installed (pip3 install virtualenv)
- You will need a Raspberry Pi. I used the Zero W which has enough power to run the script and has wifi!
- You will need WS281x type LEDs [anything compatible with neopixel]

# Setup

Desgined for Raspberry Pi. Make sure the data wire is connected to GPIO 18 and use the 5 volt or 3 volt connection depending on the leds requirements.

- Type 'make install' in the base directory of project. This will install all needed modules for project inside of a virtual environment.
- Type 'make run' in the base directory of project. This will execute the code.
- A script is given to help with running a crontab. If you want to have the script run every 5 minutes, you can write the following code snippet in the terminal:

```
sudo crontab -e
*/5 * * * * /home/pi/<absolute_path>/run_bot.sh
```
