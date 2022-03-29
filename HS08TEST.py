n,m = map(float,input().split())
n = int(n)
if (n+0.50<=m) and (n%5 == 0):
    print(float(m-(n+0.50)))
else:
    print(m)