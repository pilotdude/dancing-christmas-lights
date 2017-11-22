# Class for each channel
import RPi.GPIO as GPIO
import time

class light:
    def __init__(self,channel,duration):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)
        self.pinNum = channel
        self.chanOnFor(duration)
        return

    def chanOnFor(self,duration):
        self.chanOn()
        time.sleep(duration)
        self.chanOff()
        return

    def chanOn(self):
        '''Turns the lights on this channel to on'''
        GPIO.output(self.pinNum, GPIO.HIGH)
        self.isOn = True
        return

    def chanOff(self):
        '''Turns the lights on this channel off'''
        GPIO.output(self.pinNum, GPIO.LOW)
        self.isOn = False
        return

    def setPin(self, pin):
        self.pinNum = pin
        return




