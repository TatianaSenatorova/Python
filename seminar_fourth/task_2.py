#Найти корни уравнения 2*x**2 + 4*x + 2 = 0
#Уравнение считываем из файла

import math

# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))

path = r"file2.txt"
with open(path) as f:
    read = f.readline()
print(read)

str_nums = read.split(sep='+')
print(str_nums)
a = str_nums[0][0]
b = str_nums[1][0]
c = str_nums[2][0]

print(a, b, c, sep = '  ')   
a = int(a)
b = int(b)
c = int(c)
     
diskr = pow(b, 2) - 4 * a * c
print(diskr)
result = ''

if diskr < 0:
    print("корней нет")
    result = 'корней нет'
    
if diskr == 0:
    x = b / (2 * a)
    print(f"корень {x}")
    result = f'корень уравнения x = {x}'
     
if diskr > 0:
    x1 = (- b + math.sqrt(diskr)) / 2 * a
    x2 = (- b - math.sqrt(diskr)) / 2 * a
    print(f"первый корень {x1}, второй корень {x2}")
    result = f'корни уравнения x1 = {x1} и x2 = {x2}'


with open('file3.txt', 'w', encoding='UTF-8') as f:
    f.write(result)
  