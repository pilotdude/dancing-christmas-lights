import RPi.GPIO as GPIO
import time
import multiprocessing
import xml.etree.ElementTree as ET

#Midi to xml converter: http://flashmusicgames.com/midi/mid2xml.php

tree = ET.parse('StarWarsTheme.xml')
root = tree.getroot()



'''
print("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)
'''

#Command Data
leds = {'red1':18,'yellow1':23,'green1':24,'blue1':25,'red2':16,'green2':20, 'yellow2':12}
red1list = [('on',1),('off',2),('on',1),('off',3),('on',3)]
red2list = [('on',.5),('off',1),('on',2),('off',1),('on',3),('off',2),('on',.5)]
blue1list = [('off',1),('on',2),('off',1),('on',3),('off',3)]
green1list = [('on',2),('off',2),('on',2),('off',2),('on',2)]
green2list = [('on',.5),('off',1.5),('on',1),('off',1),('on',.5),('off',1.5),('on',1),('off',1),('on',1.5),('off',.5)]
yellow1list = [('on',1),('off',1),('on',1),('off',1),('on',1),('off',1),('on',1),('off',1),('on',1),('off',1)]
yellow2list = [('on',1),('off',1),('on',1),('off',1),('on',.5),('off',1.5),('on',1),('off',1),('on',1.5),('off',.5)]
controllers = [('red1',red1list), ('blue1',blue1list), ('green1',green1list), ('yellow1',yellow1list),
               ('red2',red2list),('green2',green2list),('yellow2',yellow2list)]

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for each in leds.values():
    GPIO.setup(each, GPIO.OUT)

def lightOn(pin, delay):
    '''Turns on a light at a given pin for a given interval'''
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin,GPIO.LOW)
    return

def control(color,controllist):
    for each in controllist:
        if each[0] == 'on':
            lightOn(leds[color],each[1])
        else:
            time.sleep(each[1])

if __name__ =='__main__':
    jobs =[]
    for each in controllers:
        p= multiprocessing.Process(target = control, args=(each[0],each[1]))
        jobs.append(p)
        p.start()



