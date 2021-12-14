# arquivo = open("contato.txt", 'w+')
# arquivo.write("\nBoa noite!")

# try:
#     arquivo = open("agenda.txt", 'r')#r obrigatorio que o arquivo exista
#     arquivo.write("Boa noite")
# except:
#     arquivo = open("agenda.txt", 'w')
# finally:
#     print("Acontece de qualquer jeito!")

#funcoes de leitura
# try:
#     arquivo = open("agenda.txt", 'r')
#     conteudo = arquivo.read() #retorna uma string
#     print(conteudo)
# except:
#     print("erro")

#string python lista de caracteres char = 1byte

# try:
#     agenda = list()
#     arquivo = open("agenda.txt", 'r')
#     #read(qtdbytes)
#     linha = " "
#     while linha!="":
#         linha = arquivo.readline() #retorna uma linha
#         print(linha)
# except:
#     print("erro")

# agenda = list()
# try:   
#     arquivo = open("agenda.txt", 'r')
#     #read(qtdbytes)
#     linha = " "
#     while linha!="":
#         linha = arquivo.readline().replace("\n", "") #retorna uma linha
#         linha = linha.split(",")
#         agenda.append(linha)
#         print(linha)
# except:
#     print("erro")
    
# print(agenda[0][0]) #caio
# arquivo = open("agenda.txt", 'r')
# # print(arquivo.name)
# conteudo = arquivo.readlines()
# print(conteudo[0])

# arquivo = open("agenda.txt", 'a')
# arquivo.write('Joao, (15) 2222-22222')

# vetor=["maca\n", "pera\n", "uva\n"]
# arquivo = open("frutas.txt", 'w')
# arquivo.writelines(vetor)
# arquivo.close()

with open ("agenda.txt") as arquivo:
    pass

import json

# load()#converte json p/ python
# dump()#converte python p/json

aluno = {
    'nome':'Joao',
    'telefone': 1111111
}

# open("aluno.json","w").write(json.dumps(aluno))

# with open("aluno.json", "r") as arquivo:
#     alunos= json.loads(arquivo.read())
#     print(alunos)
    

# alunos=[]
# alunos.append(aluno)
# alunos.append(aluno)
# alunos.append(aluno)
# alunos.append(aluno)

# open("aluno.json","w").write(json.dumps(alunos))
# with open("aluno.json", "r") as arquivo:
#     alunos= json.loads(arquivo.read())
#     print(alunos[0]['telefone'])
    

# import os 

# if os.path.exists("contato.txt"):
#     os.remove("contato.txt")

# os.rmdir("arquivo") #remove a pasta inteira

# os.mkdir("arquivo") #cria a pasta


string ="Fatec São Roque"
# #[inicio, fim,incremento] : 
# print(string[::-1])

# tamanho = len(string) #len tamanho

# string = string.upper()
# string = string.lower()
# separa = string.split(" ")#separando o contéudo até o espaço

# nome, endereco = input("Digite o nome o endereço").split()

# valores = input("Digite os valores").partition("-")
# print(valores)

string = string.replace(" ", "")
print(string)

#valorseverdadeiro if condicao else valorfalso
x = 10
a = 0

if x >=10:
    a = 1
else:
    a = 5
    
#operador ternário
#expressao ? verdadeiro : falso
#x>=10? a=1 : a=5

a = 1 if x>=10 else a=5
    

