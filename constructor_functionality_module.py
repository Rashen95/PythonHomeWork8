import dismissal_module as dm


def constructor_module(tabel_number):
    with open('employee_base.txt', 'r', encoding='utf-8') as eb:
        for line1 in eb:
            lst1 = line1.replace('\n', '').split(' ')
            if lst1[0] == tabel_number:
                with open('employee_positions.txt', 'r', encoding='utf-8') as epos:
                    for line2 in epos:
                        lst2 = line2.replace('\n', '').split(' ')
                        if lst1[4] == lst2[0]:
                            print(f'Ваша должность {" ".join(lst2[1:])}')
                            while True:
                                print('Функционал вашего меню:\n'
                                      '1. Узнать свою зарплату\n'
                                      '2. Уволиться\n'
                                      '3. Завершить работу с базой')
                                choise = input('Выберите нужный пункт меню: ')
                                if choise == '1':
                                    print(f'Ваша зарплата равна {lst1[5]} рублей')
                                elif choise == '2':
                                    print('Вы уволены')
                                    dm.dismiss(tabel_number)
                                    break
                                elif choise == '3':
                                    break
