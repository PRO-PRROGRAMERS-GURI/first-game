x = 5
time = 8
progress = 0
level = 1
intelegence = 0
def learn(progressF, timeLeft,x, level, intelegence):
    awnser=input("wana learn? ")
    if awnser == "yes":
        progressF = progressF + 1
        timeLeft = timeLeft - 1
        print('progress:',progressF,'/5', 'time left:',timeLeft) 
        if progressF == x:
            progressF = 0
            x = x + 2
            level = level + 1
            intelegence = intelegence + 1
            print('good job intelegence',intelegence,' and school level', level)
            learn(progressF, timeLeft,x, level, intelegence)
        
    else:
        print('go to menu')
        #dispenser = menu() put dispenser here
learn(progress, time,x, level, intelegence)








