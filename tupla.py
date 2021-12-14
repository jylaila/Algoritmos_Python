
#vetor tamanho pré definido, consigo add ou remover elementos 
#lista tamanho aumenta ou diminiu, , consigo add ou remover elementos 
#tupla tamanho pré definido, mas não consigo alterar os elementos


#Lista
#elementos, podem ser modificados durante a execução do programa
lista  = []

lista.append("A") #0
lista.append("B") #1
lista.append("C") #2

lista[1] = "D"

#Tupla
#valores são imutaveis
vogais = ("a", "e", "i", "o", "u")
diasdasemana = ()
moedas = ("dolar", "real", "euro")
# moedas[0] = "libra" #atribuição = erro
meses = "janeiro", "fevereiro", "marco"

# for mes in meses:
#     print(mes)
    
#atribuicao implicita
vogais = ("a", "e", "i", "o", "u")

#atribuicao explicita
vogais = tuple("aeiou")

#matriz
lista = [0,1,2,3,4]
matriz=[
    [0,1,2], #linha 0
    [3,4,5], #linha 1
    [6,7,8]  #linha 2
]

#linha x coluna
#imprimir elementos da linha 0
# print(matriz[0])
#imprimir o numero 7
# print(matriz[2][1])

#mudar o numero 3 para 33
matriz[1][0] = 33 #linha[1] coluna[0]

#dicionario
pacientes ={"Joao":111111111, "Carla": 11888888, "Daniel": 11777777, "Carla": 22222222}

pacientes["Carla"] = 11888887 #vai substituir valor
pacientes["Jose"] =  11888555 #vai add

print(pacientes)

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")

if pacientes.get(nome): #verifica se a chave existe
    print("Paciente já existe") 
else: 
    pacientes[nome] = telefone #adiciono
    
#retornar se a chave existe e se existir retorna o valor
print(pacientes.get("Joao", "Paciente não existe"))

if nome in pacientes:
   print("Paciente já existe")

print("Joao" in pacientes) #verificando se existe a chave joão em pacientes //verdadeiro ou falso

print (11888555 in pacientes.values) #verifico se existe valor 11888555 em pacientes //verdadeiro ou falso

#removendo valores do dicionario
#pop e del

del pacientes["Joao"] #removo o joão do dicionario

#remove a chave e retorna o valor, e pode mostrar uma mensagem de erro
print(pacientes.pop("Joao", "Contato não existe"))

retorno = pacientes.pop("Joao", "Contato não existe")
print(retorno)