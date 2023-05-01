#Задача 14: Требуется вывести все целые степени двойки (т.е. числавида 2k),
# не превосходящие числа N.

n = int(input('Введите число n: '))
a = 2
degree = 0
number = 0

print(n, end=' ')
print('->', end=' ')

while number < n:
    number = a**degree
    if number < n:
        print(number, end=' ')
        degree += 1
