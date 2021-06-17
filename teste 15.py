km = float(input('Quantos km rodados? '))
dias = int(input('quantos dias ele foi alugado? '))
pagar = (60 * dias) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(pagar))
