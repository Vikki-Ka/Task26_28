# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(a, b):
    if b == 0:
        return a
    a += 1
    return sum(a, b-1)
    


a = int(input("Ввидите первое число "))
b = int(input("Ввидите второе число "))
print()

print(f"{a} + {b} = {sum(a,b)}")