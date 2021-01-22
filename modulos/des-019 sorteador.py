des = 'Sorteador'
print ('{}'.format(des))
#Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

#import random
from random import choice

p = str(input('nome1: '))
m = str(input('nome2: '))
h = str(input('nome3: '))
j = str(input('nome4: '))

#Lista é feito entre Colchetes ...[]...
lista = [p, m, h, j]
sorteado = choice(lista)
print ('O aluno sorteado foi: {}'.format(sorteado))
