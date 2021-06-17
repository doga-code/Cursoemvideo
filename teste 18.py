import random

pessoas = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro',
           'Francisca', 'Marcos']

print('sorteio')

print('O ganhador foi: ' + pessoas[random.randrange(len(pessoas))])
