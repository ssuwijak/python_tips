
def comprehensions():
    # traditional for style
    tradit = []
    for i in range(9):
        tradit.append(i)
    print(tradit)

    # short for style
    short = [i for i in range(9)]
    print(short)

    # short for style to assign value
    short_assign = [0 for i in range(9)]
    print(short_assign)

    # short for style with conndition
    short_cond = [i for i in range(20) if i % 2 == 0]
    print(short_cond)

    # nest short for
    short_nest = [i*j for i in range(10) for j in range(3)]
    print(short_nest)

    # char count
    sentence = "hello, how are you today ?"
    dic = {ch: sentence.count(ch) for ch in set(sentence)}
    print(dic)


if __name__ == '__main__':
    comprehensions()
