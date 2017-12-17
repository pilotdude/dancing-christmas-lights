import time
import Light

mapDict = {'0':4,'1':17,'2':27,'3':22,'4':5,'5':6,'6':13,'7':19,'8':26,'9':21,'10':20,'11':16,'12':12,'13':25,'14':24,
          '15':23,'16':18}
activePins=['0','1','2','3','4','5','6','7']


def testAll():
    print("All ON")
    for each in activePins:
        Light.light(mapDict[each],5)

    print("All OFF")
    return

def allOn():
    print("All ON")
    for each in activePins:
        Light.light(mapDict[each],0)
    return

def allOff():
    print("All OFF")
    for each in activePins:
        Light.light(mapDict[each],-1)
    return
