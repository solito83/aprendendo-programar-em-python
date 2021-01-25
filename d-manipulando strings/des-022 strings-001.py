des = ('Desafio-022 manipulando strings-001')
print ('{}'.format(des))
#Crie um Programa que leia um nome completo de uma pessoa e mostre na tela: 
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome.

nom = str(input('Qual é seu nome: ')).strip()
nome = nom

print ('Colacando o texto todo em maiúsculo: ',nome.upper(),'OK')
print ('Colocando o texto todo em minúsculo: ',nome.lower(),'ok') 
print ('Seu nome completo é: {} e contém {} letras ao todo.'.format(nome, len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))

div = nome.split()
print ('Seu primeiro nome é: {} e tem {} letras'.format(div[0], len(div[0])))

print (nome[2:10:2])
print (nome.capitalize())
