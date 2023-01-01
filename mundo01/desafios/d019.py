import random
a1 = str(input('aluno1: '))
a2 = str(input('aluno1: '))
a3 = str(input('aluno1: '))
a4 = str(input('aluno1: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi: {}'.format(escolhido))
