'''
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
'''


ospf_route = 'O        10.0.24.0/24 [110/41] via ,10.0.13.3, 3d18h, FastEthernet0/0'

a = ospf_route.split()
proto = a[0]
prefix = a[1]
met = a[2]
met1 = met.strip('[]')
last = str(a[5]).strip(',')
inter = a[6]

b = """
Protocol:               {}SPF     
Prefix:                 {}
AD/Metric:              {}
Next-Hop:               {}
Last update:            {}
Outbound Interface:     {}
"""

print(b.format(proto,prefix,met1,str(a[4]).strip(','),last,inter))