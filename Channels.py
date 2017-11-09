# Class for each channel
import RPi.GPIO as GPIO
import time

class Channel:
    def __init__(self):
        self.pinNum = 0
        self.isOn = False
        return

    def __str__(self):
        if self.isOn:
            return str(self.pinNum)+" is on"
        else:
            return str(self.pinNum)+" is off"

    def chanOnFor(self,time):
        self.chanOn()
        time.sleep(time)
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




