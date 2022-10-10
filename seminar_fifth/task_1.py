#Создайте список из N натуральных чисел. Среди чисел не хватает одного, чтобы выполнялось
# условие A[i] - 1 = A[i - 1]. Найдите это число
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 10] ответ 9

from  random import choice

def fill_list(N: int):
    list_nums = [x for x in range(N + 1)]
    list_nums.remove(choice(list_nums))
    return list_nums

def find_miss_element(list_1: list):
    for i in range(1, len(list_1)):
        if list_1[i] - 1 != list_1[i - 1]:
            miss_el = list_1[i] - 1                         
            return miss_el 
    return -1

list_1 = (fill_list(int(input("enter N: "))))
print(list_1)
print(f" missed element {find_miss_element(list_1)}")