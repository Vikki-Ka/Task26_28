# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def NewProgress(firstEl, differ, len):
    newList=[]
    for i in range(1,len+1):
        newList.append(firstEl + (i - 1) * differ)
    return newList

firstVal = int(input("Ввидите первый элемент: "))
diff = int(input("Ввидите разность: "))
len = int(input("Ввидите длину массива: "))

print(NewProgress(firstVal, diff, len))