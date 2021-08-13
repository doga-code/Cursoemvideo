print('\n De acordo com a tabela abaixo classifique através da idade dos novos alunos sua categoria: \n')
print('Até 9 anos: MIRIM')
print('Até 14 anos: INFANTIL')
print('Até 19 anos: JUNIOR')
print('Até 20 anos: SÊNIOR')
print('Acima: MASTER\n')

Nome = input('Qual o nome do atleta: ')
idade = int(input('Qual a idade do atleta: '))

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 20:
    print('Sua categoria é SÊNIOR')
elif idade > 20:
    print('Sua categoria é MASTER')
else:
    print('Você deve digitar uma idade!')