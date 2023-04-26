# => Montar um programa que permite ao usuario digitar o espaço percorrido pelo veiculo km e o tempo utilizado h. calcular a velocidade média do veículo.

#entrada
#print("--------------------------------------------------")
#print("Programa que calcula velocidade media do veiculo.")
#print("--------------------------------------------------")
#
#distancia
#distancia = float(input("Digite a distancia percorrida: "))
#
#tempo
#tempo = float(input("Digite o tempo gasto pelo veiculo: "))

#Processamento
#velocidade_media = distancia / tempo

#Saída
#print("--------------------------------------------------")
#print(f"A velocidade media do veiculo foi: {velocidade_media} Km/h")
#print("--------------------------------------------------")

#-------------------------------------------------------

#=> Montar um programa que permite ao usuario digitar o nome de um produto, digitar o preço deste produto em dolar. Calcular o valor deste produto em reais.

##Entrada
#print("--------------------------------------------------")
#print("Programa de conversão de Dolar para reais.")
#print("--------------------------------------------------")
#
##variaveis
#produto = input("Digite o nome do produto: ")
#preco_dolar = float(input("Digite aqui preço do produto em dolar: "))
#valor_dolar = float(input("Digite o valor da cotação do dolar: "))
#
##processamento
#preco_reais = preco_dolar * valor_dolar
#
##saída
#print("--------------------------------------------------")
#print(f"O valor do produto em reais é: R${preco_reais}")
#print("--------------------------------------------------")

#-------------------------------------------------------

#=> Montar um programa que permite ao usuario digitar digitar nome do produto, valor do produto. O programa deve calcular o valor do produto com o desconto de 3% que será dado pela loja em pagamentos a vista em dinheiro.

##Entrada
#print("--------------------------------------------------")
#print("Programa de Porcentagem de desconto.")
#print("--------------------------------------------------")
#
##variaveis
#nome_prod = input("Digite o nome do produto: ")
#preco = float(input("Digite o valor do produto: "))
#
##Processamento
#novo_preco = preco - (preco * 3/100)
#
##Saída
#print("--------------------------------------------------")
#print(f"O valor do produto com desconto é: R${novo_preco}")
#print("--------------------------------------------------")

#-------------------------------------------------------

#Um programa que permita digitar a quantidade de alulos na sala e a quantidae de alunos com notas superiores ou iguais a 6 e a porcentagem de notas inferiores a 6.

##Entrada
#print("--------------------------------------------------")
#print("Programa que mostre ao usuario a '%' de alunos aprovados e reprovados.")
#print("--------------------------------------------------")
#
##variaveis
#qtd_alunos = int(input("Digite aqui a quantidade de alunos: "))
#qtd_alunos_sup = int(input("Digite aqui a quantidade alunos que tiveram nota >= 6: "))
##qtd_alunos_inf = int(input("Digite aqui a quantidade alunos que tiveram nota < 6: "))
#
##Processamento
#porc_notas_sup = qtd_alunos_sup * 100 / qtd_alunos
#porc_notas_inf = (qtd_alunos - qtd_alunos_sup) * 100 / qtd_alunos
#
##Saída
#print("--------------------------------------------------")
#print(f"Porcentagem de alunos aprovados: {porc_notas_sup}%")
#print(f"Porcentagem de alunos reprovados: {porc_notas_inf}%")
#print("--------------------------------------------------")

#-------------------------------------------------------

#Um programa que permita ao usuario digitar a quantidade de espaço em disco que o mesmo possui (em Gb). Calcular exibindo o espaço em mb e Tb.

##Entrada
#print("--------------------------------------------------")
#print("Programa de conversão de Memoria interna")
#print("--------------------------------------------------")
#
##variaveis
#espaco_em_gb = float(input("Digite a quantidade de espaço em disco (em GB): "))
#
##Processamento
#espaco_em_mb = espaco_em_gb * 1024  # 1 GB = 1024 MB
#espaco_em_tb = espaco_em_gb / 1024  # 1 TB = 1024 GB
#
##Saída
#print("--------------------------------------------------")
#print("Espaço em disco em MB: ", espaco_em_mb)
#print("Espaço em disco em TB: ", espaco_em_tb)
#print("--------------------------------------------------")



