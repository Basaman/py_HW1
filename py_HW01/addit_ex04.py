# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n_chocolate = int(input('Введите сторону шоколадки n: '))
m_chocolate = int(input('Введите сторону шоколадки m: '))
k_parts = int(input('Введите сколько долек вы хотите отломить: '))

if (k_parts % n_chocolate == 0 or k_parts % m_chocolate == 0) and k_parts < (n_chocolate * m_chocolate):
    print(f'{n_chocolate} {m_chocolate} {k_parts} -> yes')
else:
    print(f'{n_chocolate} {m_chocolate} {k_parts} -> no')