def anticheat(money, time, job, salery):
    while money <= 0:
        if job != 'none':
            if time != 0:
                time = time - 1
                money = money + salery
                print('you were in debt ')
            if job == 'none':
                print('you died')
            if time <= 0:
                print('you died')
    
anticheat(money, time, job, salery)


