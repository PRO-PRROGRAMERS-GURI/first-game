money = 200#delete when import
happines = 0
job = 'nothing'
ask = input('do you want to buy at idea(gives happines)')
def ikea(ask, money, happines):
    
    if ask == 'yes':
        ikea =  input('''
        
        1.cups(70)

        2.pillow(100)

        3.mirror(50)

        4.couch(50)

        5.table(50)

        6.candle(20)

        7.kitchen(200)

        8.bed(400)

        9.clothet(1400)

        10.towl(200)

        11.drawer(500)

        12.kids(3000)
        
        13.chair(400)

        14.meatballs(1000)

        ''')
        if ikea == 'cups':
            money = money - 70
            happines = happines + 7
        elif ikea == 'pillow':
            money = money - 100
            happines = happines + 10
        elif ikea == 'mirror':
            money = money - 50
            happines = happines + 5
        elif ikea == 'picture':
            money = money - 50
            happines = happines + 5
        elif ikea == 'couch':
            money = money - 900
            happines = happines + 90
        elif ikea == 'table':
            money = money - 700
            happines = happines + 70
        elif ikea == 'chair':
            money = money - 400
            happines = happines + 40
        elif ikea == 'candle':
            money = money - 20
            happines = happines + 2
        elif ikea == 'kitchen':
            money = money - 2000
            happines = happines + 200
        elif ikea == 'bed':
            money = money - 400
            happines = happines + 40
        elif ikea == 'clothet':
            money = money - 1400
            happines = happines + 140
        elif ikea == 'towl':
            money = money - 200
            happines = happines + 20
            print('advencment complete Magevet?? MAGEVET')
        elif ikea == 'drawr':
            money = money - 500
            happines = happines + 50
        elif ikea == 'kids':
            money = money - 3000
            happines = happines + 300
            print('advencment complete Buy Kids You bought kids at idea(ikea) LOL')
        elif ikea == 'meatballs':
            money = money - 1000
            happines = happines + 100
            print('advencment complete MEAT BALLS you little swidish boy')
        else:
            print('try agian')
            ikea()
    else:
        print('ok')
    
ikea(ask, money, happines)


def anticheat():
    import time
    while money <= 0:
        print('test')
        #call jobsystem()
        if job == "nothing":
            print('You Died')
            time.sleep(5)


    