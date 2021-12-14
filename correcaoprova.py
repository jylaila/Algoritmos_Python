n = int(input("Digite um numero maior que 3:"))

for i in range(3,n):
    if i%2==1:
        print(i)
        
print("---Outra Forma---")
i = 3   
while i<n:
    print(i)
    i +=2
    
    
saldo = 500
print('-' * 30)
print("{0:^30}".format("Caixa Eletrônico"))
print('-' * 30)
print("1 - Saque\n2 - Depósito\n3 - Saldo")
opcao = int(input("Digite a opcao desejada:"))

if opcao == 1:
    valor = float(input("Digite o valor do saque: "))
    if valor <=saldo:
        saldo = saldo - valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
        
elif opcao == 2:
    valor = float(input("Digite o valor do deposito: "))
    if valor>0:
        saldo = saldo + valor
        print("Deposito efetuado com sucesso")
        
elif opcao == 3:
    print("Saldo atual %.2f"%saldo)

else:
    print("Opção inválida")
    
        