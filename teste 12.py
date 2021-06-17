valor = float(input('qual o preço do produto? R$ '))
novo = valor - (valor * 5 / 100)
print('o produto que custava R${:.2f}, com o desconto de 5% passou a custar R${:.2f}'.format(valor, novo))


