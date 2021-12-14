# declaracao de variáveis
num = 1

# entrada de dados
# num2 = int(input("Digite um número: "))
# num2 = int(num2)

# saída de dados
# print("Mensagem")

# Condicional Simples // Teste verdadeiro
# se (condicao) entao
# comandos
# fimse

a = 50
b = 20

# operadores relacionais
# == | >= | <= | > |< |! | !=

if a > b:
    print("A é maior que B")

# Condicional Composta // Testa verdadeiro, falso
# se (condicao) entao //if
# comandos
# senao entao //else
# comandos
# fimse

if a > b:
    print("A é maior que B")  # comandos se o resultado for verdadeiro
else:
    print("B é maior que A")  # comandos se o resultado for falso


num = int(input("Digite um número: "))

if num >= 0:
    print("Positivo")
else:
    print("Negativo")


cor = 'verde'
tamanho = 48

# conjuncao E AND &&

if cor == "verde" and cor == 'amarelo' and tamanho == 48:
    print("Roupa disponível")
else:
    print("Indisponível")

# Crie um programa em Python que receba um número e
# verifique se ele está no intervalo entre 10 e 20
# Execute o programa quantas vezes desejar, alterando os valores de entrada.

num = int(input("Digite um número: "))

if num >= 10 and num <= 20:
    print("Está no intervalo")
else:
    print("Não está no intervalo")


# disjunção ou OR ||

cor = "lilas"

if cor == "verde" or cor == "amarelo":
    print("Disponivel")
else:
    print("Indisponivel")

if cor == "verde" or cor == "amarelo" and tamanho == 48:
    print("OK")

# Crie um programa em Python que receba um número e
# verifique se esse número é ou não binário
# Execute o programa quantas vezes desejar, alterando os valores de entrada.

num = int(input("Digite um número: "))

if num == 0 or num == 1:
    print("Binário")
else:
    print("Não binário")


# media = 6 = C | media >6 e <= 8 = B | media >8  = A | media < 6 reprovado
media = 5

# senao
# se (condicao) entao
# fimse
if media < 6:
    print("R")
else:
    if media == 6:
        print("c")
    else:
        if media > 6 and media <= 8:
            print("B")
        else:
            print("A")

if media < 6:
    print("R")
elif media == 6:
    print("C")
elif media > 6 and media <= 8:
    print("B")
else:
    print("A")


categoria = int(input("Insira a categoria \n de 1 até 5"))
preco = 0

if categoria >= 1 and categoria <= 5:
    if categoria == 1:
        preco = 10
    elif categoria == 2:
        preco = 18
    elif categoria == 3:
        preco = 23
    elif categoria == 4:
        preco = 26
    elif categoria == 5:
        preco = 31
    else:
        print("Categoria Inválida!")

print("O preço é:", preco)


valorEmprestimo = float(input("Valor: "))
salario = float(input("Salario"))
parcelas = int(input("Parcelas"))

if (valorEmprestimo/parcelas) > salario * 0.30:
    print("Pode emprestar !")
else:
    print("Não Pode")
