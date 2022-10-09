# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from random import choice

with open('polinomial1.txt', "r", encoding="utf-8") as f1, \
        open("polinomial2.txt", "r", encoding="utf-8") as f2:
        first = f1.readlines()
        second = f2.readlines()

with open("sum.txt", "a", encoding="utf-8") as f3:
                for i, v in enumerate(first):
                    f3.write(f"{v[:-5]} + {second[i]}")
      
