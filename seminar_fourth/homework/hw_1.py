# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

from decimal import Decimal

def NumPreсise (pi, precise):
    number = Decimal(f"{pi}")
    return number.quantize(Decimal(f"{precise}"))

pi = 3.14159265358979323846264
precise = float(input("Enter the required accuracy from 0.1 to : 0.0000000001:  "))
print(NumPreсise(pi, precise))



 
 