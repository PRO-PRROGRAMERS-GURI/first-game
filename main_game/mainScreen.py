import time
print("hi, and wellcome to *game name*")
time.sleep(1)
print("our game is textbase so you need to type what you do")
time.sleep(1)
def mainScreen():
    print("wellcome to mew mew city here you can go to appliance job, school, home, gym, ikea, mcdonalds")
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
    elif GoTo == "gym":
        print("wellcome to:", GoTo)
        #gym system
    elif GoTo == "mcdonalds":
        print("wellcome to:", GoTo)
        #mcdonalds system.py
    elif GoTo == "ikea":
        print("wellcome to:", GoTo)
        #ikea system.py
    else:
        print("there is no place like that here")
        time.sleep(0.5)
        mainScreen()
mainScreen()