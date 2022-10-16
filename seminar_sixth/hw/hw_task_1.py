# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from  random import choice, choices
import random

def fill_list(size: int):
    list_nums = choices(range(1, size * 2), k = size)
    return  list_nums

def fill_new_list(new_list: list):
    my_list = [new_list[i + 1] for i in range(len(new_list) - 1) if new_list[i] < new_list[i + 1]]
    return my_list
    
new_list = fill_list(int(input("enter a number of numbers: ")))
print(new_list)
list_1 = fill_new_list(new_list)
print(list_1)
