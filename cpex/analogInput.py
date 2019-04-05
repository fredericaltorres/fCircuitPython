# Readind ADC value
from analogio import AnalogIn

class AnalogInput:
    def __init__(self, pin, referenceVoltage = 3.3):
        self.referenceVoltage = referenceVoltage
        self.analogIn = AnalogIn(pin) 
    def readVoltage(self):
        return (self.analogIn.value * self.referenceVoltage) / 65536