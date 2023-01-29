while True:
    n = input("Введите число: ")
    if not n.isdigit():
        continue
    print("Простое" if not any(int(n) % i == 0 for i in range(2, int(n))) else "Не простое")
    break
