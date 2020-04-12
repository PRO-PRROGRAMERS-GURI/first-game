job = ""
def work():
    if job == "gym worker":
        money = money + 150
        xp = xp + 2
        time = time - 1
    if job == 'teacher':
        money = money + 300
        xp = xp + 6
        time = time - 1
    if job == 'film star':
        money = money + 100
        xp = xp + 1
        time = time - 1
    if job == 'game develepor':
        money = money + 450
        xp = xp + 10
        time = time - 1
    if job == "vet":
        money = money + 200
        xp = xp + 4
        time = time - 1
    else:
        print('you have no job')
