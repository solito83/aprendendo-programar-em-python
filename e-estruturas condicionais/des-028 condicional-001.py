des = 'Desafio-028 estruturas condicionais simples e composta.'
print ('{}'.format(des))
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu..

#nu1 = float(input('Digite im número entre "0 e 5": '))
#print ('Você Ganhoooou' if nu1 == 1 or nu1 == #4 else 'Você Perdeeeeu')

from random import randint
from time import sleep
comp = randint(0, 5)
print ('<=>'*20)
print ('Vou pensar num número entre "0" e "5". tente adinvihar')
print ('<=>'*20)
joga = int(input('Em  que número você pensou? '))
print ('To pensando...')
sleep(3)
if joga == comp:
    print ('Parabéns... Me lasquei')
else: 
    print ('Se deu mau... Guanheeeei')


