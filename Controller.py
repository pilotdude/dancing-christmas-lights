import RPi.GPIO as GPIO
import time
import multiprocessing





'''
print("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)
'''

#Command Data
leds = {'red':18,'yellow':23,'green':24,'blue':25}
redlist = [('on',1),('off',2),('on',1),('off',3),('on',3)]
bluelist = [('off',1),('on',2),('off',1),('on',3),('off',3)]
greenlist = [('on',2),('off',2),('on',2),('off',2),('on',2)]
yellowlist = [('on',1),('off',1),('on',1),('off',1),('on',1),('off',1),('on',1),('off',1),('on',1),('off',1)]
controllers = [('red',redlist), ('blue',bluelist), ('green',greenlist), ('yellow',yellowlist)]

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



