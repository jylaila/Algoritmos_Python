num1 = int(input("Digite o 1º número"))
num2 = int(input("Digite o 2º número"))

#2 forma
num1 = int(num1)
num2 = int(num2)

#3 forma
resultado = int(num1) + int(num2)

# print(resultado)

#conversões de tipo
#real - float
#inteiro = int
#caractere = str
#booleano = bool

total = float(input("Digite o peso do bolo: "))
numParticipantes = int(input("Digite a quantidade de participantes: "))

#%d - formata inteiro
#%f - formata float
#%s - formata string
print("Cada um vai comer %.2f gramas" % (total/numParticipantes))