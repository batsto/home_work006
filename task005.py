# 5- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from audioop import reverse
import math
from random import randint
from typing import Reversible


array = [randint(0,10) for item in range(0,11)]

new_array = lambda array: [array[i] * array[-i-1] for i in range(math.ceil(len(array)/2))]

print(array)
print(new_array(array))














