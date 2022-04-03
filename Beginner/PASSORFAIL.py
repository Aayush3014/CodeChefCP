for i in range(int(input())):
    x,n,p = map(int,input().split())
    l = x-n
    if ((n*3) + (l*-1))>=p:
        print("PASS")
    else:
        print("FAIL")