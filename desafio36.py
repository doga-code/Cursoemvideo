print('----------------------EMPRESTIMO BANCARIO-------------------------')
print('Responda as peguntas seguintes e veja o valor das suas prestacoes!\n')

casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos deseja pagar: '))

prestacao = casa / (anos * 12)
print('O valor da prestação sera de {:.2f}'.format(prestacao))

print('\n Consulta de salário para o empréstimo: \n')

if prestacao > (30/100) * salario:
    print('O seu salário não foi aprovado.')
else:
    print('Parabéns, o seu empréstimo foi aprovado!')
