def check(login):
    with open('employee_base.txt', 'r', encoding='utf-8') as eb:
        for line in eb:
            lst = line.replace('\n', '').split(' ')
            if 0 <= int(lst[4]) <= 4:
                if lst[0] == login:
                    return 1
            else:
                print('Вы не можете увольнять руководителей')
                return 0
        return 0
