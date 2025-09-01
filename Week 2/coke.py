
due = 50
print(f"Amount Due: {due}")
while due > 0:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        due -= coin
    if due > 0:
        print(f"Amount Due: {due}")
print(f"Change Owed: {abs(due)}")