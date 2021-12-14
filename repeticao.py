# import random

a = random.randint(1,10)

from random import randint


#enquanto (condicao) faca 
# //comandos
# fimenquanto


# repita
# //comandos
# ate (condicao)

# i = 1 #variável de controle

while i<=20:
    print(i)
    i = i+1 #mudar o valor da variável no laço de repetição

#jogo do adivinha

a = randint(1,10)
tent = 1
print(a)

while tent<=3:
    num = input("Digite um número de 1 a 10: ")
    if not num.isdigit(): 
        print("Digite um número inteiro.")
    else:
        if int(num) == a:
            print("Parabéns, você acertou na", tent, "ª tentativa!")
            break
        else:
            if tent==3:
                print("Você errou :(. O número gerado é", a)
            else:
                print("Você errou, tem ainda {} tentativas".format(3-tent))
        tent +=1            


