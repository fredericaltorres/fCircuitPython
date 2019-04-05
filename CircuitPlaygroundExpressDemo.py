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
from cpex.AudioPlayer import AudioPlayer
from cpex.Button import Button
from cpex.analogInput import AnalogInput

analogInA1 = AnalogInput(board.A1)

audioPlayer = AudioPlayer()
audioPlayer.playTone([400, 500]).playTone([400, 500])
audioPlayer.playFile("laugh.wav")
audioPlayer.playFile("rimshot.wav")

MAX_NEO_PIXEL = 10
neoPixelStrip = NeoPixelStrip(MAX_NEO_PIXEL, board.D8).fill((0, 0 ,0)).show().wait(.25)

LED = DigitalInOut(board.D13)
LED.direction = Direction.OUTPUT

# Buttons Definition
buttonA = Button(board.BUTTON_A)
buttonB = Button(board.BUTTON_B)

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

            print("Analog Voltage: %6.2f" % analogInA1.readVoltage())

Program().run()
