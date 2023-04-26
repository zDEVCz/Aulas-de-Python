# Montar um programa que mostre o meu nome 5 vezes;

#print('Contador 1\n')
#contador=1
#while contador<=5:
#    print('Cauã\n')
#    contador += 1

# Montar um programa que permita ao usuario digitar o seu nome e mostra-lo 5 vezes;

#print('Contador 2\n')
#nome = input('Digite seu nome: ')
#contador=1
#while contador<=5:
#    print(f'Seu nome é {nome}\n')
#    contador += 1

# Montar um programa que permita ao usuario digitar o seu nome e a quantidade de vezes que ele quer que repita.

#print('\nContador 3\n')
#nome = input('Digite seu nome: ')
#contador = int(input('Digite a quantidade de repetições: '))
#while 1 <= contador:
#    print(f'\nO nome digitado é {nome}, repetição {contador}')
#    contador -= 1

# Montar um programa que some todos os números 1 a 100

#soma = 0
#contador = 0
#
#while contador <= 100:
#    soma += contador
#    contador += 1
#
#print(f'A soma é {soma}\n')

#Desafio
#Montar um programa que permita ao usuario digitar um número e o computador irá somar todos os numeros entre 1 até o número digitado.
#Obs: o número pode ser positivo ou negativo

soma = 0
contador = 0
qtd = int(input('Digite um número: '))
if (qtd >= 0):
    while contador <= qtd:
        soma += contador
        contador += 1
else:
    while contador >= qtd:
        soma += contador
        contador -= 1
print(f'A soma é {soma}\n')