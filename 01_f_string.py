def f_string():
    # F strings
    x = 11
    y = [44, 'Hi', False]
    z = 'Hello'

    print(x, y, z)

    print("{} {} {}".format(x, y, z))
    print("{}-{}-{}".format(x, y, z))

    print(f'{x} {y} {z}')
    print(f'{x}-{y}-{z}')


if __name__ == '__main__':
    f_string()
