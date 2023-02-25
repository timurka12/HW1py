S0 = 0

S1 = float(input("Внесите сумму: "))

if S1 % 50 == 0:
    print("Операция выполняется")
else:
    print("Некорректная сумма")

S2 =  float(input("Какую сумму хотите снять: "))

if S2 <= S1:
        if S1 <= 2000:
            S1 = S1 - S2 - 30
            print(S1)
        elif S1 > 2000 and S1 <= 40000:
            S1 = S1 - S2 - 0.015 * S2
            print(S1)
        elif S1 > 40000 and S1 < 5000000:
            S1 = S1 - S2 - 600
            print(S1)
        elif S1 >=5000000:
            S1 = S1 - 0.1*S1 - 600
            print(S1)
        else:
            print("Ошибка")







