#Дан список чисел. создайте список, в который попадают числа, описывающие
# возрастающую последовательность. Порядок элементов менять нельзя.
#[10, 0, 5, 11, 6, 11, 15, 10]
#[[10, 11, 15], [0, 5, 11, 15], [5, 11, 15], [11, 15], [6, 15], [1, 15]]

from  random import choice, choices
import random

def fill_list(size):
    list_nums = choices(range(1, size * 2), k = size)
    return  list_nums

def fill_new_list(new_list: list):
    my_list = []
    for i in range(len(new_list)):
        f = new_list[i]
        list_1 = [f]
        for x in range(i + 1, len(new_list)):
                if new_list[x] > f:
                     f = new_list[x]
                     list_1.append(f)
        if len(list_1) > 1:
            my_list.append(list_1)
    return  my_list   
    
new_list = fill_list(int(input("enter a number of numbers: ")))
print(new_list)
new_list_1 = fill_new_list(new_list)
print(new_list_1)
