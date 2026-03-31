import RPi.GPIO as GPIO
from config import RELAY_LIGHT, RELAY_FAN

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_LIGHT, GPIO.OUT)
GPIO.setup(RELAY_FAN, GPIO.OUT)

def light_on():
    GPIO.output(RELAY_LIGHT, GPIO.HIGH)

def light_off():
    GPIO.output(RELAY_LIGHT, GPIO.LOW)

def fan_on():
    GPIO.output(RELAY_FAN, GPIO.HIGH)

def fan_off():
    GPIO.output(RELAY_FAN, GPIO.LOW)

def cleanup():
    GPIO.cleanup()
