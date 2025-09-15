names = ["Meera", "Sam","Kalu","Juli"]
bills = [10,20,100,60]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")