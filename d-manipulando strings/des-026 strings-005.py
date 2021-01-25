des = 'Desafio-026 strings-005'
print ('{}'.format(des))
#Faça um programa que leia uma frase pelo teclado e mostre: 
#Quantas veses aparece a letra "a".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece pela ultima vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print ('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print ('A primeira letra "a" aparece na {}ª posição'.format(frase.find('A')+1))
print ('A ultima letra "a" aparece na {}ª posição'.format(frase.rfind('A')+1))
