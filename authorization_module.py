def authorization(login, password):
    with open('login_database.txt', 'r', encoding='utf-8') as lb:
        for line in lb:
            lst = line.replace('\n', '').split(' ')
            if lst[0] == login:
                if lst[1] == password:
                    return 1
        print('Пара логин и пароль введена неверно')
        return 0
