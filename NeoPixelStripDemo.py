import time
import board
from digitalio import DigitalInOut, Direction
import neopixel
from NeoPixelStrip import NeoPixelStrip

"""
dir(board)
    ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'SCK', 'MOSI', 'MISO', 'D0', 'RX', 'D1', 'TX', 'SDA', 'SCL', 
    'D5', 'D6', 'D9', 'D10', 'D11', 'D12', 'D13', 'I2C', 'SPI', 'UART']
"""

MAX_NEO_PIXEL = 12
neoPixelStrip = NeoPixelStrip(MAX_NEO_PIXEL, board.D5).fill((0, 0 ,0)).show().wait(1)

def rainbow_cycle(neoPixelStrip, allStrip = True, wait = 0.01):
    jWheelColorStep = 4
    for jWheelColorIndex in range(0, 256, jWheelColorStep):
        for pixelIndex in range(0, neoPixelStrip.num_pixels):
            if allStrip:
                color = neoPixelStrip.wheel((jWheelColorIndex) & 255)
            else:
                color = neoPixelStrip.wheel(
                    ((pixelIndex * 256 // neoPixelStrip.num_pixels) + jWheelColorIndex) & 255
                    )
            neoPixelStrip.setPixel(pixelIndex, color)
        neoPixelStrip.show()
        time.sleep(wait)

LED = DigitalInOut(board.D13)
LED.direction = Direction.OUTPUT

class Program:
    def __init__(self):
        print('__init__')

    def run(self):
        counter = 0
        #rainbow_cycle(neoPixelStrip, allStrip = True)
        #rainbow_cycle(neoPixelStrip, allStrip = False)
        rgbRed = (255, 0, 0)
        rgbGreen = (0, 255, 0)
        rgbBlue = (0, 0, 255)
        neoPixelStrip.fill(rgbBlue).show()
        while True:
            neoPixelStrip.fill(rgbBlue if counter % 2 == 0 else rgbGreen).show()
            LED.value = not LED.value
            print("Led %s, count:%s" % (LED.value, counter))
            counter += 1
            time.sleep(1)
# Main

p = Program()
p.run()
