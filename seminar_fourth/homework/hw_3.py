# #Задайте последовательность цифр. Напишите программу, которая выведет список
# неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from itertools import count
from operator import index
import random
import re

def list_nums(number: int):
    list_numbers = []
    for i in range(number):
        list_numbers.append(random.randint(0, 10))
    return list_numbers 

def non_recurring_nums(list_numbers: list):
   occur = []
   count = len(list_numbers) - 1
   index = 0
   while(index != count):
        for i in range(1, count):
            if list_numbers[index] == list_numbers[i]:
                occur.append(list_numbers[index])
            index +=1
        else:
            index +=1
             
        
            
   return occur
               
list_numbers = list_nums(int(input("enter a number of numbers: ")))
print(list_numbers)
print(non_recurring_nums(list_numbers))