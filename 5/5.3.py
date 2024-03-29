'''
Задание 5.3
Скрипт должен запрашивать у пользователя:

информацию о режиме интерфейса (access/trunk)
номере интерфейса (тип и номер, вида Gi0/3)
номер VLANа (для режима trunk будет вводиться список VLANов)
В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться соответствующая конфигурация access или trunk (шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if и циклов for/while.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

'''

input1 = input('Введите режим работы интерфейса (access/trunk): ')
input2 = input('Введите тип и номер интерфейса: ')
input3 = input('Введите номер влан(ов): ')

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

print()
print('interface ' + input2)
print('\n'.join(type[input1]).format(input3))
