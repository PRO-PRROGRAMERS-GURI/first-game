load=""
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
        #has probleme
        name = input('enter your name here ')
        if name == "guri":
            print('this name is alredy taken')
            name()
        if name == "sans":
            print('this name is alredy taken')
            name()
        if name == "pip":
            print('this name is alredy taken')
            name()
manu()