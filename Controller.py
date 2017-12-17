#import RPi.GPIO as GPIO
import time
import multiprocessing
import pygame
import xml.etree.ElementTree as ET

import Light
import re
import threading

# https://chrome.soundation.com/


#key = channel id, value = BCMGPIO port
mapDict = {'0':4,'1':17,'2':27,'3':22,'4':5,'5':6,'6':13,'7':19,'8':26,'9':21,'10':20,'11':16,'12':12,'13':25,'14':24,
          '15':23,'16':18}


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
            note = int(thing[0])-12 #to bring things down an octave
            pos = float(thing[1])+float(each[0]) #get absolute position instead of realative position
            len = float(thing[2])

            #changing things to put position first, then note, then length
            playCommands.append((pos,note,len))
            # (1, 2, 5),(3,1,3),(
    #sorting by order of occurance
    playCommands.sort()

    return playCommands

def danceLights(playCommands,mapDict, song):
    '''Accepts a list of tuples with position, note and duration and a dictionary to map notes to
    channels, turns on pins at specified position for given duration'''
    i = 0
    playMusic(song)
    print("Playing the song")
    time.sleep(.65)
    print('Dancing the lights!!!!')
    while i<len(playCommands):
        #print(playCommands[i])
        #print(playCommands[i+1])
        channel = mapDict[str(playCommands[i][1])]
        duration = playCommands[i][2]
        Light.light(channel,duration/44100)
        if i>0 and i+1<len(playCommands):
            amount = playCommands[i+1][0]-playCommands[i][0]
            if amount >0:
                time.sleep(amount/44100)
            else:
                pass
        else:
            pass
        i+=1

def playMusic(song):
    '''Accepts the file name of a song as a string and then plays that song.'''
    #Plays the song
    #time.sleep(.25)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy():
        #pygame.time.wait(1000)

pygame.init()
songlist = readSong("test1.sng")

danceLights(songlist, mapDict, "KissMeBabe.mp3")
#Delay to help fix timing issue
#t = threading.Timer(.03, playMusic("KissMeBabe.mp3"))
#t.start()
#playMusic("KissMeBabe.mp3")
