'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9

'''

from random import randint
bush=int(input('Введите количество кустов '))
count_berry=[randint(1,20) for _ in range(bush)]
max_berry=count_berry[bush-1]+count_berry[0]+count_berry[1]
if max_berry<count_berry[bush-1]+count_berry[0]+count_berry[1]:
    max_berry=count_berry[bush-1]+count_berry[0]+count_berry[1]
for i in range(1,bush-1):
    if count_berry[i-1]+count_berry[i]+count_berry[i+1]>max_berry:
        max_berry=count_berry[i-1]+count_berry[i]+count_berry[i+1]

print(count_berry)
print(max_berry)