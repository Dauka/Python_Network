'''
Задание 4.2
Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX XXXX.XXXX.XXXX
'''


mac = 'AAAA:BBBB:CCCC'
print(mac.replace(':','.'))