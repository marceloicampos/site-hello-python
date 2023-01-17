nome = str(input('Digite seu nome: ')).strip()
print(nome.split())
print('Muito prazer em te conhecer.')
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
f = len(nome.split()) - 1
print(f)
print('Seu último nome é: {}'.format(nome.split()[f]))
