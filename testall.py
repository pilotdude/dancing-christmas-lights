import time
import Channels


def test():
    numChannels = 8
    activePins=['0','1','2','3','4','5','6','7']

    for each in activePins:
        a=Channels.Channel()
        a.chanOn()
    print("all channels on")

    time.sleep(2)
    for each in activePins:
        a=Channels.Channel()
        a.chanOff()

    print("all off")


    for each in activePins:
        a=Channels.Channel()
        a.setPin(mapDict[each])
        print(str(each)+"ON")
        a.chanOnFor(1)
        print(str(each)+"OFF")

    return
test()