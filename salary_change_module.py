def change(tabel_number):
    while True:
        salary = input('Какую зарплату сделать данному сотруднику: ')
        if salary.isdigit():
            break
        else:
            print('Неверное значение')
    with open('employee_base.txt', 'r', encoding='utf-8') as eb:
        old_base = eb.read()
    old_base = old_base.split('\n')
    for i in range(len(old_base)):
        if old_base[i].split(' ')[0] == tabel_number:
            old_base[i] = " ".join(old_base[i].split(' ')[:5]) + f' {salary}'
    with open('employee_base.txt', 'w', encoding='utf-8') as eb:
        for i in range(len(old_base)):
            if i == len(old_base) - 1:
                eb.write(f'{old_base[i]}')
            else:
                eb.write(f'{old_base[i]}\n')
