'''
Задание 5.3a
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:

для access: „Введите номер VLAN:“
для trunk: „Введите разрешенные VLANы:“
Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if и циклов for/while.

'''

input1 = input('Введите режим работы интерфейса (access/trunk): ')
input2 = input('Введите тип и номер интерфейса: ')


access_template = [
    'switchport mode access',
    'switchport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

type = {
    'access': access_template,
    'trunk' : trunk_template
}
a = {
    'access': "Введите номер VLAN:",
    'trunk' : "Введите разрешенные VLANы:"

}
input3 = input(a[input1])

print()
print('interface ' + input2)
print('\n'.join(type[input1]).format(input3))
