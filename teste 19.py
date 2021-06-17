from random import choice
um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Terceiro aluno: ')
quatro = input('Quarto aluno: ')
lista = [um, dois, tres, quatro]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))
