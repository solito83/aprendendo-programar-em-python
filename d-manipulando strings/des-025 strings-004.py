des = 'Desafio-025 strings-004'
print ('{}'.format(des))
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no seu nome.

nome = str(input('Digite um nome: ')).strip()
print ('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
