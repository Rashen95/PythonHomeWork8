def list_module():
    with open('employee_base.txt', 'r', encoding='utf-8') as eb:
        base = eb.read()
        base = base.split('\n')
        for i in range(len(base)):
            base[i] = base[i].split(' ')[:4]
        for i in base:
            print(" ".join(i))
