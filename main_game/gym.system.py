money = 200
fitness = 0
def gym(money, fitness):
    ask = input('''
    
    want to work out?
    
    
    
    
    ''')

    if ask == 'yes':
        money = money - 100
        fitness = fitness + 1
        print('you have', fitness, 'fitness and', money, 'money left')
        gym(money, fitness)

    else:
        print('ok')
        #put menu()
gym(money, fitness)