num = int(input('Digite um número de 0 até 9999: '))
# n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
# print(n.split()[0][0])
# print(n.split()[0][1])
# print(n.split()[0][2])
# print(n.split()[0][3])
