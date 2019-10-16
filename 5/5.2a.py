'''
Задание 5.2a
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети, надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):

10.0.1.0/24
190.1.0.0/16
Пример адреса хоста:

10.0.1.1/24 - хост из сети 10.0.1.0/24
10.0.5.1/30 - хост из сети 10.0.5.0/30
Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

'''

z = input('Введите префикс: ')
z = z.split('/')
ip = z[0]
mask = int(z[1])

#print(ip)
#print(mask)

ip = ip.split('.')
ipo1 = int(ip[0])
ipo1 = f'{ipo1:08b}'
ipo2 = int(ip[1])
ipo2 = f'{ipo2:08b}'
ipo3 = int(ip[2])
ipo3 = f'{ipo3:08b}'
ipo4 = int(ip[3])
ipo4 = f'{ipo4:08b}'

maskbin = "1"*mask + "0"*(32-mask)
masko1 = maskbin[:8]
masko2 = maskbin[8:16]
masko3 = maskbin[16:24]
masko4 = maskbin[24:]

print(ipo1, ipo2, ipo3, ipo4)
print(masko1, masko2, masko3, masko4)

v1 = {
    '11111111' : '8',
    '11111110' : '7',
    '11111100' : '6',
    '11111000' : '5',
    '11110000' : '4',
    '11100000' : '3',
    '11000000' : '2',
    '10000000' : '1',
    '00000000' : '0'
}

v = {
	'0': 0,
	'1': 1,
	'2': 1,
	'3': 1,
	'4': 1,
	'5': 1,
	'6': 1,
	'7': 1,
	'8': 1,
}

maskoo1 = int(v1[masko1])
maskoo2 = int(v1[masko2])
maskoo3 = int(v1[masko3])
maskoo4 = int(v1[masko4])

ipoo1 = str(int(ipo1[0:maskoo1]*v[str(maskoo1)]+'0'*(8-maskoo1), 2))
ipoo2 = str(int(ipo2[0:maskoo2]*v[str(maskoo2)]+'0'*(8-maskoo2), 2))
ipoo3 = str(int(ipo3[0:maskoo3]*v[str(maskoo3)]+'0'*(8-maskoo3), 2))
ipoo4 = str(int(ipo4[0:maskoo4]*v[str(maskoo4)]+'0'*(8-maskoo4), 2))

#print(maskoo1, maskoo2, maskoo3, maskoo4)
print(ipoo1+'.'+ipoo2+'.'+ipoo3+'.'+ipoo4+'/'+ str(mask))
