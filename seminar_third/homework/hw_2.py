#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import random

N = int(input('enter size of list: '))

def FillList(N):   #заполняем список
    list = []
    for i in range(N):
         list.append(random.randint(-100, 100))
    return list

def Multiply(list_1, N): #находим произведения пар чисел и записываем их значения в новый список
    new_list = []
    i = 0
    while(i < N / 2):
         new_list.append(list_1[i] * list_1[N - 1 - i])
         i += 1
    return new_list

list_1 = (FillList(N))
print(list_1)
print(f"Multiply pairs of numbers {Multiply(list_1, N)}")
