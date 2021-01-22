print('aula 08 comandos import, math')
print('from math import sqrt')
# modulo em python >>> bibliotecas externas, onde para criar um programa podemos importa comandos adiocionais destas bibliotecas.
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
fim = 'The End'
print('A raiz de {} é igual a {}\n{}'.format(num, math.ceil(raiz), fim))

import random
num = random.randint (1, 10)
print (num)

#:sweat_smile:

import emoji
print(emoji.emojize('Olá Mundo :sweat_smile:', use_aliases=True))
