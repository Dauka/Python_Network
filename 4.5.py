'''
Задание 4.5
Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']
'''


command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

a1 = command1.split()
a2 = command2.split()

vlan1 = a1[-1].split(',')
vlan2 = a2[-1].split(',')

#print(a1)
#print(a2)
#print()
#print(vlan1)
#print(vlan2)

b1 = set(vlan1)
b2 = set(vlan2)

result = b1 & b2

print(list(sorted(result)))
