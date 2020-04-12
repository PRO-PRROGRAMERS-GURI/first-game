def time():
    time = 8
    sleep = input('''how much you wanna sleep
    
    1.2h

    2.4h

    3.6h

    4.8h

    
    
    
    ''')

    if sleep == '2h':
        time = 2
        print('you have two turns')
    elif sleep == '4h':
        time = 4
        print('you have 4 turns')
    elif sleep == '6h':
        time = 6
        print('you have 6 turns')
    elif sleep == 8:
        time = 8
        print('you have ful turns 8') 

    else:
        print('try agian')
        time()
time()
