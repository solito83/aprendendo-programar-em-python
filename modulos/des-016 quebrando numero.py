des = 'Quebrando um número'
print ('{}'.format(des))
#Desafio-016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um número: '))
inteiro = math.trunc(num)
fim = 'The End'
print ('O {} é proximo de {:.0f}\n{}'.format(num, inteiro, fim))