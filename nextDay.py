import time
def nextDay():
    time = 8
    #defalt of time is False
    if eating == False:
        time = time - 2
        print("you forgot to eat!")
        #forgot to eat system?
    if time <= 8 or time < 0 :
        print("game is dead")
        time.sleep(3)
        #anti cheat system
eating = False
#defalt of eating is False
nextDay()