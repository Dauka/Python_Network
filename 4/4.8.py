'''
Задание 4.8
Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:

столбцами
ширина столбца 10 символов
Пример вывода для адреса 10.1.1.1:

10        1         1         1
00001010  00000001  00000001  00000001
'''


ip = '192.168.3.1'
b=ip.split('.')
A = int(b[0])
B = int(b[1])
C = int(b[2])
D = int(b[3])


result = """
    IP address:
    {0:<10} {1:<10} {2:<10} {3:<10}
    {0:010b} {1:010b} {2:010b} {3:010b}
"""

print(result.format(A,B,C,D))