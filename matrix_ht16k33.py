import time
import board
from digitalio import DigitalInOut, Direction

"""
dir(board)
    ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'SCK', 'MOSI', 'MISO', 'D0', 'RX', 'D1', 'TX', 'SDA', 'SCL', 
    'D5', 'D6', 'D9', 'D10', 'D11', 'D12', 'D13', 'I2C', 'SPI', 'UART']
"""

LED = DigitalInOut(board.D13)
LED.direction = Direction.OUTPUT

import busio
# requires lib adafruit_ht16k33, adafruit_bus_device
# How to search for source of library https://github.com/search?q=org%3Aadafruit+adafruit_ht16k33
from adafruit_ht16k33 import matrix 
matrix = matrix.Matrix8x8(busio.I2C(board.SCL, board.SDA), address=0x70, auto_write=False)
matrix.brightness = 15

def matrixGo():
    matrix.fill(0)
    for r in range(8):
        for c in range(8):
            matrix[r, c] = 1
            matrix.show()
            time.sleep(0.03)

class Program:
    def __init__(self):
        print('__init__')

    def run(self):
        matrixGo()
        while True:
            LED.value = not LED.value
            print("Led %s" % (LED.value))
            time.sleep(1)
# Main

p = Program()
p.run()
