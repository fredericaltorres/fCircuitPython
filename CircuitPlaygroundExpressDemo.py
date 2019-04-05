"""
Circuit Playground Express
    https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts

    - Audio
    - LED
    - Buttons
    - NeoPixels
    - Analog In
"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel
from cpex.NeoPixelStrip import NeoPixelStrip
from cpex.cpAudioPlayer import cpAudioPlayer
from cpex.cpButton import cpButton

cpAudioPlayer().playTone([400, 500]).playTone([400, 500])

MAX_NEO_PIXEL = 10
neoPixelStrip = NeoPixelStrip(MAX_NEO_PIXEL, board.D8).fill((0, 0 ,0)).show().wait(.25)

LED = DigitalInOut(board.D13)
LED.direction = Direction.OUTPUT

# Buttons Definition
buttonA = cpButton(board.BUTTON_A)
buttonB = cpButton(board.BUTTON_B)

# Readind ADC value
from analogio import AnalogIn
analogInA1 = AnalogIn(board.A1)
 
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

rgbRed   = (255, 0, 0)
rgbGreen = (0, 180, 0)
rgbBlue  = (0, 0, 255)

class Program:
    def __init__(self):
        print('Initialization...')
        neoPixelStrip.animate(rgbRed, .05).wait(1)

    def run(self):
        counter = 0

        while True:
            neoPixelStrip.fill(rgbBlue if counter % 2 == 0 else rgbGreen).show()
            LED.value = not LED.value
            print("Led %s, count:%s" % (LED.value, counter))
            counter += 1
            time.sleep(.3)
            # Buttons
            if buttonA.isPressed():
                print('button A down')
            if buttonB.isPressed():
                print('button B down')

            print("Analog Voltage: %6.2f" % getVoltage(analogInA1))

Program().run()

