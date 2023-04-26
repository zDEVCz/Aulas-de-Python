#=> Criar um programa de votação, onde deverá ser mostrado ao usuário as opções:
# 1 - item A 
# 2 - item B
# 3 - item C
# 4 - item D
# 5 - item E
# 6 - Brancos ou nulos

#Variaveis
continua = "s"
contador = 0

cont1 = 0   
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont10 = 0
cont20 = 0
cont30 = 0
cont40 = 0
cont50 = 0
cont60 = 0
cont70 = 0
cont80 = 0
cont11 = 0
cont21 = 0
cont31 = 0
cont41 = 0
cont51 = 0
cont61 = 0
cont71 = 0
cont81 = 0

porcent1 = 0
porcent2 = 0
porcent3 = 0
porcent4 = 0
porcent5 = 0
porcent6 = 0
porcent7 = 0
porcent8 = 0
porcent10 = 0
porcent20 = 0
porcent30 = 0
porcent40 = 0
porcent50 = 0
porcent60 = 0
porcent70 = 0
porcent80 = 0
porcent11 = 0
porcent21 = 0
porcent31 = 0
porcent41 = 0
porcent51 = 0
porcent61 = 0
porcent71 = 0
porcent81 = 0

#Looping
while continua == "s" or continua == "S":
  
  print("---------------------------------------")
  print("----------Enquete----------")
  print("---------------------------------------")
  print("Lista de Linguagens\n\n1 -  HTML\n2 - CSS\n3 - JavaScript\n4 - Java\n5 - PHP\n6 - C\n7 - Python\n8 - Outras")
  print("---------------------------------------")
  nome = input("Digite o seu nome: ")
  quest1 = int(input("1) Qual linguagen você mais gostou ? (escolha um número)\nR:"))
  quest2 = int(input("2) Qual linguagen você achou mais pratica ? (escolha um número)\nR:"))
  quest3 = int(input("3) Qual linguagen você achou mais dificio ? (escolha um número)\nR:"))
  
  contador += 1 #Qtd de entrevistados
  #condition
  if quest1 == 1:
    cont1 += 1
  elif quest1 == 2:
    cont2 += 1
  elif quest1 == 3:
    cont3 += 1
  elif quest1 == 4: 
    cont4 += 1
  elif quest1 == 5:
    cont5 += 1
  elif quest1 == 6:
    cont6 += 1
  elif quest1 == 7:
    cont7 += 1
  else: 
    cont8 += 1

  if quest2 == 1:
    cont10 += 1
  elif quest2 == 2:
    cont20 += 1
  elif quest2 == 3:
    cont30 += 1
  elif quest2 == 4: 
    cont40 += 1
  elif quest2 == 5:
    cont50 += 1
  elif quest2 == 6:
    cont60 += 1
  elif quest2 == 7:
    cont70 += 1
  else: 
    cont80 += 1

  if quest3 == 1:
    cont11 += 1
  elif quest3 == 2:
    cont21 += 1
  elif quest3 == 3:
    cont31 += 1
  elif quest3 == 4: 
    cont41 += 1
  elif quest3 == 5:
    cont51 += 1
  elif quest3 == 6:
    cont61 += 1
  elif quest3 == 7:
    cont71 += 1
  else: 
    cont81 += 1

  print("--------------------------------------") 
  continua = input("Deseja continuar a entrevista ? (S ou N) : ")

#Out-dados
print("-----------------------------------------")
print("Resultados:")

print("A quantidade de pessoas entrevistadas foi: ", contador)

print("P/Q1")
porcent1 = (cont1 / contador)*100
print("A quantidade de HTML: ", cont1, " são ", porcent1, "%")
porcent2 = (cont2 / contador)*100
print("A quantidade de CSS: ", cont2, " são ", porcent2, "%")
porcent3 = (cont3 / contador)*100
print("A quantidade de JavaScript: ", cont3, " são ", porcent3, "%")
porcent4 = (cont4 / contador)*100
print("A quantidade de Java: ", cont4, " são ", porcent4, "%")
porcent5 = (cont5 / contador)*100
print("A quantidade de PHP: ", cont5, " são ", porcent5, "%")
porcent6 = (cont6 / contador)*100
print("A quantidade de C: ", cont6, " são ", porcent6, "%")
porcent7 = (cont7 / contador)*100
print("A quantidade de Python: ", cont7, " são ", porcent7, "%")
porcent8 = (cont8 / contador)*100
print("A quantidade de Outras: ", cont8, " são ", porcent8, "%")


print("P/Q2")
porcent10 = (cont10 / contador)*100
print("A quantidade de HTML: ", cont10, " são ", porcent10, "%")
porcent20 = (cont20 / contador)*100
print("A quantidade de CSS: ", cont20, " são ", porcent20, "%")
porcent30 = (cont30 / contador)*100
print("A quantidade de JavaScript: ", cont30, " são ", porcent30, "%")
porcent40 = (cont40 / contador)*100
print("A quantidade de Java: ", cont40, " são ", porcent40, "%")
porcent50 = (cont50 / contador)*100
print("A quantidade de PHP: ", cont50, " são ", porcent50, "%")
porcent6 = (cont6 / contador)*100
print("A quantidade de C: ", cont60, " são ", porcent60, "%")
porcent70 = (cont70 / contador)*100
print("A quantidade de Python: ", cont70, " são ", porcent70, "%")
porcent80 = (cont80 / contador)*100
print("A quantidade de Outras: ", cont80, " são ", porcent80, "%")

print("P/Q3")
porcent11 = (cont11 / contador)*100
print("A quantidade de HTML: ", cont11, " são ", porcent11, "%")
porcent21 = (cont21 / contador)*100
print("A quantidade de CSS: ", cont21, " são ", porcent21, "%")
porcent31 = (cont31 / contador)*100
print("A quantidade de JavaScript: ", cont31, " são ", porcent31, "%")
porcent41 = (cont41 / contador)*100
print("A quantidade de Java: ", cont41, " são ", porcent41, "%")
porcent51 = (cont51 / contador)*100
print("A quantidade de PHP: ", cont51, " são ", porcent51, "%")
porcent61 = (cont61 / contador)*100
print("A quantidade de C: ", cont61, " são ", porcent61, "%")
porcent71 = (cont71 / contador)*100
print("A quantidade de Python: ", cont71, " são ", porcent71, "%")
porcent81 = (cont8 / contador)*100
print("A quantidade de Outras: ", cont81, " são ", porcent81, "%")

print("\nFim da Enquete\n")