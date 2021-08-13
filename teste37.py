print('------------------BINÁRIOS---------------\n')
valor = int(input('Digite um valor qualquer: '))
escolha = int(input('Escolha a base de conversão: (1 - binário    2 - octal    3 - hexadecimal)'))

if escolha == 1:
    print('Seu número {} em binário é {}'.format(valor, bin(valor)))
elif escolha == 2:
    print('Seu número {} em Octal é {}'.format(valor, oct(valor)))
elif escolha == 3:
    print('Seu número {} em hexadecimal é {}'.format(valor, hex(valor)))
else:
    print('Digite um número por favor...')
