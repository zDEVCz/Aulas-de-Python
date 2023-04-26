#Mostrar um programa em python para receber as notas do alunos 
#Ex 1: Se o aluno está aprovado (média >= 6) ou dependência (média < 6);

#entrada de dados
print('\nCalculo da média dos Alunos')
nota_ex = float(input('Digite a nota dos Exercícios: '))
nota_ad = float(input('Digite a nota da Avaliação Dissertativa: '))
nota_pr = float(input('Digite a nota do Provão Eletrônico: '))

#Processamento
media = (nota_ex*2 + nota_ad*3 + nota_pr*5)/10

#Saída de dados
print('A média do aluno: ',media)

if media>=6:
    print('Situação do aluno: Aprovado')
else:
    print('Situação do aluno: Dependência')


#Ex 2: Se o aluno está aprovado (média >= 6) em recuperação (média entre 3 e 5.9) ou dependência (média < 3);

#entrada de dados
print('\n\nCalculo da média dos Alunos mais elaborada')
nota_ex = float(input('Digite a nota dos Exercícios: '))
nota_ad = float(input('Digite a nota da Avaliação Dissertativa: '))
nota_pr = float(input('Digite a nota do Provão Eletrônico: '))

#Processamento
media = (nota_ex*2 + nota_ad*3 + nota_pr*5)/10

#Saída de dados
print(f'\nA média do aluno: {media}')

if media>=6:
    print('Situação do aluno: Aprovado')
else:
    if media >= 3:
        print('Situação do aluno: Recuperação')
    else:
        print('Situação do aluno: Dependência')


#Ex 3: Montar um programa em python para receber dois números inteiros, receber uma opção de operação e efetuar a operação desejada. (+,-,*,/)

print('\n\nCalculadora')
#Entrada de dados
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))

print('\n1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')
operacao=input('Escolha a operação 1,2,3 ou 4 : ')

#Processamento
if operacao == '1':
    res = n1 + n2
    print(f'A soma entre os números: {res:.2f}')
elif operacao == '2':
    res = n1 - n2
    print(f'A subtração entre os números é : {res:.2f}')
elif operacao == '3':
    res = n1 * n2
    print(f'A multiplicação entre os números é: {res:.2f}')
elif operacao == '4':
    res = n1 / n2
    print(f'A divisão entre os números é: {res:.2f}')
else:
    print('Querido usuario, era para escolher um número entre 1 e 4.')


#Ex 4: Montar um programa em python que receba o salario de um determinado funcionario, o programa deve calcular quanto deve ser o inss do funcionario.
#levando em consideração
#se ele tem salario ate 1302.00 o inss dele sera de 7.5% (calcular 7.5%)
#se ele tem salario entre 1302.00 até 2571.29, calcular 9%
#se ele tem salario entre 2571.30 até 3856.94, calcular 12%
#se ele tem salario entre 3856.95 até 7507.49, calcular 14%
#se ele tem salario maior que  7507.49 o desconto será de 850 reais.

print('\n\nCalculo de INSS')
#entrada de dados
salario = float(input('Digite aqui o seu salário: '))

#Processamento
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
