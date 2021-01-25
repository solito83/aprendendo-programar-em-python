des = 'Desafio-027 strings-006'
print ('{}'.format(des))
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nom = str(input('Digite um Nome: ')).strip()
nome = nom.split()
print ('Olá, muito prazer')
print ('Seu 1º nome é: {}'.format(nome[0]))
print ('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
