import globals
import board as b
import leds

pixel_list: list = leds._init_neopixel()

for pixel in pixel_list:
    pixel = globals.RGB_EMPTY

pixel_list.show()

