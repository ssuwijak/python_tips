def func1(a1, a2, a3):
    print(a1, a2, a3)


def func2(a1=None, a2=None, a3=None):
    print(a1, a2, a3)


if __name__ == '__main__':
    func1(111, 222, 333)  # traditional

    args = [1, 2, 3]
    func1(args[0], args[1], args[2])  # traditional
    func1(a1=111, a3=333, a2=222) # specific
    func1(*args)  # short to unpack
    print(*args)  # try to print *args


    kwargs = {'a2': 2, 'a3': 3, 'a1': 1, }
    func2(*kwargs) # pass the keys
    func2(**kwargs) # pass the values

