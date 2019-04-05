import time
import board
from digitalio import DigitalInOut, Direction, Pull

class Button:
    def __init__(self, buttonBoard):
        self.button = DigitalInOut(buttonBoard)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.DOWN
    def isPressed(self):
        return self.button.value
