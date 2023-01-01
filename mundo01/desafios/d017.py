import math
from math import pow
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
print('o valor da hipotenusa é: {:.2f}'.format(math.hypot(co, ca)))
print('o valor da hipotenusa é: {:.2f}'.format(
    math.sqrt(pow(co, 2)+pow(ca, 2))))
print('o valor da hipotenusa é: {:.2f}'.format((co**2+ca**2) ** (1/2)))
