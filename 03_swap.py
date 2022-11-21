def swap():
    xxx, yyy = 400, 500
    print("before swap: ", xxx, yyy)

    tmp = xxx  # requires a temp var for swapping
    xxx = yyy
    yyy = tmp  # restore the value
    print("traditional swap: ", xxx, yyy)

    xxx, yyy = yyy, xxx  # swap in 1 line
    print("shortcut swap: ", xxx, yyy)


if __name__ == '__main__':
    swap()
