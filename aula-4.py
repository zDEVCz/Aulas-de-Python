#Montar um programa 

##entrada
#print("\n----------------------------------------")
#print("Exemplo if - exercício 1 - Notas")
#print("----------------------------------------\n")
#
##variaveis
#nota = float(input("Digite a nota da prova: "))
#
##processamento
#if nota < 6:
#    print("\nVocê precisa fazer a prova de recuperação.")
#
#input("\nFim do programa")
#print("----------------------------------------\n")

#-------------------------------------------------------

#Montar um programa que o usuário digitar o preço e se o produto for mair que mil, mostra a mensagem "Nossa que caro !", caso o contrario mostrar a mensagem "Podemos pensar em comprar.".

##entrada
#print("\n----------------------------------------")
#print("Exemplo if - exercício 2 - Produto")
#print("----------------------------------------\n")
#
##variaveis
#prod_preco1 = float(input("Digite aqui o valor do produto: #"))
#
##processamento/Saída
#if prod_preco1 > 1000:
#    print("Nossa que caro !")
#else:
#    print("Podemos pensar em comprar.")
#
#print("\n----------------------------------------")
#input("Fim do programa")
#print("----------------------------------------")

#-------------------------------------------------------

#Montar um programa que calcule o reajuste do preço de um produto. Se o produto ter o preço menor que 100, calcular o reajuste de 5%. Caso o preço for maior que 100 e menor que 200 o reajuste é de 3%. Caso contrario o reajuste será de 1.5%.

##entrada
#print("\n----------------------------------------")
#print("Exemplo if - exercício 3 - Reajuste")
#print("----------------------------------------\n")
#
##variaveis
#prod_preco2 = float(input("Digite aqui o valor do produto: #"))
#
##processamento/Saída
#if prod_preco2 > 200:
#    novo_preco = prod_preco2 + (prod_preco2*0.015)
#    
#elif prod_preco2 >= 100:
#    novo_preco = prod_preco2 + (prod_preco2*0.03)
#    
#else: 
#    novo_preco = prod_preco2 + (prod_preco2*0.05)
#
#print(f"O preço do produto com reajuste é: R${novo_preco}")
#
#print("\n----------------------------------------")
#input("Fim do programa")
#print("----------------------------------------")

#-------------------------------------------------------

#Montar um programa que permita ao usuario digitar 3 números que correspondem aos lados de um triangulo. Para verificar se o triangulo é isoceles, escaleno ou equilatero.

#Regras:
#Equilatero = lados iguais;
#Escaleno = lados diferentes;
#Isósceles = dois lados iguais;
#Retângulo = angulo = 90°;

##entrada
#print("\n----------------------------------------")
#print("Exemplo if - exercício 4 - Desafio")
#print("----------------------------------------\n")
#
##variaveis
#lado1 = float(input("Digite aqui o valor do 1º Cateto do triangulo: "))
#lado2 = float(input("Digite aqui o valor do 2º Cateto do triangulo: "))
#lado3 = float(input("Digite aqui o valor da Hipotenusa do triangulo: "))
#
##processamento/Saída
#if lado1 == lado2 == lado3:
#    print("É um triangulo Equilátero.")
#elif lado1 == lado2 and lado1 != lado3:
#    print("É um triangulo Isósceles.")
#elif ((lado3**2)==(lado1**2)+(lado2**2)):
#    print("É um triangulo Retângulo.")
#else:
#    print("É um triangulo Escaleno.")
#
#
#print("\n----------------------------------------")
#input("Fim do programa")
#print("----------------------------------------")

#-------------------------------------------------------

#Montar um programa que calcule o reajuste do salario de um funcionario. 
#se o funcionario recebe 1500, seu reajuste é de 12.57%. 
#se o funcionario recebe entre 1500 e 3000, o reajuste será de 8.35%.
#se o funcionario recebe entre 3000 e 5785, o reajuste será de 5.78%. 
#caso contrario, o resajuste será de 2%.

##entrada
#print("\n----------------------------------------")
#print("Exemplo if - exercício 5 - Desafio")
#print("----------------------------------------\n")
#
##variaveis
#salario = float(input('Digite aqui seu salario: '))
#
##processamento
#if salario >= 5785:
#    reajuste = salario + (salario * 0.02)
#elif salario >= 3000:
#    reajuste = salario + (salario * 0.0578) 
#elif salario >= 1500:
#    reajuste = salario + (salario * 0.0835)
#else:
#    reajuste = salario + (salario * 0.1257)
#
##Saída
#print(f'Seu salario com reajuste será de R${reajuste}')
#
#print("\n----------------------------------------")
#input("Fim do programa")
#print("----------------------------------------")

#-------------------------------------------------------

#Montar um programa que calcule o salario de um funcionário.

#entrada
print("\n----------------------------------------")
print("Exemplo if - exercício 6 - Desafio")
print("----------------------------------------\n")

#variaveis
salario = float(input('Digite aqui seu salario: '))

#processamento
if salario >= 5785:
    reajuste = salario + (salario * 0.02)
elif salario >= 3000:
    reajuste = salario + (salario * 0.0578) 
elif salario >= 1500:
    reajuste = salario + (salario * 0.0835)
else:
    reajuste = salario + (salario * 0.1257)

#Saída
print(f'Seu salario com reajuste será de R${reajuste}')

print("\n----------------------------------------")
input("Fim do programa")
print("----------------------------------------")