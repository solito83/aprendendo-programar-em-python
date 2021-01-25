des = 'Desafio-024 strings-003'
print ('{}'.format(des))
#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".

city = str(input('Digite o nome da cidade: ')).strip()
#cidade = city.split()
#print ('santo' in cidade[0])

print (city[:5].upper() == 'SANTO')


