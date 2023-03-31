# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def NewList(len):
    newlist = [randint(0, 9) for _ in range(len)]
    return newlist


userNamber = int(input("Ввидите длину массива: "))
minVal = int(input("Ввидите минимальный порог: "))
maxVal = int(input("Ввидите максимальный порог: "))

workList = NewList(userNamber)
print(workList)

for i in range(userNamber):
    if workList[i] > minVal and workList[i] < maxVal:
        print(i, end=" ")
