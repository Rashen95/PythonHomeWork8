import dismissal_module as dm
import list_of_exployee_module as loem
import dismiss_checker_module as dcm
import salary_checker as sc
import salary_change_module as scm


def managerial_module(tabel_number):
    with open('employee_base.txt', 'r', encoding='utf-8') as eb:
        for line1 in eb:
            lst1 = line1.replace('\n', '').split(' ')
            if lst1[0] == tabel_number:
                with open('managerial_positions.txt', 'r', encoding='utf-8') as manpos:
                    for line2 in manpos:
                        lst2 = line2.replace('\n', '').split(' ')
                        if lst1[4] == lst2[0]:
                            print(f'Ваша должность {" ".join(lst2[1:])}')
                            while True:
                                print('Функционал вашего меню:\n'
                                      '1. Узнать свою зарплату\n'
                                      '2. Уволиться\n'
                                      '3. Уволить сотрудника\n'
                                      '4. Изменить сотруднику ЗП\n'
                                      '5. Вывести список сотрудников\n'
                                      '6. Завершить работу с базой')
                                choise = input('Выберите нужный пункт меню: ')
                                if choise == '1':
                                    print(f'Ваша зарплата равна {lst1[5]} рублей')
                                elif choise == '2':
                                    print('Вы уволены')
                                    dm.dismiss(tabel_number)
                                    break
                                elif choise == '3':
                                    print('Список всех сотрудников: ')
                                    loem.list_module()
                                    while True:
                                        dismiss_pos = input('Введите табельный номер для увольнения сотрудника: ')
                                        if dcm.check(dismiss_pos) == 1:
                                            dm.dismiss(dismiss_pos)
                                            print(f'Сотрудник с табельным номером {dismiss_pos} уволен')
                                            break
                                        else:
                                            print('Введен неверный табельный номер')
                                elif choise == '4':
                                    print('Список всех сотрудников: ')
                                    loem.list_module()
                                    while True:
                                        change_pos = input('Введите табельный номер для изменения ЗП: ')
                                        if sc.check_sal(change_pos) == 1:
                                            scm.change(change_pos)
                                            print(f'Зарплата сотрудника с табельным номером {change_pos} изменена')
                                            break
                                        else:
                                            print('Введен неверный табельный номер')
                                elif choise == '5':
                                    loem.list_module()
                                elif choise == '6':
                                    break
