salario = float(input('Qual é o salário do funcinário? R$'))
# Salários acima R$1.250,00 calculado aumento de 10%
# Salários abaixo ou igual a R$1.250,00 calculado aumento de 15%
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))
