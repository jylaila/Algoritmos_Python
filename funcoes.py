#variaveis globais
num1 = int(input("num1:")) #10
num2 = int(input("num2:")) #20

def soma():
    num3 = 14 #variavel local
    print(num3)
    # num1 = num1+num2 #30
    
#chamada para a função
soma()    

# print("O numero digitado foi ", num1)#valor incorreto

# print(num3) #variaveis locais não são acessiveis fora do escopo

#3 formas de definir funções

#1 forma
#funcao sem parâmetro e sem retorno
def soma():
    num1 = int(input("num1:")) #10
    num2 = int(input("num2:")) #20
    print(num1+num2)
#chamada para funcao
soma()

#2Forma
#funcao com parâmetro e sem retorno
def soma(x, y):
    print(x+y)
    
#chamada para funcao
num1 = int(input("num1:")) #10
num2 = int(input("num2:")) #20

#chamada para funcao, passagem por valor
soma(num1, num2)
soma(1,2)
soma(num1, 20)
soma(10.5, num1)

#parâmetros opcionais, sempre por ultimo
def soma2(x, y, z=0):
    print(x+y+z)#30
    
#chamada
soma2(num1, num2, 10)
soma2(num1, num2)

#3Forma
#funcao com parâmetro e com retorno
def soma3(x, y):
    return x+y
    
#chamada da funcao
print(soma3(num1,num2))

resultado = soma3(num1, num2)

print(resultado)

#sobrescrita da função
def soma3(x, y):
    return x+y

soma3(5,7)