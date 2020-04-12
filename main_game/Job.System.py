intelegens = 0
fitness = 0
xp = 0
time = 8
def jobsystem(time_left):
    job_apply = input('want a job? ')
    time = time_left
    if job_apply == 'yes':
        time = time - 1
        job = input('''
        What job do you want


        1.gym worker(requries fitness 1)

        2.teacher(requires intelegens 2)

        3.film star

        4.game develepor(requires intelegens 3)

        5.vet(requires intelegens 1)


        ''')
    if job == 'film star':
        print('you are now a film star')
    elif job == "gym worker":
        if fitness >= 1 and  xp >= 25:
            print('you are now a gym worker')
        if fitness < 1:
            print('you do not have enogh fitness')
        if  xp < 25:
            print("you don't have enogh work xp")
    elif job == "vet":
        if xp >= 100 and intelegens >= 1:
            print('you are now a vet')
        if intelegens < 1:
            print('go learn kid you are not smart enogh')
        if xp < 100:
            print("you don't have enogh work xp")            
    elif job == 'teacher':
        if intelegens >= 2 and xp >= 200:
            print('you are now a teacher')
        if intelegens < 2:
            print('go learn kid you are not smart enogh')
        if xp < 200:
            print("you don't have enogh work xp")
    elif job == 'game develepor':
        if xp >= 500 and intelegens >= 3:
            print('you are now a game develepor')
        if intelegens < 3:
            print('go learn kid you are not smart enogh')
        if intelegens == 2:
            print('you cant be a game develepor but you can be a teacher')
        if xp < 500:
            print("you don't have enogh work xp")
    else:
        print('try agian no job like that or you used capslock it wouldnt')
        jobsystem(8)


jobsystem(8)


