playerName=""
def manu(): 
    name()
    print("press enter on the option you want to select")
    new = input('')
    if new == "new game":
        print('test')
        #pot new game stats here
    elif new == "load game":
        #saves here
        #check if he has saves
        print('Test')
    else:
        print('yea i dear you to do it agian')
        manu()
def name():
    playerName = input('enter your name here ')
    if playerName == "guri":
        print('this name is alredy taken')
        name()
    if playerName == "sans":
        print('this name is alredy taken')
        name()
    if playerName == "pip":
        print('this name is alredy taken')

    

    if len(playerName) >= 10:
        print('wait thats to much')
        name()

        name()


manu()
