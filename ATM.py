withdraw,balance = (input()).split(" ")
withdraw = int(withdraw)
balance = float(balance)

if withdraw % 5 == 0 and withdraw < balance:
    Lbalance = balance - (withdraw + 0.50)
    print(Lbalance)
elif withdraw>balance:
    print(balance)


