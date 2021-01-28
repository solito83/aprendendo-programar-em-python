des = 'Desafio-029 estruturas condicionais'
print ('{}'.format(des))
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

kmh = int(input('Mostre a velocidade do seu carro: '))
multa = (kmh - 80 ) * 7
print ('Você foi multado em R${:.2f} reais'.format(multa) if multa > 0 else ('Parabéns Você andou certo.'))
