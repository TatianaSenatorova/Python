#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

N = int(input('enter size of list: '))

def FillList(N):   #заполняем список
    list = []
    for i in range(N):
         list.append(random.randint(-100, 100))
    return list

def SummUnevenNumsIndex(list_1, N): #находим сумму элементов с нечетными индексами
    sum = 0
    for i in range(1, N, 2):
         sum += list_1[i]
    return sum

list_1 = (FillList(N))
print(list_1)
print(f"Summ numbers on uneven positions {SummUnevenNumsIndex(list_1, N)}")

