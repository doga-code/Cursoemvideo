frase = str(input('Digite uma frase: ')).strip().lower()
print('A plavra A aparece {} na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A letra A aparece por último na posição {}'.format(frase.rfind('a')+1))


