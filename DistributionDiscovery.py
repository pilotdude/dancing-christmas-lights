from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
import datetime
import pygame

#Trying to commit a change
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("KissMeBabe.mp3")
pygame.mixer.music.play()

class DataEntryApp(BoxLayout):
    numSamples = NumericProperty(0)
    #initializationTime = datetime.datetime()
    #sampleTimes=[initializationTime.now()]

    def newSample(self,*args):
        self.numSamples +=1
        #self.sampleTimes.append(datetime.timedelta(self.initializationTime,datetime.now()))

        #print(self.sampleTimes)
        return
    def doStuff(self):
        print("doing things")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("KissMeBabe.mp3")
        pygame.mixer.music.play()

class InitializationApp(App):
    def build(self):
        return DataEntryApp()









if __name__ == "__main__":
    print("running")
    InitializationApp().run()