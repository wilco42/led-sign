#!/usr/bin/env python
import time
import sys
import glob

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

def get_cards():
    files = glob.glob('./cards/*.png')
    return files

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
# with pwm slowdown to 4 seems to work well for RPi0
options.gpio_slowdown = 4
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

try:
    while True:
        cards = get_cards()
        for card in cards:
            image = Image.open(card)
            image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
            matrix.SetImage(image.convert('RGB'))
            time.sleep(10)
except KeyboardInterrupt:
    sys.exit(0)
