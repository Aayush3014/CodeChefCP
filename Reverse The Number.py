for i in range(int(input())):
    a=int(input())
    rev=0
    while a>0:
        d=a%10
        a=a//10
        rev=rev*10+d
    print(rev)
    