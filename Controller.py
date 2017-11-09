#import RPi.GPIO as GPIO
import time
import multiprocessing
import pygame
import xml.etree.ElementTree as ET
import Channels
import Light
import re

a=Channels.Channel()
a.chanOn()
a.chanOff()

#key = channel id, value = BCMGPIO port
mapDict = {'0':4,'1':17,'2':27,'3':22,'4':5,'5':6,'6':13,'7':19,'8':26,'9':21,'10':20,'11':16,'12':12,'13':25,'14':24,
          '15':23,'16':18}

def test():
    numChannels = 7
    activePins=[12,23,24,25,16,20]

    #Create a list of each channel
    chanList = [Channels.Channel() for i in range(numChannels)]
    i=0
    while i < numChannels:
        chanList[i].setPin(activePins[i])
        i+=1

    return chanList


def readSong(songFile):
    '''reads a song file and returns a list with channel, position and duration indicators'''

    playCommands =[] #holds the position, channel and duration of each light on period

    #reading data out of file
    a=open(songFile,'r')
    midiText = a.readline()
    sections = re.findall("{\"color\":[0-9]+,\"position\":([0-9]+)(.+?(?<=}\]}))",midiText)

    #Converting that data into a useful list
    for each in sections:
        notes = re.findall("\"note\":([0-9]+).+?(?<=position\":)([0-9.]+),\"length\":([0-9.]+)",each[1])
        for thing in notes:
            print(thing)
            note = int(thing[0])-12 #to bring things down an octave
            pos = float(thing[1])+float(each[0]) #get absolute position instead of realative position
            len = float(thing[2])

            #changing things to put position first, then note, then length
            playCommands.append((pos,note,len))

    #sorting by order of occurance
    playCommands.sort()

    return playCommands

readSong("test1.sng")

def danceLights(playCommands,mapDict):
    '''Accepts a list of tuples with position, note and duration and a dictionary to map notes to
    channels, turns on pins at specified position for given duration'''
    i = 0
    while i<=len(playCommands):
        channel = mapDict[str(playCommands[i][1])]
        duration = playCommands[i][2]
        Light.light(channel,duration)
        i+=1


def playMusic():
    song = 'StarWarsTheme' #set this equal to the name of the song you want to capture without the file extension
    #Plays the song
    pygame.init()
    pygame.mixer.music.load("KissMeBabe.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)
#playMusic()



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
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# for each in leds.values():
#     GPIO.setup(each, GPIO.OUT)
#
# def lightOn(pin, delay):
#     '''Turns on a light at a given pin for a given interval'''
#     GPIO.output(pin,GPIO.HIGH)
#     time.sleep(delay)
#     GPIO.output(pin,GPIO.LOW)
#     return
#
# def control(color,controllist):
#     for each in controllist:
#         if each[0] == 'on':
#             lightOn(leds[color],each[1])
#         else:
#             time.sleep(each[1])
#
# if __name__ =='__main__':
#     jobs =[]
#     for each in controllers:
#         p1= multiprocessing.Process(target = control, args=(each[0],each[1]))
#         jobs.append(p1)
#         p1.start()
#     p2 = multiprocessing.Process(target = playMusic)
#     p2.start()



