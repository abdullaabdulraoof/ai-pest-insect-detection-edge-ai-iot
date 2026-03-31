import smbus
from apds9960 import APDS9960
from apds9960.const import *

bus = smbus.SMBus(1)
apds = APDS9960(bus)

apds.enableGestureSensor()

def read_gesture():
    if apds.isGestureAvailable():
        motion = apds.readGesture()
        return motion
    return None
