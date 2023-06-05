#  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
from random import randint
N = int(input("Введите количество кустов: "))

list_N = []

for i in range(N):
    list_N.append(randint(0,10))

list_count = []
for i in range(len(list_N) - 1):
    list_count.append(list_N[i-1] + list_N[i] + list_N[i + 1])
list_count.append(list_N[-2] + list_N[-1] + list_N[0])

print(max(list_count))
