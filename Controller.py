import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)

def lightOn(pin, delay):
    '''Turns on a light at a given pin for a given interval'''
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin,GPIO.LOW)
    return

alist = [('on',1),('off',2),('on',1),('off',3),('on',4)]
for each in alist:
    if each[0] == 'on':
        lightOn(18,each[1])
    else:
        time.sleep(each[1])
