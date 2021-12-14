nota1 = 8.5
nota2 = 10
nota3 = 3.5
nota4 = 5

#vetor
nota = [8.5,10,3.5,5]
#posicao[0 , 1, 2, 3]

# print(nota1)
#vetor
# print(nota[0])

nota1 = 9
#atribuir valores ao vetor
nota[0] = 9
nota[2] = 6
nota[3] = 4
nota[1] = 10

media = [] #criando lista vazia

media = range(10) #gera uma lista de numeros
# print(media[2])

lista1 = [1,2,3,[4,5,6], "Antonio"]

#declaração de vetores
nomes = list()
nomes = []

#acesso sempre através dos índices 
# nomes[0]

numeros = [1,2,3,4,5,6,7,8,9,10]
cont = 0

while cont<10:
    # print(numeros[cont])#numeros[2]
    cont+=1

notas = []
i = 0

while i<10:
    # notas.append(input("Digite um numero"))
    i+=1

numeros = [10,20,"Frase",4,5,6,7,8,9,10]
for x in numeros:
    pass
    #  print(x)

z = 0
while z <10:
    print("Posicao:", z, "Valor:", numeros[z])
    z+=1

# numeros = [0=10,1=20,2="Frase",3=4,5,6,7,8,9,10]
for index, valor in enumerate(numeros):
    print("Posicao:", index, "Valor:", valor)



notas = [8.5, 10, 3.4, 7]
media = notas[0] + notas[1] + notas[2] + notas[3]

y = 0 #controlar a quantidade de repetições
media = 0

while y<4:
    # media = media + notas[y]
    media += notas[y]
    y+=1
print("A média é %.2f" % (media/4))

media = 0
for nota in notas:
    media += nota

print("A média é", (media/4))


