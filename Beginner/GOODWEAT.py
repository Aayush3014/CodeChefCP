from itertools import count


a = list(map(int,input().split()))
count1 = 0
count0 = 0
for i in a:
    if i == 1:
        count1+=1
    else:
        count0 += 1
if count1>count0:
    print("YES")
else:
    print("NO")