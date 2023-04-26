# Monte um programa para mostrar na tela do computador boa noite 10 vezes (utilizando estrutura de repetição);
print('\nContador 1')
contador=1
while contador<=10:
    print(f'BOA NOITE! - {contador}')
    contador += 1


# Monte um programa para mostrar na tela do computador todos números entre 0 e 100, somente os pares (utilizando estrutura de repetição);
print('\nContador 2')
contador=0
while contador <= 100:
    print(contador)
    contador += 2

# Monte um programa para mostrar na tela do computador todos números entre 100 e 0, somente os impares (utilizando estrutura de repetição);
print('\nContador 3')
contador=100
while contador >= 0:
    print(contador)
    contador -= 2

# Monte um programa para mostrar na tela do computador números entre 100 e 0, somente os impares (utilizando estrutura de repetição);
print('\nContador 4')
contador=100
while contador >= 0:
    print(contador)
    contador -= 3

# Monte um programa para receber na tela do computador nomes de 5 pessoas (utilizando estrutura de repetição);
print('\nContador 5')
cont = 0
while cont <= 4:
    nome = input('Digite seu nome: ')
    cont += 1

# Monte um programa para digitar na tela do computador nomes de 5 pessoas, receber a idade de cada uma delas, calcular e exibir a media de idades (utilizando estrutura de repetição);
print('\nContador 6')
cont = 0
soma = 0
while cont <= 4:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    cont += 1
    soma += idade
media = soma / 5
print(f'A média entre as idades é: {media}')


#DESAFIO: Montar um programa em python que receba o salario de um determinado funcionario, o programa deve calcular quanto deve ser o inss do funcionario.
#levando em consideração
#se ele tem salario ate 1302.00 o inss dele sera de 7.5% (calcular 7.5%)
#se ele tem salario entre 1302.00 até 2571.29, calcular 9%
#se ele tem salario entre 2571.30 até 3856.94, calcular 12%
#se ele tem salario entre 3856.95 até 7507.49, calcular 14%
#se ele tem salario maior que  7507.49 o desconto será de 850 reais.

print('\n\nCalculo de INSS')
#entrada de dados
cont = 0
while cont < 5:
    salario = float(input('Digite aqui o seu salário: '))
    cont += 1
    if salario >= 7507.49:
         inss = salario - 850
         print(f'Sua taxa de INSS é: {inss:.2f}')
    elif salario >= 3856.95:
         inss = salario * 0.14
         print(f'Sua taxa de INSS é: {inss:.2f}')
    elif salario >= 2571.30:
         inss = salario * 0.12
         print(f'Sua taxa de INSS é: {inss:.2f}')
    elif salario >= 1302.00:
         inss = salario * 0.09
         print(f'Sua taxa de INSS é: {inss:.2f}')
    else:
         inss = salario * 0.075
         print(f'Sua taxa de INSS é: {inss:.2f}')



