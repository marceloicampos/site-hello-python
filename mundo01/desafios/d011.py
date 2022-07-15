a = float(input('Altura da Parede em Metros: '))
l = float(input('Largura da Parede em Metros: '))
r = a*l
t = 2
print('Área da parede é: ', r, 'metros quadrados')
print('Será necessário {} litro de tinta para pintar a parede'.format(r/t))
print('Cada litro de tinta, pinta 2 metros quadrados')
