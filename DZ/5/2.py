# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def sum_number (i, j):
    i += 1
    j -= 1
    if j > 0:
        return sum_number(i,j)
    return i

print(sum_number(a,b))