valorEmprestimo = float(input("Digite o valor do empréstimo:"))
salario = float(input("Salário: "))
parcelas = int(input("Parcelas: "))

if (valorEmprestimo/parcelas) <= (salario * 0.30):
    print("Pode emprestar :)")
else:
    print("Não pode emprestar")
    print("Quantidade mínima de parcelas para esse valor: ", int(valorEmprestimo/(salario*0.30)))

   