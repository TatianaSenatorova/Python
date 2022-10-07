#Задайте натуральное число N. Напишите программу,
#которая составит список простых множителей числа N.


def simple_nums(num):
    list_of_simple_nums = []
    divisor  = 2
    while num > 1:
        if num % divisor == 0:
            list_of_simple_nums.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return list_of_simple_nums

num = int(input("enter any integer number: "))
print(simple_nums(num))
    