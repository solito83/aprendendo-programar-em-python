des = 'Desafio-028 estruturas condicionais simples e composta.'
print ('{}'.format(des))
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu..

from random import randint
comp = randint(0, 5)
joga = float(input('Pense em um número entre "0 e 5": '))
joga == comp
print ('Você Ganhoooou' if (joga == comp) == 1 or (joga == comp) == 4 else 'Você Perdeeeeu')