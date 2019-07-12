"""
Circuit Playground Express
    https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts
    - Audio
    - LED
    - Buttons
    - NeoPixels
    - Analog In
    - Play wav file on internal speaker
"""
import time
import board
import neopixel
import microcontroller
from digitalio import DigitalInOut, Direction, Pull

from cpex.NeoPixelStrip import NeoPixelStrip
from cpex.AudioPlayer import AudioPlayer
from cpex.Button import Button
from cpex.analogInput import AnalogInput
from cpex.LightSensor import LightSensor

from analogio import AnalogIn
from simpleio import map_range

lightSensor = LightSensor()

analogInA1 = AnalogInput(board.A1)

audioPlayer = AudioPlayer()
audioPlayer.playTone([400, 500], 0.3).playTone([400, 500], 0.2).playTone([400, 500], 0.1)

MAX_NEO_PIXEL = 10
NEO_PIXEL_PIN = board.D8
print("NEO_PIXEL_PIN:%s" % (NEO_PIXEL_PIN)) 
neoPixelStrip = NeoPixelStrip(MAX_NEO_PIXEL, NEO_PIXEL_PIN, 0.01).fill((0, 0 ,0)).show().wait(.25)

LED = DigitalInOut(board.D13)
LED.direction = Direction.OUTPUT

# Buttons Definition
buttonA = Button(board.BUTTON_A)
buttonB = Button(board.BUTTON_B)
#slide = Button(board.D7)

rgbRed   = (255, 0, 0)
rgbGreen = (0, 180, 0)
rgbBlue  = (0, 0, 255)
rgbBlack = (0, 0, 0)
animationColors = [rgbRed, rgbGreen, rgbBlue, rgbBlack]
animationColorsSpeed = 0.05

class Program:

    def __init__(self):
        print('Initialization...')
        neoPixelStrip.animateColors(animationColors, animationColorsSpeed)

    def run(self):

        counter = 0

        while True:
            print("")
            neoPixelStrip.fill(rgbBlue if counter % 2 == 0 else rgbGreen).show()
            LED.value = not LED.value
            print("Led %s, count:%s" % (LED.value, counter))
            counter += 1
            # Buttons
            if buttonA.isPressed():
                print('button A down')
                audioPlayer.playFile("laugh.wav")
            if buttonB.isPressed():
                print('button B down')
                audioPlayer.playFile("rimshot.wav")

            # if slide.isPressed():
            #     print('Slide down')
            # else:
            #     print('Slide up')

            # ADC Read
            print("Analog Voltage: %6.2f" % analogInA1.readVoltage())

            # The temperature sensor is included in the mcu and is not accurate, try to correct the reading
            temperature = microcontroller.cpu.temperature - 5
            print("Temp: %fc %ff" % (temperature, (temperature)*1.8 + 32))

             # light value remaped to pixel position
            print("Light Sensor value:%f, peak:%s" % (lightSensor.value(), lightSensor.peakValue()))

            time.sleep(1)

Program().run()
