"""
    https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
"""
import board
import digitalio
import storage

#
# See output in file boot_out.txt
#

print('boot.py - start')

# For Gemma M0, Trinket M0, Metro M0/M4 Express, ItsyBitsy M0/M4 Express
# switch = digitalio.DigitalInOut(board.D2)
switch = digitalio.DigitalInOut(board.D5)  # For Feather M0/M4 Express
# switch = digitalio.DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

if switch.value == False:
    print('Pin D5 is grounded, authorize write mode')
else:    
    print('Pin D5 is high, read mode mode only')
 
# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", switch.value)

print('boot.py - done')
