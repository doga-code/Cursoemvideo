real = float(input('Digite o valor aqui:R$'))
dollar = real / 5.27
pesos = real / 0.056
print('com R${:.2f} você pode comprar US${:.2f} ou $a{:.2f}'.format(real, dollar, pesos))
