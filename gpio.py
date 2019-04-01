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

class Program:
    def __init__(self):
        print('__init__')

    def run(self):        
        while True:
            LED.value = not LED.value
            print("Led %s" % (LED.value))
            time.sleep(1)
# Main

p = Program()
p.run()
