distancia = float(input('Qual é a distância da sua viajem: '))
print('Você está prestes a começar uma viajem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
