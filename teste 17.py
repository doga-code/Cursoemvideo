import math

co = float(input('encontre o valor do cateto oposto: '))
ca = float(input('Encontre o valor do cateto adjacente: '))

hipo = (ca ** 2 + co ** 2) ** (1 / 2)

print('O valor da hipotenusa é {}'.format(hipo))
