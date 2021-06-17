vel = float(input('Qual a velocidade atual do carro: '))
if vel >= 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h'
          'você deve pagar uma multa de R${:.2f}'.format((vel-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança.')
