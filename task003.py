# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math

t = input().split()
t  = list(map(lambda x: int(x), t))
print(t)

length = math.sqrt((t[1]-t[0])**2 + (t[3]-t[2])**2)
print(length)