#Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

num = int(input('enter any number: '))
fibonacci = [0, 1]
negafibonacci = []
negafibonacci_fibonacci = []
for i in range (2, num + 1):
    fibonacci.append(fibonacci [i - 1] + fibonacci [i - 2]) #заполняем фибонначи
    negafibonacci.insert(0, ((-1) ** (i + 1) * fibonacci[i])) #заполняем негафибонначи
negafibonacci_fibonacci = negafibonacci + fibonacci #объединяем два списка
print(negafibonacci_fibonacci)