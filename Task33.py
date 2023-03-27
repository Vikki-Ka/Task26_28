# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

def magazin(n):
    array = [randint(1, 5) for _ in range(n)]
    print(array)
    return array

def chanMin(array):
    small = min(array)
    large = max(array)
    for i in range(len(array)-1):
        if array[i] == large:
            array[i] = small
    return array

arrayNew = magazin(10)
print(chanMin(arrayNew))