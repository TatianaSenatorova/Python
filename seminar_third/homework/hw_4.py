#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

num = int(input('enter any number: '))
num_str = ''
while (num / 2 > 0):
    num_str = str(num % 2) + num_str
    num //= 2
binary_num = int(num_str)
print(f"binary number is {binary_num}")
