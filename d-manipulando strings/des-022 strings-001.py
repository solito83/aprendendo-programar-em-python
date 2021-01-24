des = ('Desafio-022 manipulando strings-001')
print ('{}'.format(des))
#Crie um Programa que leia um nome completo de uma pessoa e mostre na tela: 
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome.

nom = str(input('Qual é seu nome: '))
nome = nom
print ('Meu nome é: {}'.format(nome))

print ('Colacando o texto todo em maiúsculo: ',nome.upper(),'OK')
print ('Colocando o texto todo em minúsculo: ',nome.lower(),'ok') 
print ('Contando as letras e excluíndo os espaços da contagem ', len(nome.strip()), '<corrigir>')

print ('Contando somente as letras do primeiro nome: =',len(nome[:6]),'letras <corrigir>')

print (nome[2:10:2])
print (nome.capitalize())
