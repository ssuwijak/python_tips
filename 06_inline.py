def inline():
    # c# style x = 2 > 3 ? False:True

    # traditional form
    if 2 > 3:
        x = "2 > 3"
    else:
        x = "2 <= 3"
    print(x)

    # inline form
    y = "2 > 3" if 2 > 3 else "2 <= 3"
    print(y)


if __name__ == '__main__':
    inline()
