#btw this code do not work

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
        mainScreen()

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
        print('advencment complete name alredy taken')
        name()
    if playerName == "sans":
        print('this name is alredy taken')
        print('advencment complete name alredy taken')
        name()
    if playerName == "pip":
        print('this name is alredy taken')
        print('advencment complete name alredy taken')
    else:
        print('your name is,', playerName)

    

    if len(playerName) >= 10:
        print('wait thats to much')
        name()
import time
time.sleep(1)
def mainScreen():
    if time == 0:
        nextDay()
    else:
        print("hi, and wellcome to YOU only live once")
        print('----------------------------------------')
        time.sleep(1)
        print("our game is textbase so you need to type what you do")
        print("wellcome to mew mew city here you can go to appliance job, school, home, vet")
        GoTo=input("just type where you wana go ")
        if GoTo == "appliance job":
            print("wellcome to:", GoTo)
            jobsystem(time, intelegens, xp, fitness)
        elif GoTo == "school":
            print("wellcome to:", GoTo)
            #school system
        elif GoTo == "home":
            print("wellcome to:", GoTo)
            #home system
        elif GoTo == "ikea":
            print("wellcome to:", GoTo)
            #ikea system
        elif GoTo == "mctrump":
            print("wellcome to:", GoTo)
            #mctrump system
        else:
            print("there is no place like that here")
            time.sleep(0.5)
            mainScreen()
def newGame():
    time = 8
    nomey = 200
    happiness = 0
    intelegens = 0
    fitness = 0
    playerName=""
    playerJob='nothing'
    stuff = ""
    xp = 0
def jobsystem(time, intelegens, xp, fitness):
    job_apply = input('want a job? ')
    if job_apply == 'yes':
        job = input('''
        What job do you want


        1.gym worker(requries fitness 1)

        2.teacher(requires intelegens 2)

        3.film star

        4.game develepor(requires intelegens 3)

        5.vet(requires intelegens 1)


        ''')

    if job_apply == 'no':
        mainScreen()
    if job == 'film star':
        print('you are now a film star')
        mainScreen()
    elif job == "gym worker":
        mainScreen()
        if fitness >= 1 and  xp >= 25:
            print('you are now a gym worker')
            mainScreen()
        if fitness < 1:
            print('you do not have enogh fitness')
            mainScreen()
        if  xp < 25:
            print("you don't have enogh work xp")
            mainScreen()
    elif job == "vet":
        if xp >= 100 and intelegens >= 1:
            print('you are now a vet')
            mainScreen()
        if intelegens < 1:
            print('go learn kid you are not smart enogh')
            mainScreen()
        if xp < 100:
            print("you don't have enogh work xp")        
            mainScreen()    
    elif job == 'teacher':
        if intelegens >= 2 and xp >= 200:
            print('you are now a teacher')
            mainScreen()
        if intelegens < 2:
            mainScreen()
            print('go learn kid you are not smart enogh')
        if xp < 200:
            print("you don't have enogh work xp")
            mainScreen()
    elif job == 'game develepor':
        if xp >= 500 and intelegens >= 3:
            mainScreen()
            print('you are now a game develepor')
        if intelegens < 3:
            print('go learn kid you are not smart enogh')
        if intelegens == 2:
            print('you cant be a game develepor but you can be a teacher')
            mainScreen()
        if xp < 500:
            print("you don't have enogh work xp")
            mainScreen()
    else:
        print('try agian no job like that or you used capslock it wouldnt')
        jobsystem(time)
def nextDay():
    time = 8
    eating = False
    #defalt of eating is False
    if eating == False:
        time = time - 2
        print("you forgot to eat!")
        #forgot to eat system?
    if time <= 8 or time < 0 :
        print("game is dead")
        time.sleep(3)
        #anti cheat system

manu()
