def zip_ex():
    names = ['joe', 'jane', 'bill', 'tom']
    ages = [21, 19, 18, 43]
    hairs = ['black', 'bronde', 'brown', 'black', 'test']

    print(list(zip(names, ages)))
    print(list(zip(names, hairs)))
    print(list(zip(names, ages, hairs)))  # skip for extra members

    for name, age in zip(names, ages):
        if age > 20:
            print(name, age)

        print('-' * 20)

    for name, age, hair in zip(names, ages, hairs):
        if age > 20:
            print(name, age)
        print(hair)


if __name__ == '__main__':
    zip()
