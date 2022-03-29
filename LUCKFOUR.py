#for i in range(int(input())):
number = int(input())
count = 0
while number>0:
    rem = number%10
    if rem == 4:
        count+=1
        number = number//10
    else:
        number = number//10
print(count)