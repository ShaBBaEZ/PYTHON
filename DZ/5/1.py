# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def Degree (i, j):
    if (j == 0):
        return 1
    return Degree(i, j - 1) * i

print(Degree(a,b))