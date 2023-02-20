import fractions

a = int(input("a = "))
b = int(input("b =  "))

c = int(input("c = "))
d = int(input("d = "))

one = fractions.Fraction(a, b)
two = fractions.Fraction(c, d)

print('{} + {} = {}'.format(one, two, one + two))
print('{} + {} = {}'.format(one, two, one * two))
