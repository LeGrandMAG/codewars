def square_digits(num):

    v = str(num)
    listt = []
    for i in v:
        r = (int(i))
        r = r*r
        listt.append(r)
    l=''
    for x in listt:
        l= l + str(x)
    print(int(l))
square_digits(9119)
