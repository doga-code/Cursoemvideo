lar = float(input('digite aqui a largura em metros: '))
alt = float(input('digite aqu a altura em metros: '))
area = lar * alt
print('sua parede tem a dimensão de {} x {} e a sua área é de {}m²'.format(lar, alt, area))
tinta = area / 2
print('para pintar esta parede, você irá precisar de {}L de tinta '.format(tinta))
