#Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#минимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
import math

N = int(input('enter size of list: '))

def FillList(N):   #заполняем список
    list = []
    for i in range(N):
         list.append(random.uniform(0, 100))
         list[i] = round(list[i], 2)                             
    return list

def ListWithoutIntPart(list_1, N): #заполняем новый список без целой части чисел
    new_list = []
    for i in range(N):
        new_list.append(list_1[i] - int(list_1[i]))
        new_list[i] = round(new_list[i], 2)  
    return new_list

def DifferenceMinMax(new_list):  #находим разницу между мин и мак элементами
    min = new_list[0]
    max = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] < min:
            min = new_list[i]
        if new_list[i] > max:
             max = new_list[i]
    dif = max - min
    return dif


list_1 = (FillList(N))
print(f"List of float numbers {list_1}")
new_list_1 = ListWithoutIntPart(list_1, N)
print(f"List of numbers without int part {new_list_1}")
print(f"Difference between max and min {DifferenceMinMax(new_list_1)}")
