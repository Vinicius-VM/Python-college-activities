import math as mt

#variavelpython = "Hello world"
# print(r.variavelR)
#mt.sqrt(25)

#nome = "anderson"
#sobrenome = "ara"
#nome_total = nome + " " + sobrenome
#len(nome_total)
#nome_total.capitalize()

#LISTA1=[1,3,'texto',['a','b','c'],[10,20,30],90]
#print(LISTA1)


##estrutura if e elif
#nota = float(input("digite a nota: "))
#f nota >= 6:
#  print("Aprovado")
#elif nota >= 4:
#  print("Exame")
#else:
#  print("Reprovado")

#if nota == 10:
#  print("parabéns!")
  
#num = 2
#if num == 0:
#  print("O numero é zero")
#elif num > 0:
#  print("O número é positivo")
#else: 
#  print("O número é negativo")


#idade = int(input("Digite a idade: "))
#if idade < 12:
#  print("Criança")
#elif idade < 18:
#  print("adolescente")
#elif idade < 60:
#  print("Adulto")
#else:
#  print("idoso")

#contador = 0
#while contador <= 5:
#  print("Contador: ", contador)
#  contador = contador + 1

senha = "12345"
leitura = ""
while leitura != senha:
  leitura = input("Digite a senha: ")
  if leitura == senha:
    print("Acesso liberado")
  else:
    print("Acesso negado, tente novamente!")
