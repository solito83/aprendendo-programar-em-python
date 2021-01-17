des = ('Desafio-012 Calculando desconto')
print ('{}'.format(des))
#Desafio-12 >>> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pro = float(input('Qual é o valor do produto: '))
desc = float(input('Qual é o valor do desconto: '))

pre = (pro-(pro*(desc/100)))
fim = ('The End')
print ('Legal com este desconto você vai pagar apenas R${:.2f} reais.\n{}'.format(pre,fim))
