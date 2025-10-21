def dec(f):
    def wrap():
        print('До вызова')
        res = f()
        print('После вызова')
        return res

    return wrap


@dec
def main():
    return 'Моя функция'


print(main())

st = "Просто строка"

st2 = "Просто еще одна строка"

