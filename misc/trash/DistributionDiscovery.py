import xml.etree.ElementTree as ET
import pygame

#Midi to xml converter: http://flashmusicgames.com/midi/mid2xml.php

song = 'StarWarsTheme' #set this equal to the name of the song you want to capture without the file extension
'''
#Plays the song
pygame.init()
pygame.mixer.music.load(song+".mid")
pygame.mixer.music.play()
'''

tree = ET.parse(song+'.xml')
root = tree.getroot()
#text is between the wrapppers
#Attrib is what it is equal too
#tag is what it's called
for child in root:
    if child.tag == "TicksPerBeat":
        tpb = child.text #ticks per beat
    if child.tag == "Track":
        for event in child:

            print(event[0].text, event[1].attrib)
print(tpb)
#shouldn't be needed in final code just here while code is running too fast
#while pygame.mixer.music.get_busy():
#    pygame.time.wait(1000)