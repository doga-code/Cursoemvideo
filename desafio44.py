print('{:^40}'.format('LOJAS DOUGSOA'))
preço = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO
[1] À VISTA DINHEIRO/CHEQUE
[2] À VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
opção = int(input('Escolha umas das opções acima: '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelado em 2x de R$ {:.2f} sem juros.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS.'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))