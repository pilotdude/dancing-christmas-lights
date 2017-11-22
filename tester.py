import RPi.GPIO as GPIO
import time
mapDict = {'0':4,'1':17,'2':27,'3':22,'4':5,'5':6,'6':13,'7':19,'8':26,'9':21,'10':20,'11':16,'12':12,'13':25,'14':24,
          '15':23,'16':18}

i=0
GPIO.setmode(GPIO.BCM)
#print(mapDict[str(0)])
while i<= len(mapDict):

    GPIO.setup(mapDict[str(i)], GPIO.OUT)
    GPIO.output(mapDict[str(i)], GPIO.HIGH)

    time.sleep(.5)
    GPIO.output(mapDict[str(i)], GPIO.LOW)
    i+=1