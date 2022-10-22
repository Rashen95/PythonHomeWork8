import authorization_module as am
import constructor_functionality_module as cfm
import managerial_functionality_module as mfm
examination = 0
login = None
password = None
while examination != 1:
    login = input('Введите логин, он соответствует табельному номеру работника: ')
    password = input('Введите пароль: ')
    examination = am.authorization(login, password)
with open('employee_base.txt', 'r', encoding='utf-8') as eb:
    for line in eb:
        lst = line.replace('\n', '').split(' ')
        if lst[0] == login:
            print(f'Вы авторизовались как {lst[1]} {lst[2]} {lst[3]}')
            if 0 <= int(lst[4]) <= 4:
                cfm.constructor_module(login)
            elif 5 <= int(lst[4]) <= 7:
                mfm.managerial_module(login)
            else:
                print('3')
