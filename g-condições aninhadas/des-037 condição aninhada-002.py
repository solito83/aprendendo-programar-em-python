'''
    import tkinter as tk

    window = tk.Tk()
    window.geometry ("800x450+0+0")
    window.title ('Conversor de base')

    des = 'Desafio-037 estrutura condição aninhada-002'
    print ('{}'.format(des))
'''
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print ('''
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
''')

opção = int(input('Sua opção: '))

if opção == 1:
    print ('\033[0;32m{} Converido para BINARIO é igual a: {}\033[m'.format(n, bin(n)[2:]))
elif opção == 2:
    print ('\033[0;31m{} Convertido para OCTAL é igual a: {}\033[m'.format(n, oct(n)[2:]))
elif opção == 3:
    print ('\033[0;36m{} Convertido para HEXADECIMAL é igual a: {}\033[m'.format(n, hex(n)[2:]))
