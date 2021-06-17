n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {}'.format(m))
print('PARABÉNS VOCÊ FOI APROVADO!!' if m >= 7 else 'Você está na recuperação!')
