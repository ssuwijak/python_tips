def unpacking():
    tup = (1, 2, 3, 4, 5)
    a, b, c, d, e = tup  # unpack tuple to variables
    print(a, b, c, d, e, type(tup))

    lst = list(tup)  # create a list from a tuple by the list constructor
    a, b, c, d, e = lst  # unpack list to variables (requires member match)
    print(a, b, c, d, e, type(lst))

    string = 'hello'
    a, b, c, d, e = string  # unpack a string to variables
    print(a, b, c, d, e, type(string))

    dic = {"aaa": 99, "bbb": 88}
    a, b = dic  # unpack keys of a dict to variables (requires member matching)
    print(a, b, type(dic))

    a, b = dic.items()  # unpack dictionary to variables
    print(a, b, type(dic))

    a, b = dic.values()  # unpack values of a dictionary to variables (requires member matching)
    print(a, b, type(dic))

    coords = [4, 5]
    x, y = coords  # unpack a list to variables (requires member match)
    print(x, y, type(coords))


if __name__ == '__main__':
    unpacking()
