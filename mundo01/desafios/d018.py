import math
from math import sin, cos, tan
a = float(input('digite um ângulo: '))
r = math.radians(a)
print('valor do seno é: {:.2f}'.format(sin(r)))
print('valor do cosseno é: {:.2f}'.format(cos(r)))
print('valor da tangente é: {:.2f}'.format(tan(r)))
