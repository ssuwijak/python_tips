# for else / while else

def find_tradit():
    search = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 7

    found = False
    for element in search:
        if element == target:
            print("the traget was found !")
            found = True
            break

    if not found:
        print("the target was not found !")


def find_tradit2():
    search = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 7

    found = False
    i = 0
    while i < len(search):
        element = search[i]
        if element == target:
            print("the traget was found !")
            found = True
            break

        i += 1

    if not found:
        print("the target was not found !")


def find_short():
    search = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 7

    for element in search:
        if element == target:
            print("the traget was found !")
            break
    else:
        print("the target was not found !")


if __name__ == '__main__':
    find_tradit()
