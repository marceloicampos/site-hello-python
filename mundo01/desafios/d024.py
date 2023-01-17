c = str(input('Digite um nome de uma cidade: ')).strip()
lc = c.lower()
print('{} começa com SANTO: {}'.format(c, ('santo' in lc.split()[0])))
print(lc[:5] == 'santo')
