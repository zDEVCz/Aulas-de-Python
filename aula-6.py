#=> Montar um programa que permita fazer uma enquete. Nesta enquete
#iremos perguntar o nome da pessoa e a sua idade. Serão entrevistados N pessoas (N pessoas corresponde a um número positivo e qualquer).
#Ao término da enquete o programa deve fornecer:
#a) Quantidade de pessoas entrevistadas
#b) A média das idades entre as pessoas entrevistadas
#c) A maior idade digitada entre os entrevistados
#d) A menor idade digitada entre os entrevistados
#e) A quantidade de cada genero entre os entrevistados
#f) A quantidade em porcentagem de cada genero entre os entrevistados
#g) O programa deve perguntar quando para de entrevistar

#qtd = int(input("Digite a qtd de pessoas que serão entrevistadas: "))

#Variaveis
continua = "s"
contador = 0
soma = 0
maior = 0
menor = 0
contF = 0
contM = 0
contO = 0
porcentO = 0
porcentF = 0
porcentM = 0

#looping
while continua == "s" or continua == "S":
   print("---------------------------------------------------")
   nome = input("Digite o seu nome: ")
   idade = int(input("Digite a sua idade: "))
   sexo = input('Digite o sexo (F, M ou O) : ')
   
   if contador == 0:    # digitou a primeira idade
      maior = idade     # o maior tem que ser a primeira idade digitada
      menor = idade     # a primeira idade digitada é a menor  
   contador += 1
   soma += idade
   
   if idade > maior:
      maior = idade
   if idade < menor:
      menor = idade
    
   if sexo == "f" or sexo == "F":
    contF += 1
   elif sexo == "m" or sexo == "M":
    contM += 1
   else:
    contO += 1
   print("---------------------------------------------------") 
   continua = input("Deseja continuar a entrevistar ? (S ou N) : ")

#Saída de dados
print("-------------------------------------------------")
print("Resultados:")
print("A quantidade de pessoas entrevistadas foi: ", contador)
media = soma / contador
print("A média das idades é: ", media)
print("A maior idade digitada é: ", maior)
print("A menor idade digitada é: ", menor)
porcentM = (contM / contador)*100
print("A quantidade de pessoas do sexo Masculino: ", contM, " são ", porcentM, "%")
porcentF = (contF / contador)*100
print("A quantidade de pessoas do sexo Feminino: ", contF, " são ", porcentF, "%")
porcentO = (contO / contador)*100
print("A quantidade de pessoas do sexo Outros: ", contO, " são ", porcentO, "%")
print("\nFim da Enquete\n")