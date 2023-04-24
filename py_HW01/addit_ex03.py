# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# Пример:
# 385916 -> yes
# 123456 -> no

user_input = input('Введите шестизначный номер билета: ')
ticket_number = int(user_input)
first_amount = 0
second_amount = 0
count = 0

while count < 3:
    last_number = ticket_number % 10
    second_amount = second_amount + last_number
    ticket_number = ticket_number // 10
    count += 1

while count < 6:
    last_number = ticket_number % 10
    first_amount = first_amount + last_number
    ticket_number = ticket_number // 10
    count += 1

if first_amount == second_amount:
    print(f'{user_input} -> yes')
else:
    print(f'{user_input} -> no')
