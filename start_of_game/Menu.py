import time
def manu(): 
    #selection of type
    print("enter New game, Credits, Quit(caps required for all of them)")
    selective = input('')
    #new game | starts the game
    if selective == "New game":
        newGame()
        backstory()
        name()
        #Credits | shows Credits
    elif selective == "Credits":
        print('''
        Thanks for downloading this game
        --From--
        Guri
        Assaf
        Gilad
        ''')
        manu()
    #Quit | crashes the game
    elif selective == "Quit":
        print('BUH BYE GAME')
    #if its not quit credits or new game | Debuger
    else:
        print('yea i dare you to do it agian')
        manu()
#backstory
defalt_time = 3
#defalt_time is the time btween prints
def backstory():
    print("so you are a man who lived at zolmak city all his life untill you reched the age of 18... ")
    time.sleep(defalt_time)
    print("then you left your family to have a fresh start...")
    time.sleep(defalt_time)
    print("you reched mew mew city after using almost all your saving...")
    time.sleep(defalt_time)
    #backStory() just print the back story with "defalt_time" as the time btween prints
    # you can add to the backStoy as much as you want 
#Name system
def name():
    playerName = str(input('enter your name here '))
    if playerName == "guri":
        print('this name is alredy taken')
        name()
    if playerName == "sans":
        print('this name is alredy taken')
        name()
    if playerName == "pip":
        print('this name is alredy taken')
    else:
        print('your name is,', playerName)

    

    if len(playerName) >= 10:
        print('wait thats to much')
        name()
#new game
def newGame():
    nomey = 200
    happiness = 0
    education = 0
    fitness = 0
    playerName=""
    playerJob='nothing'
    stuff = ""
    playerName=""

        


manu()
