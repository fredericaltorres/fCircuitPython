import time
import board
from analogio import AnalogIn
from simpleio import map_range

class LightSensor:

    def __init__(self, pin = board.LIGHT):
        self.analogIn = AnalogIn(pin)

    def value(self):
        return self.analogIn.value

    def peakValue(self):
        return int( map_range(self.value(), 1000, 30000, 0, 10) )
