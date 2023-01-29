print("Стороны:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

if a == b and b == c and a == c:
    print("Треугольник равносторонний")
elif a == b or b == c or c == a:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторнний")

