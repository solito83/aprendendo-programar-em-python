des = 'Ordem sorteada'
print ('{}'.format(des))
#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nome1 = str(input('Primeiro nome: '))
nome2 = str(input('Segundo nome: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print ('A ordem de apresentação será:')
print (lista)
print ('The End')

