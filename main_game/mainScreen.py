import time
print("hi, and wellcome to *game name*")
time.sleep(1)
print("our game is textbase so you need to type what you do")
time.sleep(1)
def mainScreen():
    print("wellcome to mew mew city here you can go to appliance job, school, home, vet")
    GoTo=input("just type where you wana go ")
    if GoTo == "appliance job":
        print("wellcome to:", GoTo)
        #appliance job screen
    elif GoTo == "school":
        print("wellcome to:", GoTo)
        #school system
    elif GoTo == "home":
        print("wellcome to:", GoTo)
        #home system
    elif GoTo == "vet":
        print("wellcome to:", GoTo)
        #vet system
    else:
        print("there is no place like that here")
        time.sleep(0.5)
        mainScreen()
mainScreen()