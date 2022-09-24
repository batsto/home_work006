#2- Найти сумму чисел списка стоящих на нечетной позиции



from random import random, randint


array = [randint(0,10) for i in range(10)]

print(array)
print(sum(array[::2]))
