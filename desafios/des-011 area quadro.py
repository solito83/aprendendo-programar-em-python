des = ('Desafio-011 Calculando área')
print ('{}'.format(des))
#Desafio-11 >>> Faça um programa que leia a largura e a altura de uma parede em metros. cálcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta dois metros quadrado.

alt = float(input('Digite a altura: '))
lar = float(input('Digite a lagura: '))

area = (alt*lar)/2
fim = ('The End')
print ('É necessário {:.2f} litros de tinta para pintar toda a area.\n{}'.format(area,fim))
