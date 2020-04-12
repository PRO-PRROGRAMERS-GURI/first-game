def mcdonalds(money):
    print("hi! and wellcome to mcdonalds do you wish to buy?")
    BUY=input("")
    if BUY == "yes":
        print ("""
        may i take your order?
        we have here:
        fryies -- 150
        burger -- 200
        meal -- 300
        happy meal -- 350
        """)
        Iwana=input("I want ")
        if Iwana =="fryies":
            print("you ate", Iwana)
            money = money-150
            eating = True
            mcdonalds(money)
        elif Iwana == "burger":
            print("you ate", Iwana)
            money = money-200
            eating = True
            mcdonalds(money)
        elif Iwana == "meal":
            print("you ate", Iwana)
            money = money-300
            eating = True
            mcdonalds(money)
        elif Iwana == "happy meal":
            print("you ate", Iwana)
            money = money-350
            eating = True
            happness = happness + 1
            mcdonalds(money)
        else:  
            print("we don't have that here")
            mcdonalds(money)
    elif BUY == "no":
        print("ok bye")
        #run main Screen
    else: print("plz select somefing from that we have here")
money=200
mcdonalds(money)