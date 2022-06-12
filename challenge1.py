##This function take a number find the square if  each number

##for example if the input is "9119"  the result will be 811181
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
