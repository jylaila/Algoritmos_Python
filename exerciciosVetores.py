#criar a lista
#Exercicio 1
from typing import no_type_check


a = []

#ler 10 numeros
for i in range(10):
    #armazenando no vetor
    a.append(int(input("Digite um número: ")))
print(a)#imprimo todos os elementos do vetor

i = 0
while i<10:
    a.append(int(input("Digite um número: ")))
    i+=1
print(a)

#Exercício 2
tam = len(a) #len retorna o tamanho da lista
x=0 #variável de controle
while x < tam:
    print(a[x]) #imprimo vetor[posicao]
    x+=1 #incremento o x

#não preciso do tamanho do vetor
for x in a:
    print(x)


#Exercicio Maior e Menor

numeros = []
maior = 0
menor = 0
y = 0

for i in range(10):
    #armazenando no vetor
    numeros.append(int(input("Digite um número: ")))

#percorrer o vetor e comparar os valores
while y < len(numeros):
    if y == 0:
        menor = numeros[y]
        maior = numeros[y]
    if numeros[y] > maior:
        maior = numeros[y]
    if numeros[y] < menor:
        menor = numeros[y]

print("O maior valor é:", maior, "O menor valor é:", menor)


#Exercicio 4

quant = int(input("Digite a quantidade de alunos: "))
notas = list()
abaixo = 0
acima = 0

for i in range(quant):
    notas.append(float(input("Digite a nota: ")))
    if notas[i] < 60:
        abaixo+=1
    else:
        acima +=1

print("Acima da média: %d alunos. Abaixo da média: %d alunos" %acima, abaixo)




