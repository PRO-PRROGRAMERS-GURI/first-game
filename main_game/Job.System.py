intelegens = 0
fitness = 0
def jobsystem():
    job_apply = input('want a job? ')
    if job_apply == 'yes':
        job = input('''
        What job do you want


        1.gym worker(requries fitness 1)

        2.teacher(requires intelegens 2)

        3.film star

        4.game develepor(requires intelegens 3)

        5.vet(requires intelegens 1)


        ''')
    if job == "gym worker":
        if fitness == 1:
            print('you are now a gym worker')
        if fitness <= 1:
            print('you do not have enogh fitness')
        if fitness >= 1:
            print('you are now a gym worker')
    elif job == 'teacher':
        if intelegens == 2:
            print('you are now a teacher')
        if intelegens <= 2:
            print('go learn kid you are not smart enogh')
        if intelegens >= 2:
            print('you are now a teacher')
    elif job == 'film star':
        print('you are now a film star')
    elif job == 'game develepor':
        if intelegens == 3:
            print('you are now a game develepor')
        if intelegens <= 3:
            print('go learn kid you are not smart enogh')
        if intelegens >= 3:
            print('you are now a develepor')
        if intelegens == 2:
            print('you cant be a game develepor but you can be a teacher')
    elif job == "vet":
        if intelegens == 1:
            print('you are now a vet')
        if intelegens <= 1:
            print('go learn kid you are not smart enogh')
        if intelegens >= 1:
            print('you are now a vet')
    else:
        print('try agian no job like that or you used capslock it wouldnt')
        jobsystem()


jobsystem()


