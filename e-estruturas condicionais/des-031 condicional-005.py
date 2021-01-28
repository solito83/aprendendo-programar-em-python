des = 'Desafio-029 estruturas condicionais'
print ('{}'.format(des))
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

kmh = int(input('Quantos kilometros tem seu percurso? '))
fim = 'The End'

if kmh <= 200:
    print ('Sua passagem vai custar: R${:.2f} reais\n {}'.format(kmh * 0.5, fim))
else:
    print ('Sua passagem vai custar: R${:.2f} reais\n {}'.format(kmh * 0.45, fim))
