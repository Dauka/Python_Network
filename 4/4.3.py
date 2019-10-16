'''
Задание 4.3
Получить из строки config список VLANов вида: ['1', '3', '10', '20', '30', '100']
'''


config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
a=config.split()
print(a)
b=a[-1].split(',')
print(b)
