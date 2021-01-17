des = ('Desafio-013 Aumento de salário')
print ('{}'.format(des))
#Desafio-12 >>> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

sal = float(input('Qual é seu salário atual: '))
aum = float(input('Digite seu aumento: '))

pre = (sal+(sal*(aum/100)))
fim = ('The End')
print ('Legal com este aumento você vai ganhar R${:.2f} reais.\n{}'.format(pre,fim))
