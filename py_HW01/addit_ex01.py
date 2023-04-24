# Задача 2: Найдите сумму цифр трехзначного числа.
#
# Пример:
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

user_input = int(input('Введите число: '))
user_number = user_input
amount_numbers = 0

while user_number > 0:
    last_number = user_number % 10
    amount_numbers = amount_numbers + last_number
    user_number = user_number // 10

print(f'{user_input} -> {amount_numbers}')
