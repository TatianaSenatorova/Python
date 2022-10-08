# #Задайте последовательность цифр. Напишите программу, которая выведет список
# неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random

def list_nums(number: int):
    list_numbers = []
    for i in range(number):
        list_numbers.append(random.randint(0, 10))
    return list_numbers 

def non_recurring_nums(list_numbers: list):
    new_list = []
    for i in range(len(list_numbers)):
        flag = 1
        for j in range(len(list_numbers)):
            if list_numbers[i] == list_numbers[j] and i != j:
                flag = 0
                break
        if flag:
             new_list.append(list_numbers[i]) 
    return new_list

list_numbers = list_nums(int(input("enter a number of numbers: ")))
print(list_numbers)
print(non_recurring_nums(list_numbers))