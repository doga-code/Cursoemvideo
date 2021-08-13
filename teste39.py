nome = input('Qual seu nome: ')
idade = int(input('Qual sua idade: '))

if idade > 18:
    print('Já passaram {} anos da data de alistamento!'.format(idade - 18))
elif idade == 18:
    print('Você deve se alistar. Se atente aos prazos!')
else:
    print('Você ainda não completou 18 anos. Ainda lhe faltam {} anos para o alistamento!'.format(18 - idade))
