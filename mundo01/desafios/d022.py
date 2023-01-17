nome = str(input('Qual o seu nome ? ')).strip()
# o strip() elimina os espaços em branco antes e depois da str
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
t = int(len(nome))
s = int(nome.count(' '))
l = t - s
print('Seu nome tem: {} letras'.format(l))
print('O primeiro nome tem: {} letras'.format(len(nome.split()[0])))
print('O primeiro nome tem: {} letras'.format(nome.find(' ')))
# acima estamos encontrando o primeiro espaço
