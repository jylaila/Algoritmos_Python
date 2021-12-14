# import funcoes
# from funcoes import soma

#Crie uma função que mostre um menu com as seguintes opcoes:
#0 - Sair
#1 - Inserir
#2 - Alterar o telefone
#3 - Consultar o telefone
#4 - Excluir o aluno
#5 - Exibir a lista de todos os alunos

def menu():
    resposta = 1
    while resposta:
        resposta =int(input("\n\nMenu \n0 - Sair\n1 - Inserir\n2 - Alterar o telefone\n3 - Consultar o telefone\n4 - Excluir o aluno\n5 - Exibir a lista de todos os alunos\nDigite a opção desejada: "))
        if resposta == 0:
            print("Encerrando o Programa...")        
            # soma()   
            # funcoes.soma   
        elif resposta == 1 or resposta == 2:
            nome = input("Digite o nome do aluno: ") 
            telefone = input("Digite o telefone do aluno: ") 
                        
            if resposta == 1:
                inserir(nome, telefone)
            else:
                alterar(nome, telefone)
        elif resposta == 3:            
            nome = input("Digite o nome do aluno a ser pesquisado: ")
            consultar(nome)
            
        elif resposta == 4:
            nome = input("Digite o nome do aluno a ser removido: ")
            excluir(nome)
        
        elif resposta == 5:
            listar()
        
        else:
            print("Opção Inválida")
    
def inserir(nome, telefone):
    if aluno.get(nome):
        print("Aluno já existe!")
    else:
        aluno[nome] = telefone #{nome:'Fatec'} {'Caio':'11-33333'}
        print("Cadastro incluído com sucesso!")
    
def alterar(nome, telefone):
    if nome in aluno:
        aluno[nome] = telefone
        print("Cadastro alterado com sucesso")
    else:
        print("Cadastro não existe!")
        
def consultar(nome):
    if aluno.get(nome):
        print("Telefone: ", aluno[nome])
    else:
        print("Cadastro não existe!")
              
def excluir(nome):    
    if aluno.get(nome):
      aluno.pop(nome)
    else:
        print("Cadastro não existe!")

def listar():
    for nome in aluno.keys():
        print("\nNome: ", nome, "\nTelefone: ", aluno[nome])
      
#crio o dicionário vazio
aluno = {}     
#chamada para o menu
menu()

