def dismiss(tabel_number):
    with open('employee_base.txt', 'r', encoding='utf-8') as eb:
        old_base = eb.read()
    old_base = old_base.split('\n')
    with open('employee_base.txt', 'w', encoding='utf-8') as eb:
        for i in range(len(old_base)):
            if old_base[i].split(' ')[0] == tabel_number:
                continue
            elif i == len(old_base) - 1:
                eb.write(f'{old_base[i]}')
            else:
                eb.write(f'{old_base[i]}\n')
    with open('login_database.txt', 'r', encoding='utf-8') as ld:
        ld_old_base = ld.read()
    ld_old_base = ld_old_base.split('\n')
    with open('login_database.txt', 'w', encoding='utf-8') as ld:
        for i in range(len(ld_old_base)):
            if ld_old_base[i].split(' ')[0] == tabel_number:
                continue
            elif i == len(ld_old_base) - 1:
                ld.write(f'{ld_old_base[i]}')
            else:
                ld.write(f'{ld_old_base[i]}\n')
