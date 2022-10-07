#Создаем последовательность случайных чисел, разделенных пробелом. Записываем ее в файл. 
#Из последовательности вычисляем максимальное и минимальные значения, записываем их в другой файл.
import random

quantity = int(input('enter how many numbers: '))

def creataList(quantity):   #заполняем список
    list = []
    for i in range(quantity):
         list.append(random.randint(0, 100))
    return list

def createLine(list):
     line = ''
     for i in range(len(list)):
          line += str(list[i])
          if i < len(list) - 1:
               line += ' '
     return line

with open('from.txt', 'w') as f:
  f.write(createLine(creataList(quantity)))

readedLine = ''
with open('from.txt', 'r') as f:
     readedLine = f.readline()
print(readedLine)     

line = readedLine.split(' ')
print(line)

minI = 0
maxI = 0
for i in range (len(line)):
     if int(line[i]) < int(line[minI]):
          minI = i
     if int(line[i]) > int(line[maxI]):
          maxI = i
print(str(line[minI]) + ' ' + str(line[maxI]))

with open('newfile.txt', 'w') as f:
     f.write(str(line[minI]) + '\n')
     f.write(str(line[maxI]) + '\n')
          
         
