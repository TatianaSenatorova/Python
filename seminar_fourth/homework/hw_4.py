# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0
# просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random

k = int(input("enter a number of numbers: "))
polynomial = ''

for i in range(k, -1, -1):
   koef = (random.randint(-100, 100))
   if (koef == 0):
      polynomial = f"{polynomial}"
   elif (i == 0 and koef < 0):
      polynomial = f"{polynomial} {koef}"
   elif (i == 0):
      polynomial = f"{polynomial} + {koef}"
   elif (koef < 0):
      polynomial = f"{polynomial}  {koef} * X ^ {i}"
   elif (i == 1):
      polynomial = f"{polynomial} + {koef} * X "   
   else:
      polynomial = f"{polynomial} + {koef} * X ^ {i}"

polynomial = f'{polynomial} = 0'
print(polynomial)

with open('text.txt', 'w') as f:
  f.write(polynomial)
    
