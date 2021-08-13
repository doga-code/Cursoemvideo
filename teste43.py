print('-----------------CALCULADORA IMC--------------')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

print('O seu IMC é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('CUIDADO! Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está no peso ideal.')
elif 25 <= imc < 30:
    print('ATENÇÃO! Você está no sobrepeso.')
elif 30 <= imc < 40:
    print('CUIDADO! Você está na faixa da obesidade.')
elif imc >=40:
    print('CUIDADO! Você está na faixa de obesidade mórbida.')
