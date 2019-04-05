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
from digitalio import DigitalInOut, Direction, Pull
import neopixel
from cpex.NeoPixelStrip import NeoPixelStrip
from cpex.AudioPlayer import AudioPlayer
from cpex.Button import Button
from cpex.analogInput import AnalogInput
import microcontroller

from analogio import AnalogIn
from simpleio import map_range
analogLightSensor = AnalogIn(board.LIGHT)

analogInA1 = AnalogInput(board.A1)

audioPlayer = AudioPlayer()
audioPlayer.playTone([400, 500], 0.5).playTone([400, 500], 0.3)

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
rgbBlack = (0, 0, 0)

class Program:
    def __init__(self):
        print('Initialization...')
        neoPixelStrip.animate(rgbRed, .05).wait(.5)
        neoPixelStrip.animate(rgbBlack, .05).wait(.5)

    def run(self):
        counter = 0

        while True:
            #neoPixelStrip.fill(rgbBlue if counter % 2 == 0 else rgbGreen).show()
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

            print("Analog Voltage: %6.2f" % analogInA1.readVoltage())
            # The temperature sensor is included in the mcu and is not accurate, try to correct the reading
            temperature = microcontroller.cpu.temperature-5
            print("Temp: %fc %ff" % (temperature, (temperature)*1.8+32))

             # light value remaped to pixel position
            analogLightSensorValue = analogLightSensor.value
            peak = map_range(analogLightSensorValue, 1000, 30000, 0, 10)
            print("Light Sensor AnalogValue:%f, Peak:%s" % (analogLightSensorValue, int(peak)))

            time.sleep(1)

Program().run()
