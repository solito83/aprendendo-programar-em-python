strs = 'Aula 9 manipulação de string'
print ('{}'.format(strs))
#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = ('Aprendendo programar em python')
print (len(frase))
print (frase[:30])
print (frase[::15])
print (frase.count('n'))
print ('programar' in frase)
#print (frase.replace ('em', 'com'))
frase = frase.replace ('em', 'com')
print (frase)
print (frase.split())
