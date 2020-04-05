playerName=""
def manu(): 
    name()
    print("press enter on the option you want to select")
    new = input('')
    if new == "new game":
        print('test')
        #put here start thing
    elif new == "load game":
        #saves here
        #check if he has saves
        print('Test')
def name():
        while playerName != 'guri' or 'sans' or 'pip':
            name = input('enter your name here ')
            if name == "guri":
                print('this name is alredy taken')
            if name == "sans":
                print('this name is alredy taken')
            if name == "pip":
                print('this name is alredy taken')
manu()