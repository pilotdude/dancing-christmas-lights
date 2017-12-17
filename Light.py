# Class for each channel
import RPi.GPIO as GPIO
import time
import threading

class light:
    def __init__(self,channel,duration):
        '''if the duration is negative the lights will turn off if the duration is positive they lights will turn on for
        the duration in seconds If the duration is 0 they will turn on indefinately.'''
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(channel, GPIO.OUT)
        self.pinNum = channel
        if duration > 0:
            self.chanOnFor(duration)
        if duration < 0:
            self.chanOff()
        else:
            self.chanOn()
        return

    def chanOnFor(self,duration):
        #print("Channel:"+str(self.pinNum)+"duration:"+str(duration))
        self.chanOn()
        t = threading.Timer(duration, self.chanOff)
        t.start()  # after 30 seconds, unban will be run
        return

    def chanOn(self):
        '''Turns the lights on this channel to on'''
        GPIO.output(self.pinNum, GPIO.HIGH)
        return

    def chanOff(self):
        '''Turns the lights on this channel off'''
        GPIO.output(self.pinNum, GPIO.LOW)
        #print(time.gmtime())
        self.isOn = False
        return

    def setPin(self, pin):
        self.pinNum = pin
        return




