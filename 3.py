things_to_pack = {'палатка': 5 , 'угли': 2 , 'еда': 10, 'чай в термосе': 3, 'куртка': 1, 'салфетки': 2, 'аптечка': 2 }
P = int(input("P = "))
sorted_things_to_pack = dict(sorted(things_to_pack.items(), key = lambda y: -y[1]))
for x, z in sorted_things_to_pack.items():
    if z <= P:
        print(x, sep = "/n")
        P -= z