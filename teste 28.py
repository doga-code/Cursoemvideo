from random import randint
from time import sleep
escolha = randint (0, 5)
print('-=-' *20)
print('Escolha um número inteiro entre 0 e 5 e veja se você acertou')
print('-=-' *20)
jogador = int(input('O número que você escolheu foi? '))
print('PROCESSANDO...')
sleep(2)
if jogador == escolha:
    print('Você acertou Mizeraviii!!')
else:
    print('ERRRRRRRRRROU, eu pensei no {} e não no {}!!'.format(escolha, jogador))

