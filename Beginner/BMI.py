for i in range(int(input())):
    m,h = map(int,input().split())
    if (m/(h*h))<=18:
        print(1)
    elif (m/(h*h))<=24:
        print(2)
    elif (m/(h*h))<=29:
        print(3)
    elif (m/(h*h))>=30:
        print(4)