import math
from math import trunc
num = float(input('digite um número real: '))
print('a porção inteira número é: {:.0f}'.format(num))
print('a porção inteira número é: {}'.format(math.trunc(num)))
print('a porção inteira número é: {}'.format(trunc(num)))
print('a porção inteira número é: {}'.format(int(num)))
