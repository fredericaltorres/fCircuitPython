import time
import board
from digitalio import DigitalInOut, Direction
import neopixel

class NeoPixelStrip:
    """
        Adafruit sample
            https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_simpletest.py
        NubioMCU sample 
            https://github.com/madeintheusb/NusbioMCU/blob/master/NusbioPixelConsole/Program.cs
    """
    def __init__(self, num_pixels, pin = board.D5):
        self.pixel_pin = pin; # Pin require PWM
        self.num_pixels = num_pixels
        self.ORDER = neopixel.GRB
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER)
    def wheel(self,pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos*3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos*3)
            g = 0
            b = int(pos*3)
        else:
            pos -= 170
            r = 0
            g = int(pos*3)
            b = int(255 - pos*3)
        return (r, g, b) if self.ORDER == neopixel.RGB or self.ORDER == neopixel.GRB else (r, g, b, 0)
    def fill(self, color):
        self.pixels.fill(color)
        return self
    def show(self):        
        self.pixels.show()
        return self
    def wait(self, duration):
        time.sleep(duration)
        return self
    def setPixel(self, index, color):
        self.pixels[index] = color
        return self
