#Vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

nome = str(input('Digite seu nome: '))
if nome == 'Solito':
    print ('Legal! seu nome é diferente!')
#else:
#    print ('Seu nome é bem comum.')
#print ('fim')

from emoji import emojize
em = emojize (':sweat_smile:', use_aliases=True)

n1 = float(input('Digite a primeria nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1+n2)/2
print ('A sua nota foi: {:.1f}'.format(nota))
print ('Parabéns',em*3 if nota >=6 else 'Estude mais!!!')
