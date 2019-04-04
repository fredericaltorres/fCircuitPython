import time
import board
from digitalio import DigitalInOut, Direction
import neopixel
from NeoPixelStrip import NeoPixelStrip

MAX_NEO_PIXEL = 12
neoPixelStrip = NeoPixelStrip(MAX_NEO_PIXEL, board.D5).fill((0, 0 ,0)).show().wait(.25)

def rainbow_cycle(neoPixelStrip, allStrip = True, wait = 0.01):
    wheelColorStep = 4
    for wheelColorIndex in range(0, 256, wheelColorStep):
        for pixelIndex in range(0, neoPixelStrip.num_pixels):
            if allStrip:
                color = neoPixelStrip.wheel((wheelColorIndex) & 255)
            else:
                color = neoPixelStrip.wheel( ((pixelIndex * 256 // neoPixelStrip.num_pixels) + wheelColorIndex) & 255 )
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
        rgbRed      = (255, 0, 0)
        rgbGreen    = (0, 255, 0)
        rgbBlue     = (0, 0, 255)
        neoPixelStrip.animate(rgbRed, .05).wait(1)
        while True:
            neoPixelStrip.fill(rgbBlue if counter % 2 == 0 else rgbGreen).show()
            LED.value = not LED.value
            print("Led %s, count:%s" % (LED.value, counter))
            counter += 1
            time.sleep(1)

# Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Program().run()

